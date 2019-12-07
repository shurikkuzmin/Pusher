import pygame,sys
import pygame.transform
from pygame.locals import *

pygame.init()
level1=[['*','*','*','*',' ',' ',' '],
	    ['*','T',' ','*','*',' ',' '],
	    ['*','T','H',' ','*',' ',' '],
	    ['*','T',' ','B','*',' ',' '],
	    ['*','*','B',' ','*','*','*'],
	    [' ','*',' ','B',' ',' ','*'],
        [' ','*',' ','T',' ',' ','*'],
	    [' ','*',' ',' ','*','*','*'],
	    [' ','*','*','*','*',' ',' ']]

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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                hero = heroRight
                if level1[yHero][xHero+1] != '*':
                    level1[yHero][xHero] = ' '
                    xHero = xHero + 1
                    level1[yHero][xHero] = 'H'
                
            if event.key == K_LEFT:
                hero = heroLeft
                if level1[yHero][xHero-1] != '*':
                    level1[yHero][xHero] = ' '
                    xHero = xHero - 1
                    level1[yHero][xHero] = 'H'
                    
            if event.key == K_UP:
                hero = heroUp
                if level1[yHero-1][xHero] != '*':
                    level1[yHero][xHero] = ' '
                    yHero = yHero - 1
                    level1[yHero][xHero] = 'H'
                
            if event.key == K_DOWN:
                hero = heroDown
                if level1[yHero+1][xHero] != '*':
                    if level1[yHero+1][xHero] == "B":
                        if level1[yHero+2][xHero] == "T":
                            level1[yHero+2][xHero] = "G"
                        elif level1[yHero+2][xHero] == " ":
                            level1[yHero+2][xHero] = 'B'
                        elif level1[yHero+2][xHero] == "*":   
                            continue
                    
                    elif level1[yHero+1][xHero] == "G":
                        if level1[yHero+2][xHero] == "*":
                            continue
                        elif level1[yHero+2][xHero] == ' ':
                            level1[yHero+2][xHero] = 'B'
                            level1[yHero+1][xHero] = 'I'
                            
                            
                    # use return move true or false to move the Hero?
                    level1[yHero][xHero] = ' '
                    yHero = yHero + 1
                    level1[yHero][xHero] = 'H'
                    
                    
                    
            
       
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
                
                
            
    
    pygame.display.update()   
