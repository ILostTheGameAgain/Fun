#minesweeper game, because why not?

#needs import random to randomly place mines
import random

#function for size of grid
def grid_size(size):
    grid = []
    for x in range(size):
        grid.append([])
        for y in range(size):
            grid[x].append(" ")
        
    return grid


#function to display the grid in a good looking way
def display_grid(grid, size):
    grid_display = "\n   "
    for i in range(size):
        if len(str(i+1)) == 1:
            grid_display += f"| {i+1} "
        else:
            grid_display += f"| {i+1}"

    for x in range(size):
        grid_display += "\n"
        for z in range(size):
            grid_display += "---+"

        if len(str(x+1)) == 1:
            grid_display += f"---\n {x+1} "
        else:
            grid_display += f"---\n {x+1}"

        for y in range(size):
            grid_display += f"| {grid[x][y]} "
    
    return grid_display


#main function
def main():
    while True:
        try:
            size = int(input("\nhow big is the board? "))
            if size > 0:
                break
            print("\ninvalid input")
        except ValueError:
            print("\ninvalid input")

    grid = grid_size(size)
    print(display_grid(grid, size))

while True:
    main()
    if input() == "y":
        break