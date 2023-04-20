import unicornhathd as u
import time

i = 0

while True:
    u.clear()
    if i % 2 == 1:
        x = 0
        y = 0
        while x < 15:
            u.set_pixel(x, y, 255, 255, 255)
            u.set_pixel(15 - x, y, 255, 255, 255)
            x = x + 1
            y = y + 1
    else:
        x = 0
        while x < 15:
            u.set_pixel(x, 7, 255, 255, 255)
            x = x + 1
        y = 0
        while y < 15:
            u.set_pixel(7, y, 255, 255, 255)            
            y = y + 1
    u.show()
    time.sleep(0.1)
    i = i + 1