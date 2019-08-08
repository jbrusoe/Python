#Python Turtle - Circle Step Parameter Demo
#Written by: Jeff Brusoe
#Last Updated: March 3, 2019

import turtle

turtle.showturtle()

turtle.penup()
turtle.goto(0,-200)
turtle.pendown()

for i in range (3,25):
    print("Step: " + str(i))
    turtle.circle(200,steps=i)
