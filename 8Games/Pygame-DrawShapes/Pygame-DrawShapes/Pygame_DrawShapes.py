import pygame

#Program initialization
pygame.init()

win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Draw Shapes")
clock = pygame.time.Clock()

#Rectangle Parameters
x = 50
y = 50
width = 40
height = 60

#Circle Paramters
Circlex = 100
Circley = 200
Radius = 50

CanContinue = True

while CanContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CanContinue = False

    pygame.draw.rect(win,(0,0,255),(x,y,width,height))
    pygame.draw.circle(win,(0,255,0),(Circlex,Circley),Radius)
    pygame.draw.ellipse(win,(255,0,0),(4*x,4*4,3*width,5*height))

    pygame.display.update()
    clock.tick(60)

pygame.quit()



