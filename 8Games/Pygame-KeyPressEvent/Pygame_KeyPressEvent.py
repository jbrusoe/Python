import pygame

pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame Event Demonstration")
clock = pygame.time.Clock()

x=50
y=50
Radius = 50
Velocity = 5

CanContinue = True

while CanContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CanContinue = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()

