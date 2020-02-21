### ALWAYS IMPORT THESE LIBRARIES
import pygame
import sys

### INITIATING THE PYGAME LIBRARY
pygame.init()

### DIMENSIONS OF YOUR SCREEN
width = 500
height = 500

### CREATING A SCREEN
screen = pygame.display.set_mode((width, height))

### DEFINING THE MAIN COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

### RUN THE GAME PROGRAM WIT A WHILE LOOP
while True:

    ### CAPTURE THE KEYS THAT YOU PRESS
    for event in pygame.event.get():
        ### PRESS THE RED X BOTTON ON THE TOP RIGHT AND PROGRAM WILL QUIT
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white) ### BACKGROUND IS WHITE
    pygame.display.update() ### NEED THIS SO THAT WE CAN SEE SCREEN
