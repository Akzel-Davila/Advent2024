
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
    if(col < len(grid[row])-3):
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
    if(row < len(grid)-3):
        if grid[row+1][col] == "M" and grid[row+2][col] == "A" and grid[row+3][col]== "S":
            return 1
        else:
            return 0
    return 0

def check_up_right(grid,row,col):
    if(row>=3 and col < len(grid[row])-3):
        if grid[row-1][col+1] == "M" and grid[row-2][col+2] == "A" and grid[row-3][col+3] == "S":
            return 1
        else:
            return 0
    return 0

def check_S(grid,row,col):
    s_count = 0
    if(row>=1 and col < len(grid[row])-1): #Up right
        if grid[row-1][col+1] == "S":
            s_count+=1
    if(row>=1 and col >= 1): #Up left
        if grid[row-1][col-1] == "S":
            s_count+=1
    if(row < len(grid)-1 and col < len(grid[row])-1): #Down right
        if grid[row+1][col+1] == "S":
            s_count+=1
    if(row < len(grid)-1 and col >= 1): #Down left
        if grid[row+1][col-1] == "S":
            s_count+=1
    if(row < len(grid)-1 and col >= 1 and row>=1 and col < len(grid[row])-1):
        s_count = 0
    if(row>=1 and col >= 1 and row < len(grid)-1 and col < len(grid[row])-1):
        s_count =0



def check_up_left(grid,row,col):
    if(row>=3 and col >= 3):
        if grid[row-1][col-1] == "M" and grid[row-2][col-2] == "A" and grid[row-3][col-3] == "S":
            return 1
        else:
            return 0
    return 0

def check_down_right(grid,row,col):
    if(row < len(grid)-3 and col < len(grid[row])-3):
        if grid[row+1][col+1] == "M" and grid[row+2][col+2] == "A" and grid[row+3][col+3] == "S":
            return 1
        else:
            return 0
    return 0

def check_down_left(grid,row,col):
    if(row < len(grid)-3 and col >= 3):
        if grid[row+1][col-1] == "M" and grid[row+2][col-2] == "A" and grid[row+3][col-3] == "S":
            return 1
        else:
            return 0
    return 0

def solve_part1(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == "X"):
                total += check_up(grid,i,j)
                total += check_down(grid, i, j)
                total += check_left(grid, i, j)
                total += check_right(grid, i, j)
                total += check_up_right(grid, i, j)
                total += check_up_left(grid, i, j)
                total += check_down_left(grid, i, j)
                total += check_down_right(grid, i, j)
    print(total)

file_data = get_file_data("InputFile")

# build a 2D List based on the file_data
grid = []
for line in file_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)


solve_part1(grid)
