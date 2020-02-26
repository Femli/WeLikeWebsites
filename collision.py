import pygame
import sys

pygame.init()

### SCREEN DIMENSIONS
width = 500
height = 500


screen = pygame.display.set_mode((width,height))

### coordinates for my shape
posx = 250
posy = 250

while True:
### posx = posx - 10
### posx -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                posx -= 10

    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_a] and posx > 100:
        posx -= 10

    elif keypressed[pygame.K_s] and posy < 400:
        posy += 10

    elif keypressed[pygame.K_w] and posy > 100:
        posy -= 10

    elif keypressed[pygame.K_d] and posx < 400:
        posx += 10


    screen.fill((150,0,0))
    pygame.draw.circle(screen,(0, 255, 255), (posx, posy), 100)
    ### describing above circle: color, placement, radius
    pygame.display.update()
