from math import fmod
from random import triangular
import turtle


turtle.pendown()
#turtle.penup()

turtle.bgcolor("white")
turtle.pensize(10)
turtle.pen(fillcolor="black", pencolor="Cyan", pensize=10)
turtle.circle(100)
turtle.pen(fillcolor="Cyan", pencolor="black", pensize=10)
turtle.circle(50)

turtle.color("Red", "white")
turtle.begin_fill()
turtle.filling()
turtle.circle(80)
turtle.end_fill

turtle.pensize(5)
turtle.pen(fillcolor="Green", pencolor="Red", pensize=5)
turtle.fd(100)
turtle.pensize(10)
turtle.pen(fillcolor="Green", pencolor="Red", pensize=5)
turtle.right(45)
turtle.begin_fill()
turtle.filling()
turtle.circle(120)
turtle.pen(fillcolor="Blue", pencolor="Blue", pensize=5)
turtle.circle(90)
turtle.pen(fillcolor="Yellow", pencolor="Yellow", pensize=5)
turtle.circle(60)
turtle.pen(fillcolor="cyan", pencolor="cyan", pensize=5)
turtle.circle(30)
turtle.end_fill

turtle.pensize(5)
turtle.pen(fillcolor="Green", pencolor="Red", pensize=5)
turtle.bk(300)
turtle.left(300)
turtle.begin_fill()
turtle.filling()
turtle.fd(220)
turtle.end_fill


turtle.home()

turtle.isdown()

turtle.done