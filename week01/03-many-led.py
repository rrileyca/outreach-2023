import unicornhathd as u
from random import randint

for i in range(0,1000000):
    x = randint(0, 15)
    y = randint(0, 15)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    u.set_pixel(x, y, r, g, b)
    u.show()