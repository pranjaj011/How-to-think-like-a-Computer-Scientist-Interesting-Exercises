import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.penup()
alex.goto(0,-100)
alex.pendown()
for x in range(8):
    alex.forward(100)
    alex.left(360/8)
wn.exitonclick()
