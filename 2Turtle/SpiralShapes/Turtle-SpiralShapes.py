#Python Turtle - Spiral Shapes
#Written by: Jeff Brusoe
#Last Updated: May 3, 2020

import turtle

turtle.showturtle()
turtle.width(5)

InitialLength = 10
NumberOfLines = 30
Angle = 60

for i in range(0,NumberOfLines):
    turtle.forward((i+1)*InitialLength)
    turtle.right(Angle)

turtle.hideturtle()
