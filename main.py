from generator import Generator
from solver import Solver
from colors import Color


def main():
    print(Color.pink + '✧˖°. welcome to the sudoku solver! ✧˖°. ' + Color.reset)
    print(Color.pink + '♡ choose difficulty level (easy/medium/hard):' + Color.reset)

    difficulty = input().lower()

    while difficulty not in ['easy', 'medium', 'hard']:
        print(Color.apricot + 'invalid difficulty level. please choose from easy, medium, or hard:' + Color.reset)
        difficulty = input().lower()

    print(Color.pink + '↻ generating sudoku board...' + Color.reset)

    # Generate Sudoku board based on chosen difficulty
    generator = Generator()
    generator.generate_board(difficulty)
    generator.print_generated_board()
    sudoku_board = generator.grid

    print(Color.pink + '♡ cool, we have a board! to solve the sudoku press p:' + Color.reset)

    choice = input().lower()

    if choice == 'p':
        # Solve Sudoku
        solver = Solver()
        solver.grid = sudoku_board
        elapsed_time = solver.show_timing()
        if solver.solve_board():
            print(Color.pink + '✩ solved sudoku board:' + Color.reset)
            solver.print_board()
            print(Color.pink + f'⋆ ˚｡⋆୨୧˚ elapsed time: {elapsed_time} seconds ˚୨୧⋆｡˚ ⋆' + Color.reset)
        else:
            print(Color.apricot + 'no solution exists for the provided sudoku board! ˙◠˙' + Color.reset)


if __name__ == "__main__":
    main()
