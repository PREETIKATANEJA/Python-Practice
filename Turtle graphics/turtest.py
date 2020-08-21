#TURTLE

import turtle

turtle.speed(0)
turtle.bgcolor("black")

for i in range(5):
    for colors in ["#05ebc8", "#eb0537", "#f0f3f5", "#d4f005", "#094eed"]:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        


turtle.done()
