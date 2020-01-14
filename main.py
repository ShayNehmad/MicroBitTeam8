import time

from microbit import *



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

# stage 1
"""
display.show(Image.HEART)
"""
