import pygame,sys
import pygame.transform
from pygame.locals import *

pygame.init()

SURFACE = pygame.display.set_mode((500,400))
 
pygame.display.set_caption('Hello, World!')

# Aqua      = (0, 255, 255)
BLACK     = (0, 0, 0)
#BLUE      = (0, 0, 255)
# Fuchsia   = (255, 0,255)
# Gray      = (128, 128, 128)
GREEN     = (0, 255, 0)
# Lime      = (0, 255, 0)
# Maroon    = (128, 0, 0)
# Navy Blue = (0, 0, 128)
# Olive     = (128, 128, 0)
# Purple    = (128, 0, 128)
#RED       = (255, 0, 0)
# Silver    = (192, 192, 192)
# Teal      = (0, 128, 128)
# White     = (255, 255, 255)
RED       = (255, 0, 0)
YELLOW    = (255, 255, 0)


#spamRect = pygame.Rect((10,20,200,300))
#pygame.draw.polygon(DISPLAYSURF,GREEN, ((146,0),(291,106),(236,277),(56,277),(0,106)))
#pygame.draw.line(DISPLAYSURF,BLUE,(60,60),(120,60),4)
#pygame.draw.circle(DISPLAYSURF,RED,(300,50),20,0)
#pygame.draw.ellipse(DISPLAYSURF,RED,(300,250,40,80),1)
#pygame.draw.rect(DISPLAYSURF,RED,(200,150,100,50))

cat = pygame.image.load("cat.png")
#cat2 = pygame.transform.scale(cat,(50,50))
x_cat = 100
y_cat = 100
#SURFACE.blit(cat2,(50,50))


#font = pygame.font.Font("freesansbold.ttf",32)
#textSurface = font.render("Hello, World!",True, GREEN,BLUE)
#textRect = textSurface.get_rect()
#textRect.center = (200, 150)

#DISPLAYSURF.blit(textSurface,textRect)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x_cat = x_cat + 20
            if event.key == K_LEFT:
                x_cat = x_cat - 20
                #pygame.draw.line(SURFACE,GREEN,(300,300),(400,400),10)
    SURFACE.fill(BLACK)
    pygame.draw.line(SURFACE,YELLOW,(100,200),(300,200),5)
    pygame.draw.line(SURFACE,RED,(250,100),(250,300),5)
    pygame.draw.circle(SURFACE,YELLOW,(250,200),30)

    SURFACE.blit(cat,(x_cat,y_cat))
    pygame.display.update()

    #DISPLAYSURF.blit(anotherSurface,(0,0))
    #DISPLAYSURF.fill(YellowTransparent)

