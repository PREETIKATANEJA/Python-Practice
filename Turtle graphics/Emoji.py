import turtle

emoji = turtle.Turtle()


emoji.up()
emoji.goto(0, -100)
emoji.down()

#emoji.bgcolor("#c2bca9")

#Drawing yellow circle
emoji.begin_fill()
emoji.fillcolor("yellow")
emoji.circle(100)
emoji.end_fill()

#drwaing the curve of smilie
emoji.up()
emoji.goto(-67, -10)
emoji.setheading(-60)
emoji.width(5)
emoji.down()
emoji.circle(80,120)
emoji.fillcolor("black")

#for drawing two eyes of our emojis 
for i in range(-35, 105, 70):
    emoji.up()
    emoji.goto(i,35)
    emoji.setheading(0)
    emoji.down()
    emoji.begin_fill()
    emoji.circle(10)
    emoji.end_fill()

turtle.done()
