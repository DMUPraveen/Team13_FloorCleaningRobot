from HuggingTheWalls import HuggingTheWalls,HuggingTheWallsAvoidCleaned
from RepeatedDijkstart import RepeatedDijkstart,RepeatedDijkstartAvoidCleaned
from Simulation_Platform.ExampleGrids import JanakSirsExampleGrid

algorithms = {
    "HuggingTheWalls" : HuggingTheWalls,
    "HuggingTheWallsAvoidCleaned" :HuggingTheWallsAvoidCleaned,
    "RepeatedDijkstart":RepeatedDijkstart,
    "RepeatedDijkstartAvoidCleaned":RepeatedDijkstartAvoidCleaned

}




def TestWithExampleGrid():
    times = []
    for algorithmName in algorithms:
        algorithm = algorithms[algorithmName]
        time,solution = algorithm(
            JanakSirsExampleGrid(),
            2,
            9,
            0
        )
        print(algorithmName," : ",time)
        print(solution)
        times.append((algorithmName,time))
    
    times.sort(key = lambda x :x[1])
    for time in times:
        name,t = time
        print(f"{name} : {t}")
        



if __name__ == "__main__":
    TestWithExampleGrid()