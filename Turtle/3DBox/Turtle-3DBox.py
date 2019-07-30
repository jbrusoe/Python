#Python Turtle - 3D Box - No Loops
#Written By: Jeff Brusoe (jbrusoe@gmail.com)

import turtle

turtle.showturtle()

#Draw first rectangle
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)

#Draw second rectangle
turtle.goto(-50,-50)
turtle.setheading(0)
turtle.forward(200)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(200)
turtle.setheading(270)
turtle.forward(100)

#Draw connecting lines
turtle.penup()
turtle.goto(150,-50)
turtle.pendown()
turtle.goto(200,0)
turtle.penup()
turtle.goto(150,50)
turtle.pendown()
turtle.goto(200,100)
turtle.penup()
turtle.goto(-50,50)
turtle.pendown()
turtle.goto(0,100)
