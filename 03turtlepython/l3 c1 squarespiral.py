# l3 square spiral
import turtle
t=turtle.Pen()

def squarespiral():
    for j in range(100):
        t.forward(j*2)
        t.right(90)

squarespiral()
