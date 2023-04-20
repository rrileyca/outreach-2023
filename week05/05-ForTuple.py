import unicornhathd as u
import random as r
import time


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

for i in range(0,16):
    randomNumber = r.randint(0, 2)
    
    if randomNumber == 0:
        u.set_pixel(i, 0, *RED)
    elif randomNumber == 1:
        u.set_pixel(i, 0, *GREEN)
    elif randomNumber == 2:
        u.set_pixel(i, 0, *BLUE)
    else:
        print("Something went SERIOUSLY wrong. Maybe we got hit by ionising radiation?")

    u.show()
    time.sleep(0.5)

