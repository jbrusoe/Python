#Circle Class Demo with Python
#Written by: Jeff Brusoe
#Last Updated: September 11, 2019

import math

class Circle:

    #initializer
    def __init__(self, radius = 5):
        self.__radius = radius

    def getRadius(self):
        #print("Circle radius: " + str(self.radius))
        return self.__radius

    def setRadius(self,radius):
        #To do: Add code to verify radius is a number greater than 0
        
        if radius > 0:
            print("Setting radius to " + str(radius))
            self.__radius = radius
        else:
            print("Radius: " + str(radius))
            print("Radius is less than zero. Unable to change.")

    def getCircumference(self):
        return 2*math.pi*self.__radius
            


