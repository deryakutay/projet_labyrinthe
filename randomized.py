import random
from maze_display import display_maze

class cell:
    def __init__(self,y,x):
        self.visited = False
        self.y = y
        self.x = x
        self.upWall = True
        self.rightWall = True
        self.lowWall = True
        self.leftWall = True

directions = [
    (1,0),   #down
    (0,1),   #right
    (-1,0),  #up
    (0,-1)]  #left


nbrow = 20
nbcol = 20

grid = [[cell(y,x) for x in range(nbcol)] for y in range(nbrow)]
start = grid[0][random.randrange(0,nbcol)]
start.visited = True
chain = [start]


def create(queue, grid):
    if not queue:
        return grid
    else:
        index = random.randrange(0,len(queue))
        current = queue[index]
        breeze = []
        print("Current:", (current.y, current.x))
        print("Queue:", [(c.y, c.x) for c in queue])
        print("------------------------------")

        for direction in directions:
            j = direction[0] + current.y
            i = direction[1] + current.x

            if (0<= i < len(grid[0]) and 0 <= j < len(grid) and not grid[j][i].visited):
                breeze.append(direction)
        if not breeze:
            queue.pop(index)
            return create(queue,grid)

        nextBreeze = random.choice(breeze)
        b = nextBreeze[0] + current.y
        a = nextBreeze[1] + current.x
        voisin = grid[b][a]

        if nextBreeze == directions[0]:
            current.lowWall = False
            voisin.upWall = False

        if nextBreeze == directions[1]:
            current.rightWall = False
            voisin.leftWall = False

        if nextBreeze == directions[2]:
            current.upWall = False
            voisin.lowWall = False

        if nextBreeze == directions[3]:
            current.leftWall = False
            voisin.rightWall = False

        voisin.visited = True
        queue.append(voisin)

        return create(queue, grid)




create(chain, grid)

display_maze(grid)
