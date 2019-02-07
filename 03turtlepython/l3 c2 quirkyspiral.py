# l3 quirky spiral
import turtle
t=turtle.Pen()

def quirkyspiral():
    for j in range(100):
        t.forward(j*2)
        t.right(91)

quirkyspiral()
