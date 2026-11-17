import lastOrRandom

grid = lastOrRandom.grid

case = grid[0][0]
print("Cellule :", case.y, case.x)
print("mur haut :", case.upWall)
print("mur bas :", case.lowWall)
print("mur gauche :", case.leftWall)
print("mur droite :", case.rightWall)

def voisins_accessibles(grid, cellule):
    y = cellule.y
    x = cellule.x
    resultat = []
    if not cellule.upWall:
        resultat.append(grid[y - 1][x])
    if not cellule.lowWall:
        resultat.append(grid[y+1][x])
    if not cellule.leftWall:
        resultat.append(grid[y][x-1])
    if not cellule.rightWall:
        resultat.append(grid[y][x+1])
    return resultat
def est_une_impasse(grid, cellule):
    voisins = voisins_accessibles(grid, cellule)
    if len(voisins)==2:
        return False
    elif len(voisins)==1 :
        return True
    else :
        return False
print("Voisins accessibles de (0,0) :")
for v in voisins_accessibles(grid, grid[0][0]):
    print(v.y, v.x)
compteur = 0
for ligne in grid:
    for cellule in ligne:
        if est_une_impasse(grid, cellule):
            compteur = compteur + 1
print("Nombre d'impasses :", compteur)

print(est_une_impasse(grid , grid[0][3]))
def boucher_impasses(grid, depart, arrivee):
    bouchees = set()                         
    a_change = True
    while a_change:                        
        a_change = False                     
        for ligne in grid:                   
            for cellule in ligne:            
                if cellule != depart and cellule != arrivee and cellule not in bouchees:
                                            
                                          
                    libres = voisins_libres(grid, cellule, bouchees)
                                             
                    if len(libres) == 1:           
                        bouchees.add(cellule)    
                        a_change = True          
    return bouchees
def voisins_libres(grid, cellule, bouchees):
    resultat = []
    for v in voisins_accessibles(grid, cellule):
        if v not in bouchees :
            resultat.append(v)
    return resultat

def suivre_chemin(grid, depart, arrivee, bouchees):
    chemin = [depart]
    precedent = None
    courant = depart
    while courant != arrivee:
        for v in voisins_libres(grid, courant, bouchees):
            if v != precedent:
                suivant = v
        precedent = courant
        courant = suivant
        chemin.append(courant)
    return chemin

def afficher_solution(grid, chemin):
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
            middle += " o " if grid[y][x] in chemin else "   "

        middle += "|" if grid[y][nbcol - 1].rightWall else " "
        print(middle)

    # Affichage du bas de la dernière ligne
    bottom = ""
    for x in range(nbcol):
        bottom += "+"
        bottom += "---" if grid[nbrow - 1][x].lowWall else "   "

    bottom += "+"
    print(bottom)


depart = grid[0][0]
arrivee = grid[len(grid) - 1][len(grid[0]) - 1]
bouchees = boucher_impasses(grid, depart, arrivee)  
nb_restantes = len(grid) * len(grid[0]) - len(bouchees)
print("Cases bouchées :", len(bouchees))
print("Cases restantes (= longueur du chemin) :", nb_restantes)
chemin = suivre_chemin(grid, depart, arrivee, bouchees)
print("Longueur du chemin suivi :", len(chemin))
print("Première case :", chemin[0].y, chemin[0].x)
print("Dernière case :", chemin[-1].y, chemin[-1].x)
afficher_solution(grid, chemin)
