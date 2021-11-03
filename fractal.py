import turtle as tl
def koch(angle, length, d):
    if d == 0:
        tl.forward(length)
        return
    subLength = length/3
    koch(angle, subLength, d-1)
    tl.left(angle)
    koch(angle, subLength, d - 1)
    tl.right(angle*2)
    koch(angle, subLength, d - 1)
    tl.left(angle)
    koch(angle, subLength, d - 1)


def tru(n, angle, length, d):
    tl.penup()
    tl.goto(0,0)
    tl.pendown()
    for i in range (n):
        koch(angle, length, d)
        tl.right(45*n)
tl.speed(0)
tru(1,87, 800, 3)
tl.done()

