# Projet Labyrinthe

Ce dépôt a été créé pour le projet Labyrinthe de la Vague 1, réalisé en troisième année en Génie Mathématique à l’INSA Rouen Normandie. Les scripts Python génèrent des labyrinthes rectangulaires avec l’algorithme récursif *Growing Tree*. Le projet compare les formes obtenues en changeant la règle de sélection des cellules actives.

## Démarrage rapide

Pour générer et résoudre un labyrinthe, exécutez le script de résolution avec Python 3. Les générateurs utilisent le module `random` de la bibliothèque standard.

```bash
git clone https://github.com/deryakutay/projet_labyrinthe.git
cd projet_labyrinthe
python3 resolution_affichage_de_solution.py
```

Les scripts de génération affichent les étapes de l’algorithme, puis le labyrinthe en ASCII dans le terminal. La grille fait 20 × 20 par défaut. Pour changer ses dimensions, modifiez `nbrow` (lignes) et `nbcol` (colonnes) dans le script choisi.

## Méthodes de génération

Lancez le script correspondant avec `python3`.

| Script | Choix de la cellule active |
| --- | --- |
| [`theMostRecent.py`](theMostRecent.py) | Dernière cellule ajoutée à la liste. Cette règle correspond à un parcours en profondeur. |
| [`randomized.py`](randomized.py) | Cellule tirée au hasard dans toute la liste. |
| [`lastn.py`](lastn.py) | Cellule tirée au hasard parmi les `n` dernières cellules de la liste, ou parmi toutes les cellules si la liste en contient moins de `n`. Par défaut, `n = 20`. |
| [`lastOrRandom.py`](lastOrRandom.py) | Dernière cellule dans trois tirages sur quatre. Dans le cas restant, la cellule est tirée au hasard dans toute la liste. |

À chaque appel récursif, le programme choisit une cellule active. Si elle possède des voisines non visitées, il ouvre un passage vers l’une d’elles, la marque comme visitée et l’ajoute à la liste. Si toutes ses voisines ont déjà été visitées ou qu’elle n’en a aucune, seule cette cellule est retirée de la liste. La génération s’arrête quand la liste est vide.

Chaque cellule représente un sommet et chaque passage représente une arête. Comme chaque passage ouvert relie une cellule déjà visitée à une nouvelle cellule, aucun cycle ne se forme. À la fin, toutes les cellules sont reliées et les passages forment un arbre couvrant de la grille. Il existe donc une unique chaîne simple entre deux cellules quelconques.

## Résolution automatique

Le [script de résolution](resolution_affichage_de_solution.py) importe `lastOrRandom` par défaut, récupère la grille générée (`lastOrRandom.grid`), puis cherche le chemin du coin supérieur gauche au coin inférieur droit. Il écarte successivement les impasses en préservant ces deux cellules. Les cellules restantes forment le chemin, marqué par des `o` dans l’affichage final.

### Changer de méthode de génération

Dans `resolution_affichage_de_solution.py`, modifiez les deux lignes au début du fichier. Par exemple, pour utiliser la méthode `lastn`, écrivez ceci.

```python
import lastn

grid = lastn.grid
```

Relancez ensuite le script de résolution.

## Auteurs

Fadi Alkhoury, Derya Kutay Kaptanoğlu et Yahya El Ouardighi.
