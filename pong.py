import time

import radio
import random
from microbit import display, Image, button_a, button_b, sleep

radio.config(channel=69)

# The radio won't work unless it's switched on.
radio.on()

sent = None


board = [
    "00000",  # player 1
    "00000",
    "00000",
    "08980",
    "78987",  # net
    "08980",
    "00000",
    "00000",
    "00000",  # Player 2
]

starting = 4

def clear_screens():
    display.clear()
    radio.send("CLEAR")

def server_wins():
    display.show(Image.SMILE)
    radio.send("WIN")

def client_wins():
    display.show(Image.SMILE)
    radio.send("LOSE")


def draw_screen():
    server_board = board[0:5]
    client_board = reversed(board[4:9])

    display.show(Image(str(':'.join(server_board))))
    radio.send(str(':'.join(client_board)))


def push():
    global starting
    board[starting] = "00000"
    starting += 1
    board[starting] = "78987"


def pull():
    global starting
    board[starting] = "00000"
    starting += 1
    board[starting] = "78987"

def player_right():
    global player_location
    if player_location < 3:
        player_location += 1


def start_client():
    while True:
        radio.send("SYN")
        server_response = radio.receive()
        if server_response == "ACK":
            return True


def start_server():
    while True:
        client_connected = radio.receive()
        if client_connected == "SYN":
            display.show(Image.ARROW_NW)
            radio.send("ACK")
            return True


def main(server=False):
    if server:
        display.show(Image.FABULOUS)
        start_server()
    else:
        start_client()

    if server:
        draw_screen()
        # Event loop.
        while True:
            should_redraw = False
            if button_a.was_pressed():
                pull()
                should_redraw = True
            elif radio.receive() == "A":
                push()
                should_redraw = True
            if should_redraw:
                draw_screen()

main(True)
