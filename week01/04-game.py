import unicornhathd as u
import keyboard

u.clear()
x = 7
y = 7

def move_up(int: y) -> int:
    if y == 15:
        return y
    return y + 1

def move_down(int: y) -> int:
    if y == 0:
        return y
    return y - 1

def move_right(int: x) -> int:
    if x == 15:
        return x
    return x + 1

def move_left(int: x) -> int:
    if x == 0:
        return x
    return x - 1

while True:
    u.set_pixel(x, y, 255, 255, 255)
    u.show()
    move = input("Move: ")
    if move == "w":
        y = move_up(y)
    elif move == "s":
        y = move_down(y)
    elif move == "d":
        x = move_right(x)
    elif move == "a":
        x = move_left(x)
    elif move == "exit":
        print("Thans for playing, goodbye!")
        exit(0)
    elif move == "reset":
        x = 7
        y = 7
        u.clear()
    else:
        print("Whoops, '" + move + "' is not a valid command. Type: 'w', 's', 'a', or 'd' (or - exit/reset)")