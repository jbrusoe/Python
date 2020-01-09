#Based on - https://www.101computing.net/pong-tutorial-using-pygame-getting-started/

import pygame
from paddle import Paddle

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

BLACK = (0,0,0)
WHITE = (255,255,255)

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

CanContinue = True
clock = pygame.time.Clock()
 
while CanContinue:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              CanContinue = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                carryOn=False  
        
        all_sprites_list.update()

        screen.fill(BLACK)

        #Draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
        all_sprites_list.draw(screen)
        pygame.display.update()

        clock.tick(60)
 
pygame.quit()
