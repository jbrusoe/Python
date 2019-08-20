#Python Turtle Graphics Demo - Drawing angles
#Written by: Jeff Brusoe (jbrusoe@gmail.com)

import turtle

turtle.showturtle()

turtle.title("Drawing Angles with Python Turtle")

#Define an array to hold the angles
angles = [0,30,45,60,90,120,180,270]

for angle in angles:
    turtle.up()
    turtle.goto(0,0)
    turtle.setheading(angle)
    turtle.down()
    turtle.forward(200)

    #Note: Default font size is 8
    turtle.write(" %s degrees" %angle, font=("Arial",14,"bold"))

turtle.hideturtle()


