import pygame,sys
import pygame.transform
from pygame.locals import *

pygame.init()

 ########
##      #
#   .   #
#   $   #
# .$@$. #
####$   #
   #.   #
   #   ##
   #####

level1=[[' ','*','*','*','*','*','*','*','*'],
        ['*','*',' ',' ',' ',' ',' ',' ','*'],
        ['*',' ',' ',' ','T',' ',' ',' ','*'],
        ['*',' ',' ',' ','B',' ',' ',' ','*'],
        ['*',' ','T','B','H','B','T',' ','*'],
        ['*','*','*','*','B',' ',' ',' ','*'],
        [' ',' ',' ','*','T',' ',' ',' ','*'],
        [' ',' ',' ','*',' ',' ',' ','*','*'],
        [' ',' ',' ','*','*','*','*','*',' ']]

rowSize = len(level1)
columnSize = len(level1[0])

tileWidth = 64
tileHeight = 64

WINDOWHEIGHT=tileHeight*rowSize
WINDOWLENGTH=tileWidth*columnSize

SURFACE = pygame.display.set_mode((WINDOWLENGTH,WINDOWHEIGHT))
 

pygame.display.set_caption('Hello, World!')

# Aqua      = (0, 255, 255)
BLACK     = (0, 0, 0)
BLUE      = (0, 0, 255)
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
WHITE     = (255, 255, 255)
RED       = (255, 0, 0)
YELLOW    = (255, 255, 0)



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

#Target
targetRect = pygame.Rect((tileWidth,tileHeight,tileWidth,tileHeight))
target = sprite.subsurface(targetRect)

for i in range(rowSize):
    for j in range(columnSize):
        if level1[i][j] == 'H':
            xHero = j
            yHero = i 

#Wall
wallRect = pygame.Rect((tileWidth*2,0,tileWidth,tileHeight))
wall = sprite.subsurface(wallRect)

#Grass
grassRect = pygame.Rect((tileWidth*2,tileHeight,tileWidth,tileHeight))
grass = sprite.subsurface(grassRect)

hero = heroDown

def drawLevel():
    SURFACE.fill(BLACK)
    #Draw the level
    for row in range(rowSize):
        for column in range(columnSize):
            if level1[row][column] == "*":
                SURFACE.blit(wall,(tileWidth*column,row*tileHeight))
            elif level1[row][column] == " ":
                SURFACE.blit(grass,(tileWidth*column,row*tileHeight))
            elif level1[row][column] == "T":
                SURFACE.blit(target,(tileWidth*column,row*tileHeight))    
            elif level1[row][column] == "H":
                SURFACE.blit(grass,(tileWidth*column,row*tileHeight))
                SURFACE.blit(hero,(tileWidth*column,row*tileHeight))
            elif level1[row][column] == "B":
                SURFACE.blit(box,(tileWidth*column,row*tileHeight))
            elif level1[row][column] == "G":
                SURFACE.blit(boxGoal,(tileWidth*column,row*tileHeight))
            elif level1[row][column] == "I":
                SURFACE.blit(target,(tileWidth*column,row*tileHeight)) 
                SURFACE.blit(hero,(tileWidth*column,row*tileHeight))

def checkWin():
    for row in range(rowSize):
        for column in range(columnSize):
            if level1[row][column] == "B":
                return False
    return True

gameOver = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if gameOver == True:
            continue
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero = heroRight
                xNew = xHero+1
                yNew = yHero
                xNew2 = xHero+2
                yNew2 = yHero 
            if event.key == K_LEFT:
                hero = heroLeft
                xNew = xHero - 1
                yNew = yHero
                xNew2 = xHero-2
                yNew2 = yHero
                    
            if event.key == K_UP:
                hero = heroUp
                yNew = yHero - 1
                xNew = xHero
                yNew2 = yHero - 2
                xNew2 = xHero
                 
            if event.key == K_DOWN:
                hero = heroDown
                yNew = yHero + 1
                xNew = xHero
                yNew2 = yHero + 2
                xNew2 = xHero
                
            if level1[yNew][xNew] != '*':
                
                if level1[yHero][xHero] == "H":
                    oldTile = " "
                if level1[yHero][xHero] == "I":
                    oldTile = "T"
                    
                if level1[yNew][xNew] == "B" or level1[yNew][xNew] == "G":
                    if level1[yNew2][xNew2] == "T":                       
                        level1[yNew2][xNew2] = "G"
                    elif level1[yNew2][xNew2] == " ":
                        level1[yNew2][xNew2] = "B"
                    elif level1[yNew2][xNew2] == "*" or level1[yNew2][xNew2]=="B" or level1[yNew2][xNew2]=="G":   
                        continue
                    
                    level1[yHero][xHero] = oldTile
                    if level1[yNew][xNew] == "G":
                        level1[yNew][xNew]="I"
                    if level1[yNew][xNew] == "B":
                        level1[yNew][xNew]  = "H"
                    xHero = xNew
                    yHero = yNew
                elif level1[yNew][xNew] == " " or level1[yNew][xNew] == "T":
                    if level1[yNew][xNew] == " ":
                        level1[yNew][xNew] = "H"
                    elif level1[yNew][xNew] == "T":
                        level1[yNew][xNew] = "I"
                    level1[yHero][xHero] = oldTile 
                    xHero = xNew
                    yHero = yNew
    drawLevel()
    if checkWin() == True:
         basicFont = pygame.font.SysFont(None, 30)
         text = basicFont.render('Game Over!', True, WHITE, BLUE)
         textRect = text.get_rect()
         textRect.centerx = WINDOWLENGTH/2
         textRect.centery = WINDOWHEIGHT/2
         SURFACE.blit(text,textRect)
         gameOver = True
         
                
    pygame.display.update()   
