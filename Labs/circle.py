import turtle

def drawPolygon(t, sideLength, numSides, color):
    turnAngle = 360 / numSides
    t.fillcolor(color)
    t.begin_fill()
    for i in range(numSides):
        t.forward(sideLength)
        t.left(turnAngle)
    t.end_fill()
def drawCircle(anyTurtle, radius, color):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360, color)
def drawFilledCircle(anyTurtle, radius, color):
    drawCircle(anyTurtle, radius, color)

wn = turtle.Screen()
wheel = turtle.Turtle()

drawFilledCircle(wheel, 20, "red")

wn.exitonclick()
