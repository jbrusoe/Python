#Multiple Square Shapes
#Written by: Jeff Brusoe
#Last Updated: May 3, 2020

import turtle

turtle.showturtle()
turtle.width(5)

SideLength = 250
NumberOfSquares = 5

for i in range(0,NumberOfSquares):
    turtle.setheading(i*360/NumberOfSquares)

    turtle.forward(SideLength/2)

    for j in range(0,3):
        turtle.right(90)
        turtle.forward(SideLength)
    
    turtle.right(90)
    turtle.forward(SideLength/2)

turtle.hideturtle()
