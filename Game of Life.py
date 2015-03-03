import sys
from copy import deepcopy

class GameOfLife():
    def __init__(self, grid):
        self.grid = grid
        self.copy = deepcopy(self.grid)

    def count_live_neighbors(self, i, j): #i, j are the cell position
        count = 0
        cell = self.grid[i][j]

        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]): #out of bounds
            return 0

        else:
            indices_i = [i, i+1, i-1]
            indices_j = [j, j+1, j-1]


            for index_i in indices_i:
                for index_j in indices_j:
                    if not (index_i < 0 or index_j < 0 or index_i >= len(self.grid) or index_j >= len(self.grid[0])): #if in bounds
                        if self.grid[index_i][index_j] == '*' and [index_i,index_j] != [i,j]:
                            count += 1

        self.ObeyRules(i, j, count, cell)

        #return count


    def ObeyRules(self, i, j, count, cell):
        if cell == '*':
            if count >= 4 or count <= 1:
                self.copy[i][j] = '.'
        else:
            if count == 3:
                self.copy[i][j] = '*'




test_cases = open(sys.argv[1], 'r')



grid = []

for test in test_cases:
    test = test.strip()
    if test.strip() != '':
        for character in test:
            grid.append(character)


grid = [grid[x:x+100] for x in range(0, len(grid),100)]


for i in range(10):
    g1 = GameOfLife(grid)

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            g1.count_live_neighbors(x, y)

    grid =  g1.copy

for row in grid:
    for cell in row:
        sys.stdout.write(cell)
    print ('\n')
    
    
test_cases.close()
