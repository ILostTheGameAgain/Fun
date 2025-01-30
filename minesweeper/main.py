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


#function to place the mines on a grid
def mines(grid, size):
    mine_count = int((size**2)/5)
    for i in range(mine_count):
        #while loop to keep running until the mine is in an empty space
        while True:
            randomX = random.randint(1, size)-1
            randomY = random.randint(1, size)-1
            if grid[randomX][randomY] == " ":
                grid[randomX][randomY] = "X"
                break

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


#function for user input
def user_input(type, posX, posY, grid, mine_grid):
    if type == 1
    


#main function
def main():
    while True:
        try:
            size = int(input("\nhow big is the board? (must be at least 3) "))
            if size >= 3:
                break
            print("\ninvalid input")
        except ValueError:
            print("\ninvalid input")

    grid = grid_size(size)
    print(display_grid(grid, size))
    mine_grid = mines(grid, size)

    while True:
        user_input()

while True:
    main()
    if input() == "y":
        break