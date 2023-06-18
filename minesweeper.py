#--------------------------------------------------------------------------------------------------
# The minesweeper() function creates a grid with "#" representing mines and "-"
# representing empty spaces. It then calculates the number of adjacent mines for each empty space
# and replaces it with the count. The resulting grid is printed and returned.
# This function simulates the classic Minesweeper game where the player must
# use logic to avoid the mines and uncover all the empty spaces without detonating any mines.
#------------------------------------------------------------------------------------------------------
def minesweeper(input_grid):
    # Loop through each row of the input grid
    for i in range(len(input_grid)):
        # Loop through each column of the current row
        for j in range(len(input_grid[i])):
            # If the current cell is a mine
            if input_grid[i][j] == "-":
                count = 0
                #---------------------------------------------------------------------------------
                #This code checks each adjacent cell to see if there is a mine "#" present. If so,
                # it increments the count variable.
                #----------------------------------------------------------------------------------
                if i > 0 and j > 0 and input_grid[i-1][j-1] == "#":
                    count += 1
                if i > 0 and input_grid[i-1][j] == "#":
                    count += 1
                if i > 0 and j < len(input_grid[i])-1 and input_grid[i-1][j+1] == "#":
                    count += 1
                if j > 0 and input_grid[i][j-1] == "#":
                    count += 1
                if j < len(input_grid[i])-1 and input_grid[i][j+1] == "#":
                    count += 1
                if i < len(input_grid)-1 and j > 0 and input_grid[i+1][j-1] == "#":
                    count += 1
                if i < len(input_grid)-1 and input_grid[i+1][j] == "#":
                    count += 1
                if i < len(input_grid)-1 and j < len(input_grid[i])-1 and input_grid[i+1][j+1] == "#":
                    count += 1
                # Update the current cell with the number of adjacent mines
                input_grid[i][j] = str(count)
    # Print out the updated grid with spaces between each cell
    for row in input_grid:
        print(" ".join(row))
#Define an example input grid
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]
#Call the minesweeper function with the example input grid
minesweeper(input_grid)
