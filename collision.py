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

circle_blue = False
circle_purple = False
circle_yeller = False
circle_strange = False

while True:
### posx = posx - 10
### posx -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keypressed = pygame.key.get_pressed()
    if keypressed[pygame.K_a] and posx > 100:
        posx -= 10
        circle_purple = True
        circle_blue = False
        circle_yeller = False
        circle_strange = False

    elif keypressed[pygame.K_s] and posy < 400:
        posy += 10
        circle_strange = True
        circle_blue = False
        circle_purple = False
        circle_yeller = False

    elif keypressed[pygame.K_w] and posy > 100:
        posy -= 10
        circle_yeller = True
        circle_blue = False
        circle_purple = False
        circle_strange = False

    elif keypressed[pygame.K_d] and posx < 400:
        posx += 10
        circle_blue = True
        circle_purple = False
        circle_yeller = False
        circle_strange = False

    screen.fill((150,0,0))

    if circle_blue:
        pygame.draw.circle(screen,(0, 255, 255), (posx, posy), 100)


    elif circle_purple:
        pygame.draw.circle(screen,(255, 0, 255), (posx, posy), 100)

    elif circle_yeller:
        pygame.draw.circle(screen,(255, 255, 0), (posx, posy), 100)

    elif circle_strange:
        pygame.draw.circle(screen,(200, 200, 200), (posx, posy), 100)
    ### describing above circle: color, placement, radius
    pygame.display.update()
