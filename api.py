from microbit import i2c, spi, pin15, pin16, pin19, pin20, pin1, pin13, pin14

MAX_BYTE = (1 << 8) - 1
SPI_DATA_LENGTH = 250
SPI_BAUDRATE = 125000  # units: bytes/second ( = 1,000,000 bits/second = bit/microsecond)
SPEED_OF_SOUND = 0.0343  # units: cm/microsecond

g_i2c_initialized = False
g_spi_initialized = False


def init_i2c():
    global g_i2c_initialized
    if g_i2c_initialized is False:
        i2c.init(100000, pin20, pin19)
        g_i2c_initialized = True


def init_spi():
    global g_spi_initialized
    if g_spi_initialized is False:
        spi.init(baudrate=SPI_BAUDRATE, sclk=pin16, mosi=pin16, miso=pin15)
        g_spi_initialized = True


class I2C:
    I2C_ADDRESS = 1

    def __init__(self, _id):
        self._id = _id
        init_i2c()

    def i2c_write(self, *data):
        buffer = [self._id]
        buffer.extend(data)
        i2c.write(self.I2C_ADDRESS, bytearray(buffer))


class Motors(I2C):
    MOTOR_ID = 2

    def __init__(self):
        super(Motors, self).__init__(self.MOTOR_ID)

    @staticmethod
    def _normalize_input(x):
        return min(max(x, -1), 1)

    def drive(self, right_power, left_power):
        """
        :param right_power: Right motor power from -1 (max reverse) to 1 (max ahead)
        :param left_power: Left motor velocity from -1 (max reverse) to 1 (max ahead)
        """
        # ensure inputs are normalized within range -1 < speed < 1
        right_power, left_power = self._normalize_input(right_power), self._normalize_input(left_power)

        left_forward = int(MAX_BYTE * left_power if left_power > 0 else 0)  # Left Forward PWM
        left_backward = int(MAX_BYTE * -left_power if left_power < 0 else 0)  # Left Backward PWM
        right_forward = int(MAX_BYTE * right_power if right_power > 0 else 0)  # Right Forward PWM
        right_backward = int(MAX_BYTE * -right_power if right_power < 0 else 0)  # Right Backward PWM

        self.i2c_write(left_forward, left_backward, right_forward, right_backward)


class Headlights(I2C):
    LIGHTS_ID = 1

    def __init__(self):
        super(Headlights, self).__init__(self.LIGHTS_ID)

    @staticmethod
    def _normalize_input(x):
        return min(max(x, 0), MAX_BYTE)

    def light(self, red, green, blue):
        """
        :param red: Strength of red LED from 0 to 255
        :param green: Strength of green LED from 0 to 255
        :param blue: Strength of blue LED from 0 to 255
        """
        self.i2c_write(self._normalize_input(red), self._normalize_input(green), self._normalize_input(blue))


class Ultrasonic:
    @staticmethod
    def distance():
        """
        :return: Distance detected by Ultrasonic sensor in cm
        """
        init_spi()

        raw_data = bytearray(SPI_DATA_LENGTH)

        # set output high for 8us and read input
        raw_data[0] = MAX_BYTE
        spi.write_readinto(raw_data, raw_data)

        flight_time = 0
        for value in raw_data[:-2]:
            if flight_time > 0 and value == 0:
                break
            flight_time += bin(value).count("1")  # each high bit accounts for 1us of flight-time
        else:  # either signal never started or signal never ended
            return -1

        # divide by 2 since: flight-time * speed of sound = round trip distance
        return round(flight_time * SPEED_OF_SOUND / 2 * 10)  # Times 10 for magic reasons :shrug:


class Microphone:
    @staticmethod
    def listen():
        return pin1.read_analog()


class Tracking:
    def __init__(self):
        pin13.set_pull(pin13.NO_PULL)
        self._left_pin = pin13
        pin14.set_pull(pin14.NO_PULL)
        self._right_pin = pin14

    def get_left(self):
        return self._left_pin.read_digital()

    def get_right(self):
        return self._right_pin.read_digital()
