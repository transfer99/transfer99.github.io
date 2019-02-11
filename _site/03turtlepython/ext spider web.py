import turtle
t = turtle.Pen()
t.speed(10)     # draw fast
# extension - spider web
#
def triangle(length=50):   
    for i in range(3):
        t.forward(length)
        t.right(120)
#
def triangleflower(length=50,count=2):
    for k in range(count):
        triangle(length)
        t.right(360/count)
#
def web():
    for j in range(7):
        triangleflower(j*25,18)
#
web()
