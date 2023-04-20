import unicornhathd as u
import time

mySecretNumber = "7"

while True:
    guess = input("Guess my number: ")
    if guess == mySecretNumber:
        u.set_all(0, 255, 0)
    else:
        u.set_all(255, 0, 0)
    
    u.show()
    time.sleep(1)
    
    u.clear()
    u.show()