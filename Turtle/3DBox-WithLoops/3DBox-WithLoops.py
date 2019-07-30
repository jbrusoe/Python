#Python Turtle - 3D Box - With Loops
#Written By: Jeff Brusoe (jbrusoe@gmail.com)

import turtle

turtle.showturtle()

#Draw first rectangle
for i in range(1,3):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)


#Draw second rectangle
turtle.goto(-50,-50)
turtle.setheading(0)
for i in range(1,3):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

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
