import pygame,sys
import pygame.transform
from pygame.locals import *

pygame.init()

WINDOWHEIGHT=400
WINDOWLENGTH=500
SURFACE = pygame.display.set_mode((WINDOWLENGTH,WINDOWHEIGHT))
 
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

tileWidth = 65
tileHeight = 65

# Load main file
sprite = pygame.image.load('sokoban.png')

# Hero
heroRectRight = pygame.Rect((0,tileHeight*2,tileWidth,tileHeight))
heroRight = sprite.subsurface(heroRectRight)
heroRectDown = pygame.Rect((tileWidth,tileHeight*2,tileWidth,tileHeight))
heroDown = sprite.subsurface(heroRectDown)
heroRectUp = pygame.Rect((0,tileHeight*3,tileWidth,tileHeight))
heroUp = sprite.subsurface(heroRectUp)
heroRectLeft = pygame.Rect((tileWidth,tileHeight*3,tileWidth,tileHeight))
heroLeft = sprite.subsurface(heroRectLeft)

#Box
boxRect = pygame.Rect((0,0,tileWidth,tileHeight))
box = sprite.subsurface(boxRect)
boxRectGoal = pygame.Rect((tileWidth,0,tileWidth,tileHeight))
boxGoal = sprite.subsurface(boxRectGoal)

xHero = 100
yHero = 100

#font = pygame.font.Font("freesansbold.ttf",32)
#textSurface = font.render("Hello, World!",True, GREEN,BLUE)
#textRect = textSurface.get_rect()
#textRect.center = (200, 150)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if xHero<=WINDOWHEIGHT-20:
                    xHero = xHero + 20
            if event.key == K_LEFT:
                xHero = xHero - 20
    SURFACE.fill(BLACK)

    # Hero
    SURFACE.blit(heroRight,(xHero,yHero))
    SURFACE.blit(heroDown,(10,10))
    SURFACE.blit(heroLeft,(40,40))
    SURFACE.blit(heroDown,(60,60))
    
    SURFACE.blit(box,(100,100))
    SURFACE.blit(boxGoal,(120,120))
    

    pygame.display.update()

    #DISPLAYSURF.blit(anotherSurface,(0,0))
    #DISPLAYSURF.fill(YellowTransparent)

