# star quirky spiral
import turtle
t=turtle.Pen()

def star():
    for j in range(60):
        t.forward(40+(j*4))
        t.right(144 +1)    #( 180 - 36 )
#
star()
