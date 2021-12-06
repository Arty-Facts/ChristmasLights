
from colr import color
ON_PI=True
try:
    import board
    import neopixel
except Exception as e:
    print(e)
    print("="*20)
    ON_PI=False

        
def GRB2RGB(pixel):
    g, r, b = pixel
    return r, g, b
def RGB2GRB(pixel):
    r, g, b= pixel
    return g, r, b

def colored(pixel, text="o"):
    g, r, b = pixel
    return color(text, fore=(r, g, b), back=(0, 0, 0))

class demo_board:
    def __init__(self, pixel_pin, nb_ligths, brightness, auto_write):
        self.len = nb_ligths

        self.data = [(0,0,0) for i in range(nb_ligths)]
    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, rgb):
        self.data[key] = rgb

    def fill(self, v):
        self.data = [v for i in range(self.len)]

    def show(self):
        print("".join(map(colored, self.data)), end="\r")


if ON_PI:
    pixel_pin = board.D18
    impl_bord = neopixel.NeoPixel
else:
    pixel_pin = None
    impl_bord = demo_board


class Lights():
    def __init__(self, nb_ligths=100, brightness=1, auto_write=False):
        self.nb_ligths = nb_ligths

        self.pixels = impl_bord(pixel_pin, nb_ligths, brightness=brightness, auto_write=auto_write)
        self.clear_all()

    def __str__(self) -> str:
        return "".join(map(colored, self.pixels))

    def __del__(self):
        self.clear_all()

    def __getitem__(self, key):
        return GRB2RGB(self.pixels[key])

    def __setitem__(self, key, rgb):
        self.pixels[key] = RGB2GRB(rgb)

    def __len__(self):
        return self.nb_ligths

    def clear_all(self):
        self.pixels.fill((0,0,0))
        self.show()

    def show(self):
        self.pixels.show()

    def apply(self, func, *args, **kwargs):
        func(self.pixels, *args, **kwargs)
        self.clear_all()



