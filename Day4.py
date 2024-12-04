def get_file_data(file_name):
    f = open(file_name)
    data = []
    for line in f:
        data.append(line.rstrip())
    return data

def check_left(grid, row, col):
    if(col >= 3):
        if grid[row][col-1] == "M" and grid[row][col-2] == "A" and grid[row][col-3] == "S":
            return 1
        else:
            return 0
    return 0

def check_right(grid, row, col):
    if(col <= len(grid[row])-3):
        if grid[row][col+1] == "M" and grid[row][col+2] == "A" and grid[row][col+3] == "S":
            return 1
        else:
            return 0
    return 0

def check_up(grid,row,col):
    if(row>=3):
        if grid[row-1][col] == "M" and grid[row-2][col] == "A" and grid[row-3][col]== "S":
            return 1
        else:
            return 0
    return 0

def check_up(grid,row,col):
    if(row>=3):
        if grid[row-1][col] == "M" and grid[row-2][col] == "A" and grid[row-3][col]== "S":
            return 1
        else:
            return 0
    return 0

def check_down(grid,row,col):
    if(row<= len(grid)-3):
        if grid[row-1][col] == "M" and grid[row-2][col] == "A" and grid[row-3][col]== "S":
            return 1
        else:
            return 0
    return 0
def solve_part1(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(check_up(grid,i,j))


file_data = get_file_data("InputFile")

# build a 2D List based on the file_data
grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

#for i in range(len(grid)):
#    for j in range(len(grid[i])):
#        print(grid[i][j])


solve_part1(grid)