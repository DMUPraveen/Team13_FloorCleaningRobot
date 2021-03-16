from Simulation import Grid,Robot
from HelperFunctions import Dijkstar,DijkstarNode
from Main import main,distanceFunction,replay
from ExampleGrids import JanakSirsExampleGrid


def roboConditionaBreak(grid,robot,Id):
    if(grid.Id(robot.X,robot.Y) == Id):
        print("Breaking")

def Algorithm(grid :Grid,startX :int,startY:int,startOrientation:int):
    def Endfunction(Node :DijkstarNode ):
        return grid.GetStateofId(Node.id) == Grid.states["FREE"]

    robo = Robot(grid,startX,startY,startOrientation)
    pathFinder = Dijkstar()
    while True:
        roboConditionaBreak(grid,robo,18)
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



if __name__ == "__main__":
    Algorithm(
        JanakSirsExampleGrid(),
        2,
        9,
        0
    )

        