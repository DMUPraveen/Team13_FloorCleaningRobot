from Simulation_Platform.Simulation import Grid,Robot
from Simulation_Platform.HelperFunctions import Dijkstar,DijkstarNode
from Simulation_Platform.Main import distanceFunction,replay,distanceAvoidCleaned
from Simulation_Platform.ExampleGrids import JanakSirsExampleGrid

def HuggingTheWallsInternal(gridmaker,startX :int,startY:int,startOrientation:int,direction = 1):
    grid = gridmaker()
    def Endfunction(Node :DijkstarNode ):
        return grid.GetStateofId(Node.id) == Grid.states["FREE"]
    robo = Robot(grid,startX,startY,startOrientation)
    pathFinder = Dijkstar()
    if(direction == 1):
        first = "Left"
        second = "Right"
    else:
        first = "Right"
        second = "Left"

    while True:
        
        if(robo.getNeighbourSquareREL(first) == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL(first)
            
        elif(robo.getNeighbourSquareREL("Forward") == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Forward')

        elif(robo.getNeighbourSquareREL(second) == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL(second)
        
        elif(robo.getNeighbourSquareREL('Back') == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Back')

        else:
            path = pathFinder.Run(
                grid.Id(robo.X,robo.Y),
                robo.orientation,
                Endfunction,
                grid,
                distanceFunction
            )
            if(len(path) == 0):
                break
            robo.followPath(path)
    '''
    replay(
        gridmaker(),
        robo.moves,
        startX,
        startY,
        startOrientation
    )
    '''
    return (
    (robo.time),
    (robo.moves)
    )
        


def HuggingTheWallsAvoidCleanedInternal(gridmaker,startX :int,startY:int,startOrientation:int,direction = 1):
    grid = gridmaker()
    def Endfunction(Node :DijkstarNode ):
        return grid.GetStateofId(Node.id) == Grid.states["FREE"]
    robo = Robot(grid,startX,startY,startOrientation)
    pathFinder = Dijkstar()
    if(direction == 1):
        first = "Left"
        second = "Right"
    else:
        first = "Right"
        second = "Left"

    while True:
        
        if(robo.getNeighbourSquareREL(first) == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL(first)
            
        elif(robo.getNeighbourSquareREL("Forward") == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Forward')

        elif(robo.getNeighbourSquareREL(second) == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL(second)
        
        elif(robo.getNeighbourSquareREL('Back') == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Back')

        else:
            path = pathFinder.Run(
                grid.Id(robo.X,robo.Y),
                robo.orientation,
                Endfunction,
                grid,
                distanceAvoidCleaned,
                (0,0)
            )
            if(len(path) == 0):
                break
            robo.followPath(path)
    '''
    replay(
        gridmaker(),
        robo.moves,
        startX,
        startY,
        startOrientation
    )
    '''
    return (
    (robo.time),
    (robo.moves)
    )
  

def HuggingTheWalls(gridmaker,startX :int,startY:int,startOrientation:int):
    return min(
        (HuggingTheWallsInternal(gridmaker,startX,startY,startOrientation,1),
        HuggingTheWallsInternal(gridmaker,startX,startY,startOrientation,-1)),
        key = lambda x : x[0]
    )

def HuggingTheWallsAvoidCleaned(gridmaker,startX :int,startY:int,startOrientation:int):
    return min(
        (HuggingTheWallsAvoidCleanedInternal(gridmaker,startX,startY,startOrientation,1),
        HuggingTheWallsAvoidCleanedInternal(gridmaker,startX,startY,startOrientation,-1)),
        key = lambda x : x[0]
    )

if __name__ == "__main__":
    print(HuggingTheWalls(
        JanakSirsExampleGrid,
        2,
        9,
        0
    ))
    print(HuggingTheWallsAvoidCleaned(
        JanakSirsExampleGrid,
        2,
        9,
        0
    ))

    