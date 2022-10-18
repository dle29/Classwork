# pygame template
import math

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (131,139,139)
brown = (165, 42, 42)
green = (128, 255, 128)
purple = (128, 0, 128)
blue = (10, 10, 100)
red = (255, 0, 0)
pink = (255, 170, 255)
Dark_Green = (0, 64, 0)
light_blue = (82, 200, 220)
light_yellow = (255, 0, 128)
background = blue
rate = 0.3

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

# Initialize global variables
circle_x_SUN = 200
circle_y_SUN = 200
circle_x_wheel1 = 275
circle_y_wheel2 = 325
circle_x_wheel3 = 375
circle_y_wheel4 = 325


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here        

    #sun
    circle_x_SUN += 5
    amplitude = HEIGHT
    y_offset = (amplitude / 2 + 30)
    circle_y_SUN = -1 * (math.sin(circle_x_SUN / WIDTH * math.pi) * amplitude / 2) + y_offset 

    if circle_x_SUN > WIDTH + 30:
        circle_x_SUN = -30

    # DRAWING
    
    screen.fill(background)  # always the first drawing command

    #sky 
    if circle_x_SUN < 320:
        prevr, prevg, prevb = background
        r, g, b = +0.5 * rate, +0.5 * rate, -10 *rate
        background = (prevr + r, prevg +g, prevb +b)
    if circle_x_SUN > 320:
        prevr, prevg, prevb = background
        r, g, b = -0.5 * rate, -0.5 * rate, +10 *rate
        background = (prevr + r, prevg +g, prevb +b)
    
    
    

    
    pygame.draw.circle(screen, (yellow), (circle_x_SUN, circle_y_SUN), 39)
    pygame.draw.rect(screen, (green), (0,350,640,480))
    pygame.draw.rect(screen, (red), (220,250,200,75))
    pygame.draw.rect(screen, (red), (265,200,100,50))
    pygame.draw.circle (screen, (black), (circle_x_wheel1, circle_y_wheel2), 30)
    pygame.draw.circle (screen, (black), (circle_x_wheel3, circle_y_wheel4), 30)
    pygame.draw.rect(screen, (light_blue), (280,220,40,40))
    pygame.draw.circle(screen, (white), (200, 100), 30)
    pygame.draw.circle(screen, (white), (165, 100), 30)
    pygame.draw.circle(screen, (white), (235, 100), 30)
    pygame.draw.circle(screen, (white), (220, 70), 25)
    pygame.draw.circle(screen, (white), (180, 70), 25)
    pygame.draw.circle(screen, (white), (400, 100), 30)
    pygame.draw.circle(screen, (white), (365, 100), 30)
    pygame.draw.circle(screen, (white), (435, 100), 30)
    pygame.draw.circle(screen, (white), (420, 70), 25)
    pygame.draw.circle(screen, (white), (380, 70), 25)
    pygame.draw.rect(screen,(yellow), (200,410,100,20))
    pygame.draw.rect(screen,(yellow), (65,410,100,20))
    pygame.draw.rect(screen,(yellow), (335,410,100,20))
    pygame.draw.circle(screen,(grey), (75,350), 30)
    pygame.draw.circle(screen,(grey), (80,350), 30)
    pygame.draw.circle(screen,(grey), (85,350), 30)
    pygame.draw.circle(screen,(grey), (90,350), 30)
    pygame.draw.circle(screen,(grey), (95,350), 30)
    pygame.draw.circle(screen,(grey), (105,350), 30)
    pygame.draw.circle(screen,(grey), (115,350), 30)
    pygame.draw.circle(screen,(grey), (95,325), 30)
    pygame.draw.circle(screen,(grey), (105,325), 30)
    pygame.draw.circle(screen,(grey), (80,325), 30)
    pygame.draw.circle(screen,(grey), (95,300), 30)
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
