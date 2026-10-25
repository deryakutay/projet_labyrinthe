import random

class cell:
    def __init__(self):
        self.upWall = True
        self.rightWall = True
        self.lowWall = True
        self.leftWall = True

directions = [
    (1,0),   #up
    (0,1),   #right
    (-1,0),  #down
    (0,-1)]  #left


nbrow = 10
nbcol = 10

grid = [[cell for y in range(nbrow)] for x in range(nbcol)]
start = grid[0][random.randint(0,nbcol)]
queue = [start]


def create(queue, grid, y, x):
    if len(queue) == 0:
        return grid
    else:
#
        breeze = []
        for direction in directions:
            j = direction[0] + y
            i = direction[1] + x
            if grid[j][i] not in queue and x < len(grid[0]) and y < len(grid):
                breeze.append[direction]
        nextBreeze = random.choice(breeze)
        b = nextBreeze[0] + y
        a = nextBreeze[1] + x

        voisin = grid[j][i]

        if nextbreeze == direction[0]:
            grid[y][x].upWall = False
            voisin.lowWall = False
        if nextbreeze == direction[1]:
            grid[y][x].rightWall = False
            voisin.leftWall = False
        if nextbreeze == direction[2]:
            grid[y][x].lowWall = False
            voisin.upWall = False
        if nextbreeze == direction[3]:
            grid[y][x].leftWall = False
            voisin.rightWall = False
        queue.append(voisin)

        for direction in directions:
            verif = []
            j = direction[0] + y
            i = direction[1] + x
            verif.append(grid[j][i])
        if len(verif) == 3:
            queue.pop(grid[y][x])

        return create(queue, voisin, b, a)

