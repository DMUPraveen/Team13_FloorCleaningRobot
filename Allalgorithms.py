from HuggingTheWalls import HuggingTheWalls,HuggingTheWallsAvoidCleaned
from RepeatedDijkstart import RepeatedDijkstart,RepeatedDijkstartAvoidCleaned
from SpiralOrZigZag import SpiralOrZigZag,SpiralOrZigZagAvoidCleaned
from Simulation_Platform.ExampleGrids import JanakSirsExampleGrid
from Simulation_Platform.Main import CompileSolution,replay,replayR,compileTime

algorithms = {
    "HuggingTheWalls" : HuggingTheWalls,
    "HuggingTheWallsAvoidCleaned" :HuggingTheWallsAvoidCleaned,
    "RepeatedDijkstart":RepeatedDijkstart,
    "RepeatedDijkstartAvoidCleaned":RepeatedDijkstartAvoidCleaned,
    "SpiralOrZigZag" : SpiralOrZigZag,
    "SpiralOrZigZagAvoidCleaned": SpiralOrZigZagAvoidCleaned

}


def superAlgorithm(gridMaker,startX,startY,startOrientation):
    times = []
    for algorithmName in algorithms:
        algorithm = algorithms[algorithmName]
        time,solution = algorithm(
            gridMaker,
            startX,
            startY,
            startOrientation
        )

        times.append((solution,time,algorithmName))
    
    times.sort(key = lambda x :x[1])
    print(f"WinningAlgorithm : {times[0][2]}")
    return times[0][1],times[0][0]
   


def TestAllalgorithms(gridMaker,startX,startY,startOrientation,showAllAlgoithms= True):
    times = []
    for algorithmName in algorithms:
        algorithm = algorithms[algorithmName]
        time,solution = algorithm(
            gridMaker,
            startX,
            startY,
            startOrientation
        )
        print(algorithmName," : ",time)
        print(CompileSolution(solution))
        #print(compileTime(solution))
        times.append((algorithmName,time))
        if(showAllAlgoithms):
            replay(
                gridMaker(),
                solution,
                startX,
                startY,
                startOrientation
            )
    
    times.sort(key = lambda x :x[1])
    for time in times:
        name,t = time
        print(f"{name} : {t}")
        

def main1(gridmaker):
    time,solution = superAlgorithm(
        gridmaker,
        2,
        9,
        0
    )
    print(time)
    replay(
        gridmaker(),
        solution,
        2,
        9,
        0
    )
    print(CompileSolution(solution))

def main2():
    TestAllalgorithms(
        JanakSirsExampleGrid,
        2,
        9,
        0
    )

if __name__ == "__main__":
    

    main2()
