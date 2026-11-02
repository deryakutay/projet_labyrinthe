<<<<<<< HEAD

import random
=======
import random
from maze_display import display_maze
>>>>>>> b2893ad (nettoyage)

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
nbrow = 4
nbcol = 4

grid = [[cell(y, x) for x in range(nbcol)] for y in range(nbrow)]
start = grid[0][random.randrange(0, nbcol)]
=======
nbrow = 20
nbcol = 20

<<<<<<<< HEAD:random.py
nbrow = 4
nbcol = 4

grid = [[cell(y,x) for x in range(nbcol)] for y in range(nbrow)]
start = grid[0][random.randrange(0,nbcol)]
========
grid = [[cell(y, x) for x in range(nbcol)] for y in range(nbrow)]
start = grid[0][random.randrange(0, nbcol)]
>>>>>>>> b2893ad (nettoyage):lastOrRandom.py
>>>>>>> b2893ad (nettoyage)
start.visited = True
chain = [start]


def create(queue, grid):
    if not queue:
        return grid
    else:
<<<<<<< HEAD
        breeze = []

        compteur = random.randrange(0, 4)

        if (compteur == 1):
            current = queue[random.randrange(0, len(queue))]
            print("randed")
        else:
            current = queue[-1]
=======
<<<<<<<< HEAD:random.py
        current = queue[random.randrange(0,len(queue))]
========
>>>>>>>> b2893ad (nettoyage):lastOrRandom.py
        breeze = []

        tirage = random.randrange(0, 4)

        if (tirage == 1):
            index = random.randrange(0, len(queue))
            print("randed")
        else:
            index = -1

        current = queue[index]
>>>>>>> b2893ad (nettoyage)

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
<<<<<<< HEAD

        if not breeze:
            queue.pop()
            return create(queue, grid)
=======
        if not breeze:
<<<<<<<< HEAD:random.py
            queue.pop()
            return create(queue,grid)
========
            queue.pop(index)
            return create(queue, grid)
>>>>>>>> b2893ad (nettoyage):lastOrRandom.py
>>>>>>> b2893ad (nettoyage)

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


<<<<<<< HEAD
create(chain, grid)



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
<<<<<<<< HEAD:random.py


========
>>>>>>>> b2893ad (nettoyage):lastOrRandom.py
create(chain, grid)

>>>>>>> b2893ad (nettoyage)
display_maze(grid)
