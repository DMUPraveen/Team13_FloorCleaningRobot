from Simulation import Grid, Robot
import pygame
from pygame.locals import *


class GFX:
    White = pygame.Color(255, 255, 255)
    Black = pygame.Color(0, 0, 0)
    Blue = pygame.Color(0, 0, 255)
    Gray = pygame.Color(128, 128, 128)
    Red = pygame.Color(255, 0, 0)

    stateColorMap = {
        -1: Red,
        0: White,
        1: Black,
        2: Blue
    }

    def __init__(self, window, windowWidth, windowHeight, grid: Grid, robot: Robot, cellSize):
        self.window = window
        self.width = windowWidth
        self.height = windowHeight
        ########################Read Only#####################
        self.grid = grid
        self.robot = Robot
        self.cellSize = cellSize
        ######################################################
        self.clear()

    def clear(self):
        self.window.fill((255,255,255))

    def drawBox(self, color, X, Y):
        pygame.draw.rect(
            self.window,
            color,
            (X*self.cellSize, Y*self.cellSize, self.cellSize, self.cellSize),
            0
        )
        pygame.draw.rect(
            self.window,
            self.Black,
            (X*self.cellSize, Y*self.cellSize, self.cellSize, self.cellSize),
            1
        )

    def drawGrid(self):
        for x in range(self.grid.columns):
            for y in range(self.grid.rows):
                state = self.grid.getTileState(x,y)
                self.drawBox(self.stateColorMap[state],x,y)
