import turtle

Centerx,Centery = eval(input("Enter center of rectangle: "))

print("Centerx:",Centerx)
print("Centery:",Centery)

Width = eval(input("Enter rectangle width:"))
Height = eval(input("Enter rectangle height:"))

turtle.showturtle()

turtle.penup()
turtle.goto(Centerx - (Width/2),Centery-(Height/2))
turtle.pendown()

for i in range (1,3):
    turtle.forward(Width)
    turtle.left(90)
    turtle.forward(Height)
    turtle.left(90)
