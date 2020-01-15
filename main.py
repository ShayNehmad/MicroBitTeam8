import random
import time

from microbit import *
import tinybit


def taunt():
    display.show("T")
    import music
    music.play(music.BA_DING)


def wait_for_opponent():
    position = accelerometer.get_values()
    sensitivity = 1500

    initial_sumo_distance = tinybit.ultrasonic()
    MINIMUM_DISTANCE=5
    while True:
        # Check not touched
        movement = accelerometer.get_values()
        if any([(movement[i] - position[i]) > sensitivity for i in range(3)]):
            display.show("N")
            return
        position = movement

        current_sumo_distance = tinybit.ultrasonic()
        if (current_sumo_distance < MINIMUM_DISTANCE) or (current_sumo_distance < initial_sumo_distance / 2):
            display.show(Image.ANGRY)
            return


def dodge():
    # turn
    random.choice([tinybit.car_spinright, tinybit.car_spinleft])(220)
    # tinybit.car_spinright(220)
    time.sleep(0.1)

    tinybit.car_run(0)
    # escape
    while (not tinybit.traking_sensor_L()) or (not tinybit.traking_sensor_R()):
        tinybit.car_run(42)
    tinybit.car_back(255)
    time.sleep(0.1)

    tinybit.car_run(0)


def main():
    while True:
        taunt()
        wait_for_opponent()
        dodge()

main()
