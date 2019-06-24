import turtle
def drawSquare(t, sz, sides):
    """Make turtle t draw a square of sz."""

    for i in range(sides):
        t.forward(sz)
        t.left(360/sides)
def drawTriangle(a, b, c):
    drawSquare(a, b, c)
def drawOctagon(a, b, c):
    drawTriangle(a, b, c)
tess = turtle.Turtle()
wn = turtle.Screen()
drawTriangle(tess, 50, 3)
drawOctagon(tess, 50, 8)
