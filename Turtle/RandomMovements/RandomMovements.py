#Python - Randomly Move Turtle Around Screen
#Written by: Jeff Brusoe
#Last Updated: February 25, 2019

import turtle
import random

turtle.showturtle()

#Calculate window width and height
WindowHeight = turtle.Screen().window_height()
WindowWidth = turtle.Screen().window_width()
    
for i in range(1,500):
    Forward = random.randint(25,150)
    Angle = random.randint(10,100)

    #In next lesson, use this as demo of the use of an "or" with if/then
    if (abs(turtle.xcor()) + Forward) > (WindowWidth/2):
        #Note: In later lessons, use this as a function demo.
        RandomX = random.randint(-50,50)
        RandomY = random.randint(-50,50)
        turtle.width(7)
        turtle.color("blue")
        turtle.goto(RandomX,RandomY)
    elif (abs(turtle.ycor()) + Forward) > (WindowHeight/2):
        #Note: In later lessons, use this as a function demo.
        RandomX = random.randint(-50,50)
        RandomY = random.randint(-50,50)
        turtle.width(7)
        turtle.color("purple")
        turtle.goto(RandomX,RandomY)
    else:
        turtle.width(1)
        turtle.color("black")
        turtle.forward(Forward) 
        turtle.left(Angle)
