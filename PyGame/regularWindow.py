import pygame # importing pygame
pygame.init() # initialise pygame at first
win = pygame.display.set_mode((1280,720)) # window dimensions
pygame.display.set_caption("First Simulation") # set window title
run = True # flag
fps = 60 # fps to calculate delay
frameDelay = (int)(1000/fps) # delay per frame in milliseconds
while (run): # game loop
    pygame.time.delay(frameDelay) # adding delays. argument is an integer
    for event in pygame.event.get(): # iterating through events during the delay
        if event.type == pygame.QUIT: # checking if QUIT (Close Button)
            run = False # setting up flag
pygame.quit() # actually closing the window
