import pygame
import sys

class Cell:
    def __init__(self, value=0, sketch=None, original=False):
        self.value = value
        self.sketch = sketch
        self.original = original

# sets up board for sudoku game to be played on

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]
        self.selected_cell = None

    def draw(self):
        cell_size = 9
        line_width_bold = 3
        line_width_normal = 1
        margin = 10
        
        for i in range(self.width + 1):
            if i % 3 == 0:
                line_width = line_width_bold
            else:
                line_width = line_width_normal

            pygame.draw.line(self.screen, (0, 0, 0), (margin + i * cell_size, margin),
                             (margin + i * cell_size, margin + self.height * cell_size), line_width)

    def select(self, row, col):
        self.selected_cell = (row, col)


    def click(self, x, y):
        cell_size = 9
        margin = 10

        if margin <= x <= margin + self.width * cell_size and margin <= y <= margin + self.height * cell_size:
            row = (x - margin) // cell_size
            col = (y - margin) // cell_size
            return int(row), int(col)
        else:
            return None


    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].value = 0


    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].sketch = value

    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            self.cells[row][col].value = value

    def reset_to_original(self):
        for i in range(self.width):
            for j in range(self.height):
                self.cells[i][j].value = 0

    def is_full(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.cells[i][j].value == 0:
                    return False
        return True

     def update_board(self):
        pass

    def find_empty(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.cells[i][j].value == 0:
                    return i, j
        return None

    def check_board(self):
        pass
