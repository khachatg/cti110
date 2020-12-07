import turtle
turtle.Screen()

# changing the turtle's attributes
t = turtle.Turtle()
t.pencolor('blue')
t.pensize(5)

# my initials are GK
# let's start drawing the letter G
t.left(90)
t.circle(50, 90)
t.forward(10)
t.circle(50, 90)
t.forward(40)
t.circle(50, 90)
t.forward(10)
t.circle(50, 90)
t.left(90)
t.forward(25)
t.left(180)
t.up()
t.forward(25)
t.right(90)
t.down()
t.forward(50)

# now we need to move the turtle away from G
t.up()
t.left(90)
t.forward(40)
t.down()

# now let's draw the letter K
t.left(90)
t.forward(140)
t.up()
t.left(180)
t.forward(70)
t.down()
t.left(135)
t.forward(100)
t.up()
t.left(180)
t.forward(100)
t.down()
t.left(90)
t.forward(100)
