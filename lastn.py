
import random
<<<<<<< HEAD
=======
from maze_display import display_maze
>>>>>>> 0bdb6d7 (ça me semble bien :))

class cell:
    def __init__(self, y, x):
        self.visited = False
        self.y = y
        self.x = x
        self.upWall = True
        self.rightWall = True
        self.lowWall = True
        self.leftWall = True


directions = [
    (1, 0),   # down
    (0, 1),   # right
    (-1, 0),  # up
    (0, -1)   # left
]

<<<<<<< HEAD
nbrow = 10
nbcol = 10
=======
nbrow = 20
nbcol = 20
>>>>>>> 0bdb6d7 (ça me semble bien :))

grid = [[cell(y, x) for x in range(nbcol)] for y in range(nbrow)]
start = grid[0][random.randrange(0, nbcol)]
start.visited = True
chain = [start]


def create(queue, grid):
    if not queue:
        return grid
    else:
        breeze = []
<<<<<<< HEAD
        n = 5
        if (n < len(queue)):
            current = queue[random.randrange(len(queue)-n, len(queue))]

        else:
            current = queue[-1]
=======
        n = 20
        index = random.randrange(max(0, len(queue)-n), len(queue))
        current = queue[index]
>>>>>>> 0bdb6d7 (ça me semble bien :))

        print("Current:", (current.y, current.x))
        print("Queue:", [(c.y, c.x) for c in queue])
        print("------------------------------")

        for direction in directions:
            j = direction[0] + current.y
            i = direction[1] + current.x

            if (0 <= i < len(grid[0])
                    and 0 <= j < len(grid)
                    and not grid[j][i].visited):
                breeze.append(direction)

        if not breeze:
<<<<<<< HEAD
            queue.pop()
=======
            queue.pop(index)
>>>>>>> 0bdb6d7 (ça me semble bien :))
            return create(queue, grid)

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

<<<<<<< HEAD


def display_maze(grid):
    nbrow = len(grid)
    nbcol = len(grid[0])

    for y in range(nbrow):
        # Affichage des murs du haut
        top = ""
        for x in range(nbcol):
            top += "+"
            top += "---" if grid[y][x].upWall else "   "
        top += "+"

        print(top)

        # Affichage des murs latéraux
        middle = ""
        for x in range(nbcol):
            middle += "|" if grid[y][x].leftWall else " "
            middle += "   "

        middle += "|" if grid[y][nbcol - 1].rightWall else " "
        print(middle)

    # Affichage du bas de la dernière ligne
    bottom = ""
    for x in range(nbcol):
        bottom += "+"
        bottom += "---" if grid[nbrow - 1][x].lowWall else "   "

    bottom += "+"
    print(bottom)

=======
>>>>>>> 0bdb6d7 (ça me semble bien :))
display_maze(grid)
