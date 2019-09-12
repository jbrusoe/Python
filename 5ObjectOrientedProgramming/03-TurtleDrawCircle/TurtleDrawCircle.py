#Class that draws a circle with Turtle
#Written by: Jeff Brusoe
#Last Updated: September 11, 2019

import turtle

class TurtleDrawCircle:
    def __init__(self,radius,centerX,centerY,color,thickness):
        self.__radius = radius
        self.__centerX = centerX
        self.__centerY = centerY
        self.__color = color
        self.__thickness = thickness

    def GetRadius(self):
        return self.__radius

    def SetRadius(self,radius):
        try:
            #Return true if no error setting radius
            self.__radius = radius
            return True
        except:
            #Error setting radius
            return False

    def GetCenterX(self):
        return self.__centerX

