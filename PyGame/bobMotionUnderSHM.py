import pygame
import math

pygame.init()

# fps, Amplitude A, Time Period T, display Resolution may be altered
fps = 60 #framesPerSecondwin
A = 400.0 #pixels
T = 1.0 #seconds
resolution = (1280,720)

font = pygame.font.Font(None,36)
win = pygame.display.set_mode(resolution)
pygame.display.set_caption("SHM")
run = True
frameDelay = int(1000/fps)
time = 0.0
bobx = resolution[0]/2
boby = resolution[1]/2
omega = (2*math.pi)/T
while run:
    pygame.time.delay(frameDelay)
    bobx = (resolution[0]/2)+(A*math.sin(omega*time))
    time += (float)(frameDelay/1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                run = False
                
    win.fill((0,0,0))
    
    timetext = str(time)
    nOsc = str((int)(time//T))
    text1 = font.render("Time Elapsed : "+timetext, True, (255,255,255))
    win.blit(text1,(200,100))
    text2 = font.render("No. of Oscillations : "+nOsc, True, (255,255,255))
    win.blit(text2,(200,136))
    pygame.draw.circle(win, (255,255,255), (bobx,boby), 25)
    pygame.display.update() 
    
pygame.quit()
