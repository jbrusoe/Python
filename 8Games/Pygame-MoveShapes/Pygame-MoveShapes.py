#Pygame demo to move a circle on the screen
#Written by: Jeff Brusoe
#Last Updated: January 28, 2020
#
#https://www.pygame.org/docs/ref/draw.html

import pygame
import math

#Program initialization
pygame.init()

win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Bouncing Circle")
clock = pygame.time.Clock()

#Circle Paramters
Circlex = 100
Deltax = 5
Circley = 300
Deltay = 1
Radius = 50

CanContinue = True

while CanContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CanContinue = False

    win.fill((0,0,0))
    pygame.draw.circle(win,(0,255,0),(Circlex,Circley),Radius)

    Circlex += Deltax
    Circley += Deltay

    if (Circlex + Radius) > 600 or (Circlex -Radius) < 0:
        Deltax = Deltax * (-1)

    if (Circley + Radius) > 600 or (Circley -Radius) < 0:
        Deltay = Deltay * (-1)

    pygame.display.update()
    clock.tick(60)

pygame.quit()



