import pygame
import random

# Initialise PyGame module
pygame.init()

# We use a clock to standardise the speed of game
clock = pygame.time.Clock()

## Variables
fps = 60    # Frames Per Second at which the game runs
bg_color = (0,0,0)  # Background Colour
game_run = True
color = (255,255,255)
screen_width = 1280
screen_height = 720
rectangle_length = 60
rectangle_height = 60
rectangle_x = screen_width/2
rectangle_y = screen_height/2
change_x = 5
change_y = 5

# Screen size
screen = pygame.display.set_mode((screen_width, screen_height))

################[ GAME ]################
while game_run:

    ## Code to quit the game
    # From all the events that are happening in the game
    for event in pygame.event.get():
        # If the 'x' button is pressed
        if event.type == pygame.QUIT:
            # Exit the while loop
            game_run = False

    # Draw the background
    screen.fill(bg_color)

    # Move the rectangle
    rectangle_x += change_x
    rectangle_y += change_y

    # Bounce
    if rectangle_y > screen_height - rectangle_height:
        change_y = -1*random.randint(3, 5)
        bg_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if rectangle_x > screen_width - rectangle_length:
        change_x = -1*random.randint(3, 5)
        bg_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if rectangle_x < 0:
        change_x = random.randint(3, 5)
        bg_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if rectangle_y < 0:
        change_y = random.randint(3, 5)
        bg_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # Draw the rectangle
    rectangle = pygame.Rect(rectangle_x, rectangle_y, rectangle_length, rectangle_height)
    pygame.draw.rect(screen, color, rectangle)
    pygame.display.update()
    clock.tick(fps)


