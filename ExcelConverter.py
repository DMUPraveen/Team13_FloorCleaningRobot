from openpyxl import load_workbook

from Allalgorithms import superAlgorithm
from Simulation_Platform.Main import VisualGridMaker
import sys



MoveMap = {
    "MF" : 1,
    "TR" : 2,
    "TL" : 4,
    "SP" : 5

}


def transpileCommands(commands):
    return [MoveMap[command] for command in commands]




def addCommandsAndSave(inputFile,outputFile,commands,column):
    wb = load_workbook(filename=inputFile)
    sheet = wb.active
    for i in range(len(commands)):
        sheet[f"{column}{i+2}"] = commands[i]

    wb.save(filename = outputFile)



def main(fileName):
    rows = int(input("rows: "))
    columns = int(input("columns: "))

    time,commandList = superAlgorithm(*VisualGridMaker(rows,columns))
    print(f"Time taken: {time}")

    commandList = transpileCommands(commandList)
    name = fileName.split(".")[0]
    outputName = f"{name}SolutionTeam13.xlsx"
    addCommandsAndSave(fileName,outputName,commandList,"G")





if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("File name should be provided")
    else:
        main(sys.argv[1])
    