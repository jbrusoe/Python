#Turtle - Offset rectangeles (Without if statements)
#Written by: Jeff Brusoe
#Last Updated: February 12, 2019

import turtle

turtle.showturtle()

turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()

for i in range(1,3):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(-50,0)
turtle.pendown()

for i in range(1,3):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

turtle.hideturtle()
