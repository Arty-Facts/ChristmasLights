import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.D18
num_pixels = 100

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)
pixels.fill((0,0,0))
pixels.show()

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (0, 255, 0)
YELLOW = (150, 255, 0)
GREEN = (255, 0, 0)
CYAN = (255, 0, 255)
BLUE = (0, 0, 255)
PURPLE = (0, 180, 255)
print("Running...")
i = 1
for c in [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]:
    print(f"fill {c}")
    color_chase(c, 0.01)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
print("while")
while True:
    rainbow_cycle(0)  # Increase the number to slow down the rainbow
    print(f"cycle {i}", end="\r")
    i += 1