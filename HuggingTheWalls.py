from Simulation_Platform.Simulation import Grid,Robot
from Simulation_Platform.HelperFunctions import Dijkstar,DijkstarNode
from Simulation_Platform.Main import distanceFunction,replay,distanceAvoidCleaned
from Simulation_Platform.ExampleGrids import JanakSirsExampleGrid

def Algorithm(grid :Grid,startX :int,startY:int,startOrientation:int):
    def Endfunction(Node :DijkstarNode ):
        return grid.GetStateofId(Node.id) == Grid.states["FREE"]
    robo = Robot(grid,startX,startY,startOrientation)
    pathFinder = Dijkstar()

    while True:
        
        if(robo.getNeighbourSquareREL("Left") == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Left')
            
        elif(robo.getNeighbourSquareREL("Forward") == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Forward')

        elif(robo.getNeighbourSquareREL('Right') == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Right')
        
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
    replay(
        JanakSirsExampleGrid(),
        robo.moves,
        startX,
        startY,
        startOrientation
    )
    print(robo.time)
    print("->".join(robo.moves))
        


def AlgorithmAvoidCleaned(grid :Grid,startX :int,startY:int,startOrientation:int):
    def Endfunction(Node :DijkstarNode ):
        return grid.GetStateofId(Node.id) == Grid.states["FREE"]
    robo = Robot(grid,startX,startY,startOrientation)
    pathFinder = Dijkstar()

    while True:
        
        if(robo.getNeighbourSquareREL("Left") == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Left')
            
        elif(robo.getNeighbourSquareREL("Forward") == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Forward')

        elif(robo.getNeighbourSquareREL('Right') == Grid.states["FREE"]):
            robo.goToNeighboutSquareREL('Right')
        
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
    replay(
        JanakSirsExampleGrid(),
        robo.moves,
        startX,
        startY,
        startOrientation
    )
    print(robo.time)
    print("->".join(robo.moves))
  




if __name__ == "__main__":
    Algorithm(
        JanakSirsExampleGrid(),
        2,
        9,
        0
    )