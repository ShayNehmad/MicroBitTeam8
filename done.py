"""

LM_FACTOR = 1.0
RM_FACTOR = 0.8

mic = Microphone()

display.show(Image.SMILE)


def show_volume():
    volume = mic.listen()
    how_strong = int(volume / 100)

    board = ""
    line = str(how_strong) * 5 + ":"
    board += line
    if how_strong > 2:
        board += line
    if how_strong > 4:
        board += line
    if how_strong > 6:
        board += line
    if how_strong > 8:
        board += line
    board = board[:-1]

    display.show(Image(board))

motors = Motors()

while True:
    show_volume()
    if mic.listen() > 500:
        motors.drive(-1, -1)
        time.sleep(0.1)
        motors.drive(0, 0)

"""


# game
"""
songs = {
    "BEETHOVAN": ['r4:2', 'g', 'g', 'g', 'eb:8', 'r:2', 'f', 'f', 'f', 'd:8'],
    "ENTERTAINER": music.ENTERTAINER,
    "DOREMI": ['c', 'd', 'e:2', 'd', 'e', 'd', 'e', 'd', 'e', 'f', 'f', 'e', 'd', 'e', 'f'],
    "STARWARS": ['a4:4', 'a', 'a', 'f3:4', 'c5:2', 'a4:4', 'f3:4', 'c5:2', 'a4:4', "e5:4", "e", "e"]
}


# Game challenge
def displayclock():
    display.show(Image.ALL_CLOCKS)


def main():
    points = 0
    while True:
        display.show(str(points))

        song_to_play = random.choice(list(songs.keys()))
        song_to_say = random.choice(list(songs.keys()))

        speech.say("ready set go")

        time.sleep(1)

        music.play(songs[song_to_play])

        display.scroll(song_to_say)

        should_press_a = song_to_play == song_to_say

        displayclock()

        if button_a.is_pressed():
            if should_press_a:
                display.show(Image.HAPPY)
                points += 1
            else:
                display.show(Image.SAD)
        elif button_b.is_pressed():
            if should_press_a:
                display.show(Image.SAD)
            else:
                display.show(Image.HAPPY)
                points += 1
        else:
            display.show(Image.ANGRY)
            points -= 1

        time.sleep(1)


main()
"""


# Rock Paper Scissors
"""
rock = Image("09990:"
             "99999:"
             "99999:"
             "99999:"
             "09990")
​
paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")
​
scissors = Image("90009:"
                 "09090:"
                 "00900:"
                 "99099:"
                 "99099")
​
​
while True:
    if accelerometer.was_gesture('shake'):
        display.show(random.choice([rock, paper, scissors]))
"""

# stage 2.3 response speed
"""
while True:
    numbers = range(0, 9)

    chosen_number = random.choice(numbers)
    should_press_a = bool(chosen_number >= 5)

    display.clear()
    display.show(str(chosen_number))
    time.sleep(1.5)
    display.clear()

    if button_a.is_pressed():
        if should_press_a:
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
    elif button_b.is_pressed():
        if should_press_a:
            display.show(Image.SAD)
        else:
            display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)

    time.sleep(2)
"""

# stage numbers game
"""
a = 0
while True:
    if button_a.is_pressed():
        a += 1
        display.show(a)
    elif button_b.is_pressed():
        a -= 1
        display.show(a)
"""

# stage Whack-a-mole
"""
from microbit import display, button_a, button_b
import random
​
while True:
    x = random.choice([0, 1, 3, 4])
    y = random.randrange(5)
​
    display.set_pixel(x, y, 9)
​
    while True:
        if button_a.is_pressed() and x > 2:
            break
        elif button_b.is_pressed() and x < 2:
            break
​
    display.set_pixel(x, y, 0)
"""

# Stage Knight Rider
"""
knight_rider = [
    Image("00000:"
          "00000:"
          "57900:"
          "00000:"
          "00000"),
​
    Image("00000:"
          "00000:"
          "05790:"
          "00000:"
          "00000"),
​
    Image("00000:"
          "00000:"
          "00579:"
          "00000:"
          "00000"),
​
    Image("00000:"
          "00000:"
          "00097:"
          "00000:"
          "00000"),
​
    Image("00000:"
          "00000:"
          "00975:"
          "00000:"
          "00000"),
​
    Image("00000:"
          "00000:"
          "09750:"
          "00000:"
          "00000"),
​
    Image("00000:"
          "00000:"
          "97500:"
          "00000:"
          "00000"),
​
    Image("00000:"
          "00000:"
          "79000:"
          "00000:"
          "00000"),
​
]
​
display.show(knight_rider, loop=True, delay=100)
"""

# stage G smiling buttons
"""
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    else:
        display.clear()
"""


# stage 4 logo​
"""
logo = [
    [5, 9, 9, 9, 5],
    [2, 9, 0, 9, 2],
    [5, 9, 9, 9, 5],
    [2, 9, 0, 9, 2],
    [5, 9, 9, 9, 5]
]
for x in range(5):
    for y in range(5):
        display.set_pixel(x, y, logo[y][x])
"""

# stage 3 beating heart
"""
for i in range(1, 10):
    display.show(Image.HEART)
    time.sleep(1)
    display.clear()
    time.sleep(1)
"""

# stage 1
"""
display.scroll("hello world")
"""



# stage 2 name tags

"""
display.scroll("shay")
time.sleep(1)
display.scroll("yoni")
time.sleep(1)
display.scroll("yaron")
time.sleep(1)
display.clear()
"""


# stage 1
"""
display.show(Image.HEART)
"""
