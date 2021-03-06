

from Simulation_Platform.Simulation import Grid,Robot
from Simulation_Platform.HelperFunctions import Dijkstar,DijkstarNode
from Simulation_Platform.Main import distanceFunction,replay,distanceAvoidCleaned
from Simulation_Platform.ExampleGrids import JanakSirsExampleGrid


def roboConditionaBreak(grid,robot,Id):
    if(grid.Id(robot.X,robot.Y) == Id):
        print("Breaking")

def RepeatedDijkstart(gridmaker,startX :int,startY:int,startOrientation:int):
    '''
    Goes to the nearest unclean tile
    '''
    grid = gridmaker()
    def Endfunction(Node :DijkstarNode ):
        return grid.GetStateofId(Node.id) == Grid.states["FREE"]

    robo = Robot(grid,startX,startY,startOrientation)
    pathFinder = Dijkstar()
    while True:
        
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

def RepeatedDijkstartAvoidCleaned(gridmaker,startX :int,startY:int,startOrientation:int):
    '''
    Goes to the nearest unclean tile
    '''
    grid = gridmaker()
    def Endfunction(Node :DijkstarNode ):
        return grid.GetStateofId(Node.id) == Grid.states["FREE"]

    robo = Robot(grid,startX,startY,startOrientation)
    pathFinder = Dijkstar()
    while True:
        
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


if __name__ == "__main__":
    RepeatedDijkstart(
        JanakSirsExampleGrid,
        2,
        9,
        0
    )
    RepeatedDijkstartAvoidCleaned(
        JanakSirsExampleGrid,
        2,
        9,
        0
    )

        