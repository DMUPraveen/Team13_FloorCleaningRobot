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

def compileTime(moves):
    time = 0
    dic = {
        "SP" : 1,
        "MF" : 1,
        "TR" : 2,
        "TL" : 2,
    }
    for move in moves:
        time += dic[move]

    return time
        

def replay(grid,robocommands,startX,startY,startOrientation,):
    replaySpeed = 0.02
    
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
                #print(robo.time)
                return
        

        Graphics.draw()
        
        pygame.display.update()
        Graphics.clear()
        if(time() -t > replaySpeed and len(commands)!=0):

            robo.play(commands.pop(0))
            t = time()

def replayR(grid,robocommands,startX,startY,startOrientation,):
    replaySpeed = 0.02
    
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
    start = False
    while True:
        
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
                #print(robo.time)
                return
            if(event.type == KEYDOWN):
                if(event.key == K_SPACE):
                    start = True
        

        Graphics.draw()
        
        pygame.display.update()
        Graphics.clear()
        if(time() -t > replaySpeed and len(commands)!=0 and start):

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

def CompileSolution(path):
    return "->".join(path)


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


def VisualGridMaker(rows,columns,gridArray=None):
    if(gridArray == None):
        gridArray = [Grid.states["FREE"]]*(rows*columns)
    if(len(gridArray) != rows*columns):
        raise Exception("provided array doesn't have the correct dimentsion")
    grid = Grid(
        rows,
        columns,
        gridArray
    )
    pygame.init()

    robo = Robot(grid,0,0,0)
    grid.setstate(0,0,"FREE")
    cellSize = 30
    width = grid.columns*cellSize
    height = grid.rows*cellSize
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Floor Cleaner")
    Graphics = GFX(window,width,height,grid,robo,cellSize)
    Running = True
    while True:
        
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
                Running = False
                break
            if(event.type == MOUSEBUTTONDOWN):
                if(event.button == 1):
                    mouseX,mouseY = event.pos
                    cellX,cellY = (mouseX//cellSize,mouseY//cellSize)
                    if(cellX != robo.X or cellY != robo.Y):
                        
                        
                        if(grid.getTileState(cellX,cellY) == grid.states["FREE"]):
                            grid.setstate(cellX,cellY,"BLOCKED")
                        elif(grid.getTileState(cellX,cellY) == grid.states["BLOCKED"]):
                            grid.setstate(cellX,cellY,"FREE")
                if(event.button == 3):
                    mouseX,mouseY = event.pos
                    cellX,cellY = (mouseX//cellSize,mouseY//cellSize)
                    if(grid.getTileState(cellX,cellY) == grid.states["FREE"]):
                            robo.X,robo.Y = cellX,cellY

            if(event.type == KEYDOWN):
                if(event.key == K_w):
                    robo.orientation = robo.Directions["N"]
                elif(event.key == K_d):
                    robo.orientation = robo.Directions["E"]
                elif(event.key == K_s):
                    robo.orientation = robo.Directions["S"]
                elif(event.key == K_a):
                    robo.orientation = robo.Directions["W"]               


        if(not Running):
            break

        Graphics.draw()
        
        pygame.display.update()
        Graphics.clear()


    def gridMaker():
        return Grid(rows,columns,[tile for tile in grid.array])
        
    return (gridMaker,robo.X,robo.Y,robo.orientation)




if __name__ == "__main__":

    lis = testDijkStart(JanakSirsExampleGrid(),2,9)
    grid = JanakSirsExampleGrid()
    robo = Robot(grid,2,9)
    print(robo.followPath(lis))
    replay(JanakSirsExampleGrid(),robo.moves,2,9,0)