#This filet tests out the constuctor and methods of the circle class.

import Circle

Circle1 = Circle.Circle(5)
print("Circle Radius: " + str(Circle1.getRadius()))

Circle1.setRadius(10)
print("Circle New Radius: " + str(Circle1.getRadius()))

Circle1.setRadius(1)
print("Circle New Radius: " + str(Circle1.getRadius()))

print("Circle Circumference: " + str(Circle1.getCircumference()))

print("Circle 1 Radius - Access via non-hidden variable")
print("Circle1 Radius: " + str(Circle1.__radius))
