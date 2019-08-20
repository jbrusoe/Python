#Move Python Turtle with arrow keys
#Written by: Jeff Brusoe
#Last Updated: February 5, 2019

import turtle
 
TurtleScreen = turtle.Screen()
TurtleScreen.title("Moving Turtle with Arrow Keys") 
TurtleScreen.bgcolor("lightgreen")

turtle.showturtle()
 
def Forward():
  turtle.forward(30)

  #Handle condition when turtle touches left or right side of screen
  if turtle.xcor() >= TurtleScreen.window_width()/2 or turtle.xcor() <= -1*TurtleScreen.window_width()/2:
    turtle.left(180)

  #Handle condition when turtle touches top or bottom of screen
  if turtle.ycor() >= TurtleScreen.window_height()/2 or turtle.ycor() <= -1*TurtleScreen.window_height()/2:
    turtle.left(180)  
 
def Left():
 turtle.left(45)
 
def Right():
   turtle.right(45)
   
TurtleScreen.onkey(Forward, "Up")
TurtleScreen.onkey(Left, "Left")
TurtleScreen.onkey(Right, "Right")

TurtleScreen.listen()
TurtleScreen.mainloop()
