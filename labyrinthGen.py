import random

class cell:
    def __init__(self,y,x):
        self.y = y
        self.x = x
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

grid = [[cell(y,x) for x in range(nbcol)] for y in range(nbrow)]
start = grid[0][random.randrange(0,nbcol)]
chain = [start]


def create(queue, grid, current):
    print("Current:", (current.y, current.x))
    print("Queue:", [(c.y, c.x) for c in queue])
    print("------------------------------")
    if len(queue) == 0:
        return grid
    else:
       # for cell in queue:
       #     print((cell.y,cell.x))
        breeze = []

        for direction in directions:
            j = direction[0] + current.y
            i = direction[1] + current.x
            if 0<= current.x < len(grid[0])-1 and 0 <= current.y < len(grid)-1 and grid[j][i] not in queue:
                breeze.append(direction)
        nextBreeze = random.choice(breeze)
        b = nextBreeze[0] + current.y
        a = nextBreeze[1] + current.x

        voisin = grid[j][i]

        if nextBreeze == directions[0]:
            current.upWall = False
            voisin.lowWall = False
        if nextBreeze == directions[1]:
            current.rightWall = False
            voisin.leftWall = False
        if nextBreeze == directions[2]:
            current.lowWall = False
            voisin.upWall = False
        if nextBreeze == directions[3]:
            current.leftWall = False
            voisin.rightWall = False
        queue.append(voisin)

        for direction in directions:
            verif = []
            j = direction[0] + current.y
            i = direction[1] + current.x
            verif.append(grid[j][i])
        if len(verif) == 3:
            queue.pop(current)

        return create(queue, grid, voisin)

create(chain, grid, start)
