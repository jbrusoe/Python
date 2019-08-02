#Turtle - 4 Circles Demo
#Written by: Jeff Brusoe
#Last Updated: February 4, 2019

import turtle

turtle.showturtle()

turtle.penup()
turtle.goto(100,0)
turtle.pendown()

turtle.circle(100)

turtle.penup()
turtle.goto(-100,0)
turtle.pendown()

turtle.circle(100)

turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()

turtle.circle(100)

turtle.penup()
turtle.goto(100,-200)
turtle.pendown()

turtle.circle(100)
