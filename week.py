import pygame
import sys

pygame.init()

width = 500
height = 500
posx = 350
posy = 350

screen = pygame.display.set_mode((width, height))


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 0, 255)
blue = (0, 0, 255)
purple = (255, 0, 255)
yellow = (0, 255, 255)

moveup = False
movedown = False
moveleft = False
moveright = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveup = True
                movedown = moveright = moveleft = False

            if event.key == pygame.K_s:
                movedown = True
                moveup = moveleft = moveright = False

            if event.key == pygame.K_a:
                moveleft = True
                moveup = moveright = movedown = False

            if event.key == pygame.K_d:
                moveright = True
                moveleft = moveup = movedown = False

    if moveup and posy > 0:
        posy -= 10
    if movedown and posy < 490:
        posy += 10
    if moveleft and posx > 0:
        posx -= 10
    if moveright and posx < 490:
        posx += 10


    screen.fill(purple)
    pygame.draw.rect(screen, white, (posx, posy, 10, 10), 0)
    myfont = pygame.font.Font(None, 30)
    textsurface = myfont.render('{}, {}'.format(posx, posy), True, green)
    screen.blit(textsurface, (250, 250))
    pygame.display.update()
