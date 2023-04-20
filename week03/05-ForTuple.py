import unicornhathd as u
import time

myList = [
    (255,0,0),
    (0,255,0),
    (0,0,255)
]

for i in myList:
    u.set_all(*i)
    u.show()
    time.sleep(1)

