#Pygame - Event Demonstration
#Written by: Jeff Brusoe
#Last Updated: January 9, 2020
#
#Program prints out the events that happen in the Pygame window

import pygame

pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame Event Demonstration")
clock = pygame.time.Clock()

CanContinue = True

while CanContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CanContinue = False

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
