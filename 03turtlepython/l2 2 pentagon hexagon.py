import turtle
t=turtle.Pen()
#
def pentagon():
    for i in range(5):
        t.forward(200)
        t.right(72)
#
def hexagon():
    for j in range(6):
        t.forward(150)
        t.right(60)
#
pentagon()
t.forward(-250)
hexagon()
