import unicornhathd as u
import time

x = 0
y = 0

while x < 15:
    u.set_pixel(x, y, 255, 255, 255)
    u.set_pixel(15 - x, y, 255, 255, 255)
    u.show()
    
    x += 1
    y += 1

    time.sleep(0.5)