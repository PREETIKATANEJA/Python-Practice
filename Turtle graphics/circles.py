from turtle import *

bgcolor("black")
speed(0)

penup()
goto(-200, 0)
pendown()

for i in range(3):
    for colors in ["#094eed", "#eb6709", "#09eb49", "#eb098d", "#09ebdc", "#ebdc09"]:
        color(colors)
        pensize(3)
        circle(150)
        forward(20)
        