import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
alex.penup()
alex.goto(50, -90)
alex.pendown()
for x in angles:
    alex.left(x)
    alex.forward(100)
print("The pirate's final heading is", alex.heading())
wn.exitonclick()
