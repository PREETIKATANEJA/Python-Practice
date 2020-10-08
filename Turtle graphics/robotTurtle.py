import turtle as t
import time as ti

def rectangle(hor,ver,col):
    t.pendown()
    t.pensize(1)
    t.color(col)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(hor)
        t.right(90)
        t.forward(ver)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('#8c8a85')

t.goto(-100,-150)
rectangle(50,20,'#45515e')
t.goto(-30,-150)
rectangle(50,20,'#45515e')

t.goto(-25,-50)
rectangle(15,100,'#356a70')
t.goto(-55,-50)
rectangle(-15,100,'#356a70')

t.goto(-90,100)
rectangle(100,150,'#bf192f')

t.goto(-150,70)
rectangle(60,15,'#356a70')
t.goto(-150,110)
rectangle(15,40,'#356a70')
t.goto(10,70)
rectangle(60,15,'#356a70')
t.goto(55,110)
rectangle(15,40,'#356a70')

t.goto(-50,120)
rectangle(15,20,'#356a70')
t.goto(-85,170)
rectangle(80,50,'#bf192f')
t.goto(-60,160)
rectangle(30,10,'white')
t.goto(-55,155)
rectangle(5,5,'black')
t.goto(-40,155)
rectangle(5,5,'black')
t.goto(-65,138)
rectangle(40,5,'black')

t.goto(-155,130)
rectangle(25,25,'#45515e')
t.goto(-147,130)
rectangle(10,15,t.bgcolor())
t.goto(50,130)
rectangle(25,25,'#45515e')
t.goto(58,130)
rectangle(10,15,t.bgcolor())

ti.sleep(10)

t.hideturtle()
