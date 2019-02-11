import turtle
t = turtle.Pen()
#
def square():
    for i in range(4):
        t.forward(200)
        t.right(90)
#
numbshapes = int(input("How many shapes ? "))
#
for i in range(numbshapes):
    square()
    t.right(360/numbshapes)
#
print("DONE")
