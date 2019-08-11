#Python Turtle - Draw 4 Squares
#Written By: Jeff Brusoe
#Last Updated: February 4, 2019

import turtle

turtle.showturtle()

#Draw outer square
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)

#Draw line separating two inner squares on left
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.setheading(180)
turtle.forward(100)

#Draw line down the middle separating inner squares

turtle.penup()
turtle.goto(0,100)
turtle.setheading(270)
turtle.pendown()
turtle.forward(200)

turtle.hideturtle()
