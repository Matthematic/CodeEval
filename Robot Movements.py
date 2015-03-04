from copy import deepcopy


def find_paths(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0
    elif grid[i][j] == 1:
        return 0
    elif i == len(grid)-1 and j == len(grid[0])-1:
        return 1
    else:
        grid[i][j] = 1

        copy1 = deepcopy(grid)
        copy2 = deepcopy(grid)
        copy3 = deepcopy(grid)
        copy4 = deepcopy(grid)


        return find_paths(i+1, j, copy1) + find_paths(i-1, j, copy2) + find_paths(i, j+1, copy3) + find_paths(i, j-1, copy4)



grid = [[0]*4 for x in range(4)]
print (find_paths(0, 0, grid))