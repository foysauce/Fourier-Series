import pygame, math, sys

pygame.init()

width = 1000.0
height = 800.0

white = (255,255,255)
red = (255,0,0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (20,20,20)

screen = pygame.display.set_mode((width, height))


clock = pygame.time.Clock()

n = 1

FPS = 100

radius = 100*(4/(math.pi*n))

points = [[600, height/2]]

degree = 0

series = 2
#number of series 100 is pretty much a square wave


while True:

    screen.fill(black)
    
    x = width/3
    y = height/2
    

    if pygame.event.get(pygame.QUIT):
        sys.exit()

    for i in range(series):
        n = i*2 + 1
        radius = 100*(4/(math.pi*n))
        prevx = x
        prevy = y
        x += radius*math.cos(n*(math.radians(degree)))
        y += radius*math.sin(n*(math.radians(degree)))
        pygame.draw.circle(screen, white, [prevx,prevy], radius, 1)
    
    pygame.draw.circle(screen, white, [x,y], 5, 5)
    pygame.draw.line(screen, blue, [x,y], [600,y])
    pygame.draw.circle(screen, white, [600,y], 5, 5)
        

    degree += 1
    
    p = [600,y]

    points.append(p)
    for x in range(len(points)):
        points[x][0] = points[x][0] + 1
        
    pygame.draw.lines(screen, white, False, points)

    clock.tick(FPS)
    
    
    
    
    pygame.display.update()