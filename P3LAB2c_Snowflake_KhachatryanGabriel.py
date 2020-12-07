import turtle
turtle.Screen()

speedy = turtle.Turtle()
speedy.pencolor('blue')
speedy.speed('fastest')

# This function will be called by the branch function a few times to draw to little branches on the wings
def branch(turn, run):
    speedy.right(turn)
    speedy.forward(run)
    speedy.left(90)
    speedy.forward(3)
    speedy.left(90)
    speedy.forward(run)
    speedy.right(180-turn)

# This function will be called 8 times later to draw the snowflake
def wing():
    speedy.forward(50)
    branch(45, 40)
    speedy.left(30)
    speedy.forward(15)
    speedy.right(30)
    speedy.forward(20)
    branch(45, 70)
    speedy.left(30)
    speedy.forward(15)
    speedy.right(30)
    speedy.forward(15)
    speedy.right(30)
    speedy.forward(7)
    speedy.left(30)
    speedy.forward(20)
    speedy.right(45)
    for x in range(0, 6):        
        speedy.forward(10)
        speedy.left(45)
    speedy.forward(10)
    speedy.right(45)
    speedy.forward(20)
    speedy.left(30)
    speedy.forward(7)
    speedy.right(30)
    speedy.forward(15)
    speedy.right(30)
    speedy.forward(15)
    speedy.left(30)
    branch(135, 70)
    speedy.forward(20)
    speedy.right(30)
    speedy.forward(15)
    speedy.left(30)
    branch(135, 40)
    speedy.forward(50)

# Draw the center piece
for x in range(0, 8):
    speedy.forward(17)
    speedy.up()
    speedy.left(180)
    speedy.forward(7)
    speedy.left(90)
    speedy.forward(5)
    speedy.down()
    speedy.forward(75)
    speedy.right(90)
    speedy.forward(3)
    speedy.right(90)
    speedy.forward(75)
    speedy.right(90)
    speedy.forward(3)
    speedy.up()
    speedy.left(90)
    speedy.forward(5)
    speedy.right(90)
    speedy.forward(7)
    speedy.left(45)
    speedy.down()

# Move the pen to the starting position for the wing
speedy.up()
speedy.forward(57)
speedy.down()

# Now draw the 8 wings
for x in range(0, 8):
    wing()
    speedy.right(135)

# Move the turtle away from the finished drawing
speedy.up()
speedy.forward(200)
