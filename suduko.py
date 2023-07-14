
from __future__ import annotations


Matrix = list[list[int]]

initial_grid: Matrix = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

def is_safe(grid:Matrix,row:int,column:int,n:int)->bool:

    for i in range(9):
        if grid[row][i] == n or grid[i][column] == n:
            return False
        
    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(column - column % 3) + j] == n:
                return False

    return True

def return_empty_location(grid: Matrix) -> tuple[int, int]| None:
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
            
    return None
            

def sudoko(grid:Matrix) -> Matrix | None:

    if location := return_empty_location(grid):
        row, column = location
    else:
        return grid

    for digit in range(1,10):
        if is_safe(grid, row, column, digit):
            grid[row][column] = digit
        
            if sudoko(grid) is not None:
                return grid
            grid[row][column] = 0
            
    return None

def print_solution(grid:Matrix)->None:
    for row in grid:
        for cell in row:
            print(cell,end=" ")
        print()

        

if __name__ == "__main__":
    sol = sudoko(initial_grid)
    print_solution(sol)
        
