#Based on - https://www.youtube.com/watch?v=ujOTNg17LjI

import pygame

pygame.init()
GameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame Test")
clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

        pygame.display.update()
        clock.tick(60)

pygame.quit()


