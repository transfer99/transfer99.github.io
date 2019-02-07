# 3c4 star function
import turtle
t=turtle.Pen()
# get number of points
points=int(input("How many points ? "))
# get line length (in pixels)
length=int(input("Length of Line ? "))
#
def star2(points,length):
    t.forward(length)
    t.right(180 - (180/points))
#    
for j in range (points):
    star2(points,length)
