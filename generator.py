import random
from solver import Solver
from colors import Color


class Generator:
    def __init__(self):
        self.size = 9
        self.square = 3
        self.blank = 0
        self.grid = [[self.blank] * self.size for _ in range(self.size)]

    def generate_board(self, difficulty='hard'):
        if difficulty == 'easy':
            blanks = random.randint(17, 32)
        elif difficulty == 'medium':
            blanks = random.randint(33, 48)
        else:  # difficulty = 'hard'
            blanks = random.randint(49, 64)

        self.fill_diagonal()
        self.fill_board(0, self.square)
        self.remove_clues(blanks)

    def is_valid_row(self, row, num):
        for i in range(self.size):
            if self.grid[row][i] == num:
                return False
        return True

    def is_valid_col(self, col, num):
        for i in range(self.size):
            if self.grid[i][col] == num:
                return False
        return True

    def is_valid_subgrid(self, row_start, col_start, num):
        for i in range(self.square):
            for j in range(self.square):
                if self.grid[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, i, j, num):
        return (self.is_valid_row(i, num)
                and self.is_valid_col(j, num)
                and self.is_valid_subgrid(i - i % self.square, j - j % self.square, num))

    def random_int(self, num):
        return random.randint(1, num)

    def fill_diagonal(self):
        for i in range(0, self.size, self.square):
            self.fill_subgrid(i, i)

    def fill_subgrid(self, row, col):
        for i in range(self.square):
            for j in range(self.square):
                while True:
                    num = self.random_int(self.size)
                    if self.is_valid_subgrid(row, col, num):
                        break
                self.grid[row + i][col + j] = num

    def fill_board(self, i, j):
        if i == self.size - 1 and j == self.size:
            return True
        if j == self.size:
            i += 1
            j = 0
        if self.grid[i][j] != 0:
            return self.fill_board(i, j + 1)
        for num in range(1, self.size + 1):
            if self.is_valid(i, j, num):
                self.grid[i][j] = num
                if self.fill_board(i, j + 1):
                    return True
                self.grid[i][j] = 0
        return False

    def remove_clues(self, blanks):
        while blanks != 0:
            i = self.random_int(self.size) - 1
            j = self.random_int(self.size) - 1
            if self.grid[i][j] != 0:
                blanks -= 1
                self.grid[i][j] = 0
        return

    def print_generated_board(self):
        solver = Solver()
        solver.grid = self.grid
        print(Color.pink + '✩ generated sudoku board:' + Color.reset)
        solver.print_board()
