import pygame,sys
from pygame.locals import *
from Simulation import Grid,Robot
from GraphicEngine import GFX
from ExampleGrids import JanakSirsExampleGrid




def main():
    pygame.init()
    grid = JanakSirsExampleGrid
    robot = Robot(grid,0,0)
    cellSize = 30
    width = grid.columns*cellSize
    height = grid.columns*cellSize
    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Floor Cleaner")
    Graphics = GFX(window,width,height,grid,robot,cellSize)
    while True:
        for event in pygame.event.get():
            if(event.type == QUIT):
                pygame.quit()
                sys.exit()
        

        Graphics.drawGrid()
        
        pygame.display.update()
        Graphics.clear()


if __name__ == "__main__":
    main()