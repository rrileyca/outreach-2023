import unicornhathd as u

x = 0

while x < 3:
    u.set_pixel(x, 0, 255, 255, 255)
    u.show()
    print("I showed the pixel!")
    x = x + 1