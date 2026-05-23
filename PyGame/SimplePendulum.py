import pygame
import math
#Pendulum Working
pygame.init()

# fps, Amplitude A, Time Period T, display Resolution may be altered
fps = 144 
A = 400.0
T = 1.0
resolution = (1280,720)

def plotGrid(res,gap):
    hor = res[0]
    ver = res[1]
    cenHor = (int)(hor/2)
    cenVer = (int)(ver/2)
    colorBold = (150,150,150)
    colorFaint = (100,100,100)
    pygame.draw.line(win, colorBold, (cenHor,0), (cenHor,ver), 2) #Y-Axis
    for i in range (cenHor+gap,hor,gap):
        pygame.draw.line(win, colorFaint, (i,0), (i,ver), 1)
        pygame.draw.line(win, colorFaint, (hor-i,0), (hor-i,ver), 1)
    pygame.draw.line(win, colorBold, (0,cenVer), (hor,cenVer), 2) #X-Axis
    for j in range (cenVer+gap,ver,gap):
        pygame.draw.line(win, colorFaint, (0,j), (1280,j), 1)
        pygame.draw.line(win, colorFaint, (0,ver-j), (hor,ver-j), 1)
    #pygame.display.update()

font = pygame.font.Font(None,36)
win = pygame.display.set_mode(resolution)
pygame.display.set_caption("Pendulum")
run = True
frameDelay = int(1000/fps)
time = 0.0

bobx = resolution[0]/2
boby = (resolution[1]*0.85)

centerX = resolution[0]/2
centerY = (resolution[1]*0.15)

r = (resolution[1]*0.7)
rSquared = r*r

omega = (2*math.pi)/T
while run:
    pygame.time.delay(frameDelay)
    bobx = (resolution[0]/2)+(A*math.sin(omega*time))
    boby = centerY + math.sqrt(rSquared-(centerX-bobx)**2)
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
    plotGrid(resolution,100)
    text1 = font.render("Time Elapsed :               "+timetext, True, (255,255,255))
    win.blit(text1,(20,20))
    text2 = font.render("No. of Oscillations :      "+nOsc, True, (255,255,255))
    win.blit(text2,(20,56))
    pygame.draw.circle(win, (255,255,255), (centerX,centerY), 10)
    pygame.draw.circle(win, (55,55,55), (centerX,centerY), 5)
    pygame.draw.circle(win, (255,255,255), (bobx,boby), 25)
    pygame.draw.line(win, (100,100,100), (centerX,centerY), (bobx,boby), 2)
    pygame.display.update() 
    
pygame.quit()
