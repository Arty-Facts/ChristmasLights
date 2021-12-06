import board
import neopixel
from time import sleep

pixel_pin = board.D18
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1)
pixels.fill((0,0,0))
sleep(2)
pixels.fill((255,0,0))
pixels.show()