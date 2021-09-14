import pygame
import time
import random

running = True

points = []
color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
black = (0,0,0)
bounceloss= 1
ygravity = 0.5
xgravity = 0

pygame.display.init()
pygame.display.set_caption("Physics Test")

screen = pygame.display.set_mode((800,600))

image = pygame.image.load('C:\\Users\\Leo\\Pictures\\ball.png').convert_alpha()

screenw, screenh = pygame.display.get_surface().get_size()

class point:
    def __init__(self, x, y, ox, oy):
        self.curx = x
        self.cury = y
        self.oldx = ox
        self.oldy = oy

p1 = point(1,1,0,0)
p2 = point(500,700,490,680)
points.append(p1)
points.append(p2)

for i in range(50):
    x = random.randint(50,750)
    y = random.randint(30,100)
    oxd = random.randint(1, 20)
    oyd = random.randint(1,25)
    p3 = point(x,y,x-oxd,y-oyd)
    points.append(p3)

def update():
    updatePoints()
    renderPoints()

def updatePoints():
    for i in range(len(points)):
        vx = points[i].curx - points[i].oldx        #set x velocity
        vy = points[i].cury - points[i].oldy        #set y velocity
        points[i].oldx = points[i].curx             #update oldx
        points[i].oldy = points[i].cury             #update oldy
        points[i].curx += vx                        #update new x position
        points[i].cury += vy                        #update new y position
        points[i].curx += xgravity
        points[i].cury += ygravity
        if points[i].curx > screenw:                #check if point out of bounds width
            points[i].curx = screenw
            points[i].oldx += vx * bounceloss
        elif points[i].curx < 0:
            points[i].curx = 0
            points[i].oldx += vx * bounceloss
        if points[i].cury > screenh:                #check if point out of bounds height
            points[i].cury = screenh
            points[i].oldy += vy * bounceloss
        elif points[i].cury < 0:
            points[i].cury = 0
            points[i].oldy += vy * bounceloss

def renderPoints():
    for i in range(len(points)):
        #print(points[i].curx, points[i].cury)
        #screen.set_at((int(points[i].curx), int(points[i].cury)), color)
        #screen.set_at((int(points[i].oldx), int(points[i].oldy)), black)
        screen.blit(image, (points[i].curx , points[i].cury))

while running:
    update()
    pygame.display.flip()
    color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
