import unicornhathd as u
import time 

x = 0
y = 0

while x < 16:
    while y < 16:
        if x % 2 == 1: 
            u.set_pixel(x, y, 255, 0, 0)
        else:
            u.set_pixel(x, y, 0, 255, 0)
        u.show()
        y = y + 1
        time.sleep(0.1)
    x = x + 1
    y = 0

