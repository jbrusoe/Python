#Python Turtle Demo - Olympic Rings
#Written by: Jeff Brusoe (jbrusoe@gmail.com)

import turtle

turtle.showturtle()

turtle.width(7)

#Draw the rings
turtle.up()
turtle.goto(-100,0)
turtle.down()
turtle.color("blue")
turtle.circle(75)

turtle.up()
turtle.goto(0,0)
turtle.down()
turtle.color("black")
turtle.circle(75)

turtle.up()
turtle.goto(100,0)
turtle.down()
turtle.color("red")
turtle.circle(75)

turtle.up()
turtle.goto(-50,-75)
turtle.down()
turtle.color("yellow")
turtle.circle(75)

turtle.up()
turtle.goto(50,-75)
turtle.down()
turtle.color("green")
turtle.circle(75)

turtle.hideturtle()
