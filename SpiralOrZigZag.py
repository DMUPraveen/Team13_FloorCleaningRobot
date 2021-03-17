from Simulation_Platform.Simulation import Grid,Robot
from Simulation_Platform.Main import replay
from Simulation_Platform.HelperFunctions import Dijkstar
from Simulation_Platform.Main import distanceFunction,show,CompileSolution,distanceAvoidCleaned
from Simulation_Platform.ExampleGrids import JanakSirsExampleGrid

def createSpiralPath(columns,rows,startCorner,direction):
    '''
    startCorner should be 0,1,2,3
    0      1

    3      2

    direction is 0 or 1
    1 clockwise
    -1 anticlockwise

    '''
    path = []
    grid = Grid(rows,columns)
    corners= [0, columns-1,rows*columns-1,rows*columns - columns]
    x,y = grid.getXY(corners[startCorner])
    if(direction == 1):
        turnDirection = 'Left'
        startOrientation = [
            Robot.Directions["E"],
            Robot.Directions["S"],
            Robot.Directions["W"],
            Robot.Directions["N"]
            ]

    else:
        turnDirection = 'Right'
        startOrientation = [
            Robot.Directions["S"],
            Robot.Directions["W"],
            Robot.Directions["N"],
            Robot.Directions["E"]
            ]

    
    robot = Robot(grid,x,y,startOrientation[startCorner])
    while(grid.cleanedTiles != grid.UnblockedTiles):
        path.append(grid.Id(robot.X,robot.Y))
        state = robot.getNeighbourSquareREL('Forward')
        if(state == grid.states["FREE"]):
            robot.goToNeighboutSquareREL('Forward')
        else:
        
            state = robot.getNeighbourSquareREL(turnDirection)
            if(state != grid.states["FREE"]):
                break
            robot.goToNeighboutSquareREL(turnDirection)

    path.append(grid.Id(robot.X,robot.Y))
    #replay(Grid(rows,columns),robot.moves,x,y,startOrientation[startCorner])
    return path


def createZigZagPath(columns,rows,startCorner,direction):
    '''
    startCorner should be 0,1,2,3
    0      1

    3      2

    direction is 0 or 1
    1 left-right
    -1 updown

    '''
    path = []
    grid = Grid(rows,columns)
    corners= [0, columns-1,rows*columns-1,rows*columns - columns]
    x,y = grid.getXY(corners[startCorner])

    if(direction == 1):
        shiftDirections = [
            Robot.Directions["S"],
            Robot.Directions["S"],
            Robot.Directions["N"],
            Robot.Directions["N"]
            ]

        startOrientation = [
            (Robot.Directions["E"],Robot.Directions["W"]),
            (Robot.Directions["W"],Robot.Directions["E"]),
            (Robot.Directions["W"],Robot.Directions["E"]),
            (Robot.Directions["E"],Robot.Directions["W"])
            ]

    else:
        shiftDirections = [
            Robot.Directions["E"],
            Robot.Directions["W"],
            Robot.Directions["W"],
            Robot.Directions["E"]
            ]

        startOrientation = [
            (Robot.Directions["S"],Robot.Directions["N"]),
            (Robot.Directions["S"],Robot.Directions["N"]),
            (Robot.Directions["N"],Robot.Directions["S"]),
            (Robot.Directions["N"],Robot.Directions["S"])
            ]

    
    robot = Robot(grid,x,y)
    dirIndex = 0
    dirTuple = startOrientation[startCorner]
    shiftDirection = shiftDirections[startCorner]
    while(grid.cleanedTiles != grid.UnblockedTiles):
        path.append(grid.Id(robot.X,robot.Y))
        state = robot.getNeighbourSquareABS(dirTuple[dirIndex])
        if(state == grid.states["FREE"]):
            robot.goToNeighboutSquareABS(dirTuple[dirIndex])
        else:
        
            state = robot.getNeighbourSquareABS(shiftDirection)
            if(state != grid.states["FREE"]):
                break
            robot.goToNeighboutSquareABS(shiftDirection)
            dirIndex  = (dirIndex+1)%2

    path.append(grid.Id(robot.X,robot.Y))
    #replay(Grid(rows,columns),robot.moves,x,y,0)
    return path



def Follow(grid:Grid,startX,startY,startOrientation,pathFunction):
    gopath = pathFunction(grid.columns,grid.rows)
    pathFinder = Dijkstar()
    robo = Robot(grid,startX,startY,startOrientation)
    while(len(gopath) != 0):
        dest = gopath.pop(0)
        if(grid.GetStateofId(dest) == grid.states["FREE"]):
            destFunction = lambda Node : Node.id == dest
            path = pathFinder.Run(
                grid.Id(robo.X,robo.Y),
                startOrientation,
                destFunction,
                grid,
                distanceFunction
            )
            robo.followPath(path)

    return (robo.time,robo.moves)



def FollowAvoidClean(grid:Grid,startX,startY,startOrientation,pathFunction):
    gopath = pathFunction(grid.columns,grid.rows)
    pathFinder = Dijkstar()
    robo = Robot(grid,startX,startY,startOrientation)
    while(len(gopath) != 0):
        dest = gopath.pop(0)
        if(grid.GetStateofId(dest) == grid.states["FREE"]):
            destFunction = lambda Node : Node.id == dest
            path = pathFinder.Run(
                grid.Id(robo.X,robo.Y),
                startOrientation,
                destFunction,
                grid,
                distanceAvoidCleaned,
                (0,0)

            )
            robo.followPath(path)

    return (robo.time,robo.moves)        

def makePathFunction(function,startCorner,direction):
    return (lambda columns,rows :  function(columns,rows,startCorner,direction) )
            

def SpiralOrZigZag(gridmaker,startX,startY,startOrientation):
    sols = []
    for pathFunction in [createSpiralPath,createZigZagPath]:
        for startCorner in range(0,4):
            for direction in [1,-1]:

                pf = makePathFunction(pathFunction,startCorner,direction)
                time,path = Follow(
                    gridmaker(),
                    startX,
                    startY,
                    startOrientation,
                    pf
                )
                sols.append((time,path))
    sols.sort(key = lambda x : x[0])
    #print([i[0] for i in sols])
    solution = sols.pop(0)
    '''
    replay(
        gridmaker(),
        solution[1],
        startX,
        startY,
        startOrientation
    )
    '''
    return solution

        
def SpiralOrZigZagAvoidCleaned(gridmaker,startX,startY,startOrientation):
    sols = []
    for pathFunction in [createSpiralPath,createZigZagPath]:
        for startCorner in range(0,4):
            for direction in [1,-1]:

                pf = makePathFunction(pathFunction,startCorner,direction)
                time,path = FollowAvoidClean(
                    gridmaker(),
                    startX,
                    startY,
                    startOrientation,
                    pf
                )
                sols.append((time,path))
    sols.sort(key = lambda x : x[0])
    #print([i[0] for i in sols])
    solution = sols.pop(0)
    '''
    replay(
        gridmaker(),
        solution[1],
        startX,
        startY,
        startOrientation
    )
    '''
    return solution
       
    
    


if __name__ == "__main__":
    time,path = SpiralOrZigZagAvoidCleaned(
        JanakSirsExampleGrid,
        2,
        9,
        0
    )
    print(time)
    print(CompileSolution(path))


    