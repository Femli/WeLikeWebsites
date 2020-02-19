import pygame
import sys

### infinite program
pygame.init()

white = (0,0,0)

### define our window perimiter
width = 800
height = 400

### creating our screen
screen = pygame.display.set_mode((width, height))


#sprite coordinates
pos_x = 400
pos_y = 200


### start game
while True:
    circle = False
    ### code shut down button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                circle = True
            elif event.key == pygame.K_w:
                pos_y = pos_y - 10
            elif event.key == pygame.K_a:
                pos_x = pos_y - 10

            elif event.key == pygame.K_s:
                pos_x = pos_y - 10

            elif event.key == pygame.K_d:
                pos_x = pos_y - 10

    # pygame.draw.lines(screen, white, False, [(0,0), (800, 400)], 5)
    # pygame.draw.lines(screen, white, False, [(400,0), (0, 800)], 5)


    ### draw a circle in the center
    if circle:
        pygame.draw.circle(screen, white, (400, 200), 100, 5)

### draw a rectangle sprite
    pygame.draw.rect(screen, white, (pos_x, pos_y, 10, 10), 5)

    pygame.display.update()
