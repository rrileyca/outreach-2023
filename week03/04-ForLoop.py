import unicornhathd as u

myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in myList:
    u.set_pixel(i, 0, 255, 255, 255)

u.set_pixel(1, 1, *(255, 255, 255))
u.show()

