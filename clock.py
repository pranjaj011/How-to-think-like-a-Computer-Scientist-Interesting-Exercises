import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.stamp()
alex.pensize(3)
move = 30
for x in range(12):
    alex.penup()
    alex.forward(100)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(20)
    alex.stamp()
    alex.home()
    alex.right(move)
    move += 30
wn.exitonclick()
