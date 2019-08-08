#Turtle Concentic Circle Demo with a loop
#Written by: Jeff Brusoe
#Last Updated: February 4, 2019

import turtle

turtle.showturtle

for i in range (200,10,-10):
    turtle.penup()
    turtle.sety(-1*i)
    turtle.pendown()
    turtle.circle(i)
