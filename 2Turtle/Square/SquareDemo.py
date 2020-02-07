import turtle

SideLength = int(input("Enter the side length: "))

turtle.showturtle()

turtle.up()
turtle.goto(-SideLength/2,-SideLength/2)
turtle.down()
turtle.width(5)

Count = 1

while Count < 5:
    print(Count)

    if Count%2 == 1:
        turtle.color("green")
    else:
        turtle.color("red")
        
    turtle.forward(SideLength)
    turtle.left(90)

    Count = Count +1
    

turtle.hideturtle()
