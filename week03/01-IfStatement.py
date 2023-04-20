import unicornhathd as u
import time  # Don't forget imports!

x = 0

while x < 16:
    if x % 2 == 1:  # Uses the modulo operator to find odd numbers
        u.set_pixel(x, 0, 255, 0, 0)
    else:
        u.set_pixel(x, 0, 0, 255, 0)
    u.show()
    x = x + 1
    time.sleep(0.5)  # Tells Python to sleep for 0.5 second(s)
