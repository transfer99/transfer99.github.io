import turtle
t = turtle.Pen()
#
def square():
    for i in range(4):
        t.forward(50)
        t.right(90)
        
def outer1():
    for j in range (12):
        t.forward(100)
        t.right(120)
        t.forward(50)
        t.right(120)
        t.forward(100)
        t.right(150)
        # now draw a square
        square()
#
outer1()
