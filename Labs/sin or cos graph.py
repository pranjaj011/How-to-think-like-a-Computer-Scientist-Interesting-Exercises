import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(0, -2, 1000, 2)
fred = turtle.Turtle()
fred.penup()
fred.goto(-1, 0)
fred.pendown()
for x in range(721):
    y = math.cos(math.radians(x))
    fred.goto(x, y)
wn.exitonclick()
