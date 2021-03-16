from Simulation import Grid,Robot
from HelperFunctions import Dijkstar,DijkstarNode
from Main import replay,main,distanceFunction
from ExampleGrids import JanakSirsExampleGrid

def Algorithm(grid :Grid,startX :int,startY:int,startOrientation:int):
    def Endfunction(Node :DijkstarNode ):
        return grid.GetStateofId(id) == Grid.states["FREE"]

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
    main(grid,robo)



if __name__ == "__main__":
    Algorithm(
        JanakSirsExampleGrid(),
        2,
        9,
        0
    )

        