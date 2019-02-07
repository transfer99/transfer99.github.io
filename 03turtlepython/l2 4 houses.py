import turtle
t=turtle.Pen()
#
def triangle(length=100):
    for i in range(3):
        t.forward(length)
        t.right(120)
#
def square(length=100):
    for i in range(4):
        t.forward(length)
        t.right(90)
# to draw the house dooe
def rectangle(length=100):
    t.forward(length)
    t.right(90)
    t.forward(length/2)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length/2)
    t.right(90)
# position on screen so can draw on all of it
t.penup()
t.backward(300)
t.pendown()
# how big is the house
size=150
# outside house squre
t.left(90)
square(size)
# window 1 (left)
t.penup()
t.forward(size*0.8)
t.right(90)
t.forward(size*0.2)
t.pendown()
square(size*0.2)
t.penup()
#window 2 (right)
t.forward(size*0.4)
t.pendown()
square(size*0.2)
t.penup()
# roof
t.pencolor("red")
t.backward(size*0.6)
t.left(90)
t.forward(size*0.2)
t.pendown()
t.right(30)
triangle(size)
# house door
t.pencolor("black")
t.penup()
t.right(150)
t.forward(size)
t.left(90)
t.forward(size*0.4)
t.left(90)
t.pendown()
rectangle(size*0.4)
t.right(90)
t.forward(size*0.6)
