#Pygame demo to demonstrate keyboard input
#Written by: Jeff Brusoe
#Last Updated: January 28, 2020
#
#https://www.pygame.org/docs/ref/draw.html
#This version prevents the ball from moving off screen.

import pygame
import math
import PygameFunctions

#Program initialization
ScreenWidth = 600
ScreenHeight = 600
pygame.init()

win = pygame.display.set_mode((ScreenWidth,ScreenHeight))
pygame.display.set_caption("Keyboard Input - Version 2")
clock = pygame.time.Clock()

#Circle Paramters
Circlex = 100
Deltax = 5
Circley = 300
Deltay = 5
Radius = 50

CanContinue = True

while CanContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CanContinue = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Circlex += Deltax

    if keys[pygame.K_LEFT]:
        Circlex -= Deltax

    if keys[pygame.K_DOWN]:
        Circley += Deltay

    if keys[pygame.K_UP]:
        Circley -= Deltay

    win.fill((0,0,0))
    #pygame.draw.circle(win,(0,255,0),(Circlex,Circley),Radius)
    Circlex, Circley = PygameFunctions.SetPosition(Circlex,Circley,ScreenWidth,ScreenHeight)
   
    pygame.draw.circle(win,(0,255,0),(Circlex,Circley),Radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()



