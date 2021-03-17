from Allalgorithms import superAlgorithm,TestAllalgorithms
from Simulation_Platform.Main import VisualGridMaker
from SpiralOrZigZag import SpiralOrZigZag
from Simulation_Platform.ExampleGrids import JanakaSirsExmpleGridArray


if __name__ == "__main__":
    rows = int(input("rows :"))
    columns = int(input("columns :"))
    TestAllalgorithms(*VisualGridMaker(rows,columns))
    