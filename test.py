import time
from lights import Lights
from rainbowio import colorwheel

pixels = Lights()
num_pixels = len(pixels)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

for c in [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]:
    color_chase(c, 0.01)
    print(c)
    # Increase or decrease to change the speed of the solid color change.

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    print("rainbow")
    rainbow_cycle(0)  # Increase the number to slow down 