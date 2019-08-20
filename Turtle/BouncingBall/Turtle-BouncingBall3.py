#Turtle Bouncing Ball Program
#Written by: Jeff Brusoe

import turtle
import random

def stop_loop(clickx,clicky):
    global endloop
    endloop = True
    return

MaxX = 400
MaxY = 300
MinX = -MaxX
Miny = -MaxY
turtle.setup(width=2*MaxX,height=2*MaxY)

turtle.title("Turtle Bouncing Ball")

turtle.bgcolor("Green")

ball = Turtle()
ball.hideturtle()
ball.penup()
