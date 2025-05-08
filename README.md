# Sudoku Solver

### Project description

This project implements a Sudoku solver using artificial intelligence techniques. The goal is to solve the classic 9x9 Sudoku puzzle quickly and reliably, ensuring that the algorithm always terminates and provides the correct solution.

### Game rules

The objective of Sudoku is to fill a 9x9 grid with digits 1-9 such that each column, each row, and each of the nine 3x3 subgrids (also called blocks) contains all the digits from 1 to 9. The puzzle starts with some cells already filled with numbers, and the player needs to fill in the rest according to the rules.

### Solution approach

The Sudoku puzzle is modeled as a Constraint Satisfaction Problem (CSP) where:
- Variables: Each cell in the 9x9 grid (81 variables total)
- Domains: Each variable can take a value from 1 to 9
- Constraints:
  - Each row must contain all digits from 1 to 9
  - Each column must contain all digits from 1 to 9
  - Each 3x3 block must contain all digits from 1 to 9

The implementation combines constraint-based modeling with backtracking search to find solutions quickly (typically in milliseconds) while guaranteeing correctness for any valid Sudoku grid.

### Implementation

The solution consists of two main classes:
1) Generator - Creates Sudoku puzzles with varying difficulty levels;
2) Solver - Implements the CSP solution with backtracking.

#### Generator
The generator works by first filling diagonal 3x3 blocks (which don't conflict with each other), then recursively filling the rest of the grid using backtracking to ensure a valid solution exists.

#### Solver
The solver uses backtracking to find the correct solution by:
1. Finding an empty cell
2. Trying to place digits 1-9 in the cell
3. Checking if the placement satisfies all constraints
4. If valid, recursively attempting to fill the next empty cell
5. If not valid or no solution is found with that digit, backtracking and trying another digit

### Future development

Potential improvements for the project include:
1. Algorithm optimization for more efficient solving and generation;
2. Creating a graphical user interface (possibly using PyGame);
3. Supporting different grid sizes (4x4, 16x16);
4. Implementing additional Sudoku variants.