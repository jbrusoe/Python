#Turtle Bouncing Ball Program
#Written by: Jeff Brusoe
#Last Updated: February 7, 2020

import turtle

MaxX = 400
MaxY = 300
MinX = -MaxX
MinY = -MaxY

#Configure window
turtle.setup(width=2*MaxX,height=2*MaxY)
turtle.title("Turtle Bouncing Ball")
turtle.bgcolor("Green")

#Configure ball
ball = turtle.Turtle()
ball.shape("circle")
ball.turtlesize(3,3)
ball.penup()
ball.speed(6)
dy = -5
dx = 5

#These functions determine if the ball has hit the edge of the screen
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
