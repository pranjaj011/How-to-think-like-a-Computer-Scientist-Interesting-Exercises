import turtle 
wn = turtle.Screen()
Alex = turtle.Turtle()
sides = int(input("How many numbers of sides do you want the shape to be?"))
length = int(input("How long should the length be?"))
bg_color= input("What should the background color be?")
polygon_color = input("What should the shape's color be?")
wn.bgcolor(bg_color)
Alex.fillcolor(polygon_color)
Alex.begin_fill()
for x in range(sides):
    Alex.right(360/sides)
    Alex.forward(length)
Alex.end_fill()
wn.exitonclick()
Alex.hideturtle()
