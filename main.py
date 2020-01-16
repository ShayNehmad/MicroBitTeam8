import random
import time

from microbit import *
import tinybit


def taunt():
    display.show("!")
    import music
    music.play(music.BA_DING)


def wait_for_opponent():
    position = accelerometer.get_values()
    sensitivity = 2000

    initial_sumo_distance = tinybit.ultrasonic()
    MINIMUM_DISTANCE = 10

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
    dodge_f = random.choice([tinybit.car_turnright, tinybit.car_turnleft])
    dodge_f(200)
    time.sleep(0.1)

    # stop
    tinybit.car_run(0)

    # escape
    while (not tinybit.traking_sensor_L()) or (not tinybit.traking_sensor_R()):
        tinybit.car_run(100)
    tinybit.car_back(200)
    time.sleep(0.1)

    tinybit.car_run(0)


def push():
    display.show("P")
    tinybit.car_run(190)
    time.sleep(1)
    tinybit.car_run(0)


def main():
    while True:
        taunt()
        #wait_for_opponent()
        #crazy()
        #dodge()
        push()


main()
