import pygame,sys
from pygame.locals import *
from .Simulation import Grid,Robot
from .GraphicEngine import GFX
from .ExampleGrids import JanakSirsExampleGrid
from time import time

from .HelperFunctions import Dijkstar


def show(grid,robot):
    pygame.init()


    cellSize = 30
    width = grid.columns*cellSize
    height = grid.rows*cellSize
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Floor Cleaner")
    Graphics = GFX(window,width,height,grid,robot,cellSize)
    while True:
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
                return
        

        Graphics.draw()
        
        pygame.display.update()
        Graphics.clear()


def replay(grid,robocommands,startX,startY,startOrientation):
    replaySpeed = 0.01
    
    pygame.init()
    commands = [i for i in robocommands]
    robo = Robot(grid,startX,startY,startOrientation)
    cellSize = 30
    width = grid.columns*cellSize
    height = grid.rows*cellSize
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Floor Cleaner")
    Graphics = GFX(window,width,height,grid,robo,cellSize)
    t = time()
    while True:
        
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
                print(robo.time)
                return
        

        Graphics.draw()
        
        pygame.display.update()
        Graphics.clear()
        if(time() -t > replaySpeed and len(commands)!=0):

            robo.play(commands.pop(0))
            t = time()




def distanceFunction(D,O,tO,state):
    turnFactor = (tO-O)%4
    turns = 0
    if(turnFactor == 0):
        turns = 0
    elif(turnFactor == 2):
        turns = 2
    else:
        turns = 1

    time = Robot.Turnby90Time*(turns)+Robot.MoveForwardTime
    if(state == Grid.states["FREE"]):
        time += Robot.SprayTime
    return D+time



def distanceAvoidCleaned(Distance,Orientation,targetOrientation,state):
    d = distanceFunction(Distance[1],Orientation,targetOrientation,state)
    if(state == Grid.states["FREE"]):
        return (0,d)
    else:
        return (1,d)


def testGetNeighbours():
    grid = JanakSirsExampleGrid()
    #grid.cleanTile(1,0)


    while True:
        x,y,o = int(input("x:")),int(input("y:")),int(input("o:"))
        if(x < 0):
            break
        print(grid.getNeighbours(x,y,o,0,distanceFunction))



def testDijkStart(grid,x,y):
    pathFinder = Dijkstar()

    return pathFinder.Run(
        grid.Id(x,y),0,lambda Node : (Node.id == 1),grid,distanceFunction
    )




if __name__ == "__main__":

    lis = testDijkStart(JanakSirsExampleGrid(),2,9)
    grid = JanakSirsExampleGrid()
    robo = Robot(grid,2,9)
    print(robo.followPath(lis))
    replay(JanakSirsExampleGrid(),robo.moves,2,9,0)