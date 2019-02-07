import turtle
t = turtle.Pen()
#
def square():
    for i in range(4):
        t.forward(100)
        t.right(90)
#
for i in range(18):
    square()
    t.right(20)
