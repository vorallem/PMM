import pygame
import math
#Pendulum Working
pygame.init()

# fps, Amplitude A, Time Period T, display Resolution may be altered
fps = 144
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

def plotText(str1, str2, offset):
    text1 = font.render(str1, True, (55,155,255))
    win.blit(text1,(36,offset*36))
    text2 = font.render(" : "+str2, True, (55,255,155))
    win.blit(text2,(360,offset*36))

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

g = 9.80665
omega = (2*math.pi)/T
L = (resolution[1]*0.7)
LSquared = L*L
theta = (math.pi/6.0)
alpha = 0.0
omega = 0.0
nOsc = 0
while run:
    alpha = (-1.0)*(g/L)*(math.sin(theta))*(1.0/1000.0)
    omega += alpha
    if ((((theta+omega)//theta)==-1)or(theta//(theta+(omega))==-1)):
        nOsc+=1
    theta += omega
    bobx = centerX + L*math.sin(theta)
    boby = centerY + L*math.cos(theta)
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                run = False
    time += 1
    if not(time%frameDelay==0):
        continue
                
    win.fill((0,0,0))
    
    timetext = str(time/1000)
    nOscStr = str(nOsc//2)
    plotGrid(resolution,100)

    plotText("Time Elapsed",timetext,1)
    plotText("No. of Oscillations",nOscStr,2)
    plotText("Alpha",str(alpha)[:5:],3)
    plotText("Omega",str(omega)[:7:],4)
    plotText("Theta(radians)",str(theta)[:5:],5)
    plotText("Theta(degrees)",str((int)(theta*180/math.pi)),6)
    pygame.draw.circle(win, (255,255,255), (centerX,centerY), 10)
    pygame.draw.circle(win, (55,55,55), (centerX,centerY), 5)
    pygame.draw.circle(win, (255,255,255), (bobx,boby), 25)
    pygame.draw.line(win, (100,100,100), (centerX,centerY), (bobx,boby), 2)
    pygame.display.update() 
    
pygame.quit()
