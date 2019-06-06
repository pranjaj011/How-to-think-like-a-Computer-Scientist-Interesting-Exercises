import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
n = int(input("How many legs do you want the sprite to have?"))
angle = 360/n
for x in range(n):
    alex.left(angle)
    alex.forward(100)
    alex.stamp()
    alex.home()
    angle += 360/n
alex.home()
alex.shape("circle")
alex.stamp()
wn.exitonclick()
