import unicornhathd as u

a = 0
b = 0

while a < 10:
     while b < 5:
          print("Hello!")
          b = b + 1
     u.set_pixel(0, a, 255, 255, 255)
     print(a)
     a = a + 1

u.show()