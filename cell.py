import pygame
from constants import *

# cell class
class Cell:
    def __init__(self, value, row, col, screen, width, height):
        self.width = width
        self.height = height
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_value = value
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.cell_value = value

    def set_sketched_value(self, value):

        self.sketched_value = value

# draws the main cells of the board
    def draw(self, row, col):
        pygame.draw.rect(self.screen, (155, 155, 155), pygame.Rect(row, col, CELL_WIDTH, CELL_HEIGHT), 2)

        cell_valueFont = pygame.font.Font(None, 30)
        sketch_valueFont = pygame.font.Font(None, 20)

        cell_valueText = str(self.cell_value)

        sketch_valueText = str(self.sketched_value)

        cellSurf = cell_valueFont.render(cell_valueText, 0, CELL_COLOR)
        cellRect = cellSurf.get_rect(center=(row + 26, col + 26))

        cellSketchSurf = sketch_valueFont.render(sketch_valueText, 0, SKETCH_COLOR)
        cellSketchRect = cellSketchSurf.get_rect(center=(row + 15, col + 15))


        if self.cell_value != 0:
            self.screen.blit(cellSurf, cellRect)
        else:
            pass

        if self.sketched_value != 0:
            self.screen.blit(cellSketchSurf, cellSketchRect)
        else:
            pass

# draws the sketch cells for the board
    def draw_sketch(self, row, col):
        pygame.draw.rect(self.screen, (155, 155, 155), pygame.Rect(row, col, CELL_WIDTH, CELL_HEIGHT), 2)

        cell_valueFont = pygame.font.Font(None, 30)
        sketch_valueFont = pygame.font.Font(None, 20)

        cell_valueText = str(self.cell_value)

        sketch_valueText = str(self.sketched_value)

        cellSurf = cell_valueFont.render(cell_valueText, 0, SKETCH_COLOR)
        cellRect = cellSurf.get_rect(center=(row + 26, col + 26))

        cellSketchSurf = sketch_valueFont.render(sketch_valueText, 0, SKETCH_COLOR)
        cellSketchRect = cellSketchSurf.get_rect(center=(row + 15, col + 15))

        if self.cell_value != 0:
            self.screen.blit(cellSurf, cellRect)
        else:
            pass

        if self.sketched_value != 0:
            self.screen.blit(cellSketchSurf, cellSketchRect)
        else:
            pass
