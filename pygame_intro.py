import pygame,sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400,300))
anotherSurface = DISPLAYSURF.convert_alpha()
 
pygame.display.set_caption('Hello, World!')

# Aqua      = (0, 255, 255)
# Black     = (0, 0, 0)
BLUE      = (0, 0, 255)
# Fuchsia   = (255, 0,255)
# Gray      = (128, 128, 128)
GREEN     = (0, 128, 0)
# Lime      = (0, 255, 0)
# Maroon    = (128, 0, 0)
# Navy Blue = (0, 0, 128)
# Olive     = (128, 128, 0)
# Purple    = (128, 0, 128)
RED       = (255, 0, 0)
# Silver    = (192, 192, 192)
# Teal      = (0, 128, 128)
# White     = (255, 255, 255)
YELLOW    = (255, 255, 0)

spamRect = pygame.Rect((10,20,200,300))
pygame.draw.polygon(DISPLAYSURF,GREEN, ((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.line(DISPLAYSURF,BLUE,(60,60),(120,60),4)
pygame.draw.circle(DISPLAYSURF,RED,(300,50),20,0)
pygame.draw.ellipse(DISPLAYSURF,RED,(300,250,40,80),1)
pygame.draw.rect(DISPLAYSURF,RED,(200,150,100,50))

cat = pygame.image.load("cat.png")

font = pygame.font.Font("freesansbold.ttf",32)
textSurface = font.render("Hello, World!",True, GREEN,BLUE)
textRect = textSurface.get_rect()
textRect.center = (200, 150)

DISPLAYSURF.blit(cat,(20,20))
DISPLAYSURF.blit(textSurface,textRect)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #anotherSurface.blit()
    #anotherSurface.fill(YellowTransparent)
    #DISPLAYSURF.blit(anotherSurface,(0,0))
    #DISPLAYSURF.fill(YellowTransparent)

    pygame.display.update()