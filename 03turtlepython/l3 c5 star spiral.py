# 3c3 star
import turtle
t=turtle.Pen()

def star():
    for j in range(50):
        t.forward(40+(j*4))
        t.right(144)    #( 180 - 36 )
#
star()
