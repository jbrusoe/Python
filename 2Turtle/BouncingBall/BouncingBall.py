#Turtle Bouncing Ball Program
#Written by: Jeff Brusoe

import turtle
import random

MaxX = 400
MaxY = 300
MinX = -MaxX
MinY = -MaxY
turtle.setup(width=2*MaxX,height=2*MaxY)

turtle.title("Turtle Bouncing Ball")

turtle.bgcolor("Green")

ball = turtle.Turtle()
ball.shape("circle")
ball.turtlesize(3,3)
ball.penup()
ball.speed(6)
dy = -5
dx = 5

def OnYEdge(y):
    if y > MaxY or y < MinY:
        return True

def OnXEdge(x):
    if x > MaxX or x < MinX:
        return True
    
while True:
    if OnYEdge(ball.ycor()):
        dy *= -1

    if OnXEdge(ball.xcor()):
        dx *= -1

    ball.sety(ball.ycor() + dy)
    ball.setx(ball.xcor() + dx)
