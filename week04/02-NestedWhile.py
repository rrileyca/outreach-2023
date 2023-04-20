import unicornhathd as u

x = 0
y = 0

while x < 3:
    print("Hello from outer loop!")
    
    while y < 3:
        print("|-- We are in the inner loop")
        u.set_pixel(x, y, 255, 255, 255)
        y = y + 1
    

    y = 0
    x = x + 1
    u.show()