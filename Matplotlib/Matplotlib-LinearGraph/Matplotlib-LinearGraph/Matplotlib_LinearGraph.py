#Matplotlib example to draw a straight line
#Written by: Jeff Brusoe
#Last Updated: March 23, 2019

import matplotlib.pyplot as plt

#Note: Students can add error handling here
slope = int(input("Enter the slope of a line (from -4 to 4): "))
intercept = int(input("Enter the y-intercept: "))

GraphTitle = "Graph of y = " + str(slope) + "x + " + str(intercept)
plt.title(GraphTitle,fontsize = 40)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.grid(True)

x = range(-20,20)

plt.show()




