import turtle
turtle.Screen()

# changing the turtle's attributes
t = turtle.Turtle()
t.pencolor('blue')

# drawing an equilateral triangle
for x in range(0, 3):
    t.forward(100)
    t.left(120)

# moving the turtle away from the trangle to draw another shape
t.up()
t.forward(200)
t.down()

# now drawing a square
for x in range(0, 4):
    t.forward(100)
    t.left(90)
