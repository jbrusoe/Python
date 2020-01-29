#Pygam function file
#Written by: Jeff Brusoe
#Last Updated: January 28, 2020
#
#This file contains functions that have been useful when I've been testing 
#things out with Pygame.

def SetPosition(x,y,ScreenWidth,ScreenHeight):
    #Returns true if the ball is about to move off screen

    ReturnValue = False

    if x > ScreenWidth-10:
        Newx = 10 #Go to other side of screen
    elif x < 10:
        Newx = ScreenWidth-10
    else:
        Newx=x

    if y > ScreenHeight-10:
        Newy = 10
    elif y < 10:
        Newy = ScreenHeight-10
    else:
        Newy = y

    return (Newx,Newy)
