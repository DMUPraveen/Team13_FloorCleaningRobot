from .Simulation import Grid
JanakaSirsExmpleGridArray = [
    0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
    1, 0, 1, 0, 0, 0, 1, 0, 0, 1,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    1, 0, 0, 0, 0, 1, 1, 1, 1, 0,
    1, 0, 0, 0, 0, 0, 1, 0, 0, 1,
    0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
    0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
    1, 1, 0, 0, 0, 0, 0, 0, 0, 0,

]

JanakSirsExampleGrid = lambda :Grid(10,10,JanakaSirsExmpleGridArray)
