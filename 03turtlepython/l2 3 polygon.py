import turtle
t=turtle.Pen()
#
#def pentagon():
#    for i in range(5):
#        t.forward(200)
#        t.right(72)
#

def polygon(sides=6 , length=100):
    turn_angle=360/sides
    for k in range(sides):
        t.forward(length)
        t.right(turn_angle)
# with default 6 , 100
polygon()
# 10 sides
polygon(10)
# 12 sides 50 long
t.penup()
t.forward(-200)
t.pendown()
polygon(12,50)
