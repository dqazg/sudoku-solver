import time
from colors import Color


class Solver:
    def __init__(self):
        self.size = 9
        self.square = 3
        self.blank = 0
        self.grid = [[self.blank] * self.size for _ in range(self.size)]
        self.elapsed_time = None

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

    def is_valid(self, row, col, num):
        return (
            self.is_valid_row(row, num)
            and self.is_valid_col(col, num)
            and self.is_valid_subgrid(row - row % 3, col - col % 3, num)
        )

    def find_blank(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == self.blank:
                    return (i, j)
        return None

    def solve_board(self):
        empty_cell = self.find_blank()
        if not empty_cell:
            return True  # Sudoku solved
        row, col = empty_cell
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                print('\n'*22)
                self.print_board()  # Print the updated board
                time.sleep(0.1)  # Pause for visualization
                if self.solve_board():
                    return True
                self.grid[row][col] = 0  # Backtrack
        return False

    def print_board(self):
        for i in range(self.size):
            if i % 3 == 0:
                print(Color.peach + "+---+---+---+---+---+---+---+---+---+" + Color.reset)
            else:
                print(Color.peach + "+" + Color.reset + Color.light_yellow + "---+---+---" +
                      Color.reset + Color.peach + "+" + Color.reset + Color.light_yellow +
                      "---+---+---" + Color.reset + Color.peach + "+" + Color.reset +
                      Color.light_yellow + "---+---+---" + Color.reset + Color.peach + "+" +
                      Color.reset)
            for j in range(self.size):
                if j == 0:
                    print(Color.peach + "|" + Color.reset, end=" ")
                if j % 3 == 2:
                    if self.grid[i][j] == self.blank:  # Blank cells are zeros and light violet
                        print(Color.light_violet + str(self.grid[i][j]) + Color.reset, Color.peach + "|" + Color.reset,
                              end=" ")
                    else:  # Clues are hot pink
                        print(Color.hot_pink + str(self.grid[i][j]) + Color.reset, Color.peach + "|" + Color.reset,
                              end=" ")
                else:
                    if self.grid[i][j] == self.blank:
                        print(Color.light_violet + str(self.grid[i][j]) + Color.reset,
                              Color.light_yellow + "|" + Color.reset, end=" ")
                    else:
                        print(Color.hot_pink + str(self.grid[i][j]) + Color.reset,
                              Color.light_yellow + "|" + Color.reset, end=" ")
            print()
        print(Color.peach + "+---+---+---+---+---+---+---+---+---+" + Color.reset)

    def show_timing(self):
        start_time = time.time()
        self.solve_board()
        end_time = time.time()
        self.elapsed_time = end_time - start_time
        return self.elapsed_time
