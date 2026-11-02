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
