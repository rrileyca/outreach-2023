import unicornhathd as u
import time

def increment_time(value: int, boundary: int) -> int:
    retval = value + 1
    if retval > boundary:
        return 0
    return retval

def increment_hours(value: int) -> int:
    return increment_time(value, 24)

def increment_minutes(value: int) -> int:
    return increment_time(value, 60)

def increment_seconds(value: int) -> int:
    return increment_time(value, 60)

def get_binary_array(num: int) -> list[int]:
    arr = [int(x) for x in bin(num)[2:]]
    size = len(arr)
    diff = 6 - size
    for i in range(0, diff):
        arr.insert(0, 0)
    return arr

def led_on_or_off(val: bool) -> int:
    if val:
        return 255
    return 0

def render_number(val: bool, x: int, y: int) -> None:
    u.set_pixel(x, y, led_on_or_off(val), led_on_or_off(val), led_on_or_off(val))

def render_hours(val: int) -> None:
    arr = get_binary_array(val)
    for i,v in enumerate(arr):
        on = v == 1
        render_number(on, i, 0)
        render_number(on, i, 1)
        render_number(on, i, 2)

def render_mins(val: int) -> None:
    arr = get_binary_array(val)
    for i,v in enumerate(arr):
        on = v == 1
        render_number(on, i, 4)
        render_number(on, i, 5)
        render_number(on, i, 6)

def render_sec(val: int) -> None:
    arr = get_binary_array(val)
    for i,v in enumerate(arr):
        on = v == 1
        render_number(on, i, 8)
        render_number(on, i, 9)
        render_number(on, i, 10)

def render_box() -> None:
    for i in range (0, 7):
        u.set_pixel(i, 11, 0, 255, 0)
    
    for i in range (0, 11):
        u.set_pixel(6, i, 0, 255, 0)

def render_clock(h: int, m: int, s: int) -> None:
    render_sec(s)
    render_mins(m)
    render_hours(h)

hours = 0
minutes = 0
second = 0
     
while True:
    time.sleep(1)
    u.clear()
    render_box()
    second = increment_seconds(second)
    if second == 0:
        minutes = increment_minutes(minutes)
        if minutes == 0:
            hours = increment_hours(hours)
    render_clock(hours, minutes, second)
    u.show()
    print(f"Current time is: {hours:02}:{minutes:02}:{second:02}")