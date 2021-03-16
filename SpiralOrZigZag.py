from Simulation_Platform.Simulation import Grid,Robot
from Simulation_Platform.Main import replay

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
    replay(Grid(rows,columns),robot.moves,x,y,0)
    return path

    

if __name__ == "__main__":
    print(createZigZagPath(5,5,3,-1))


    