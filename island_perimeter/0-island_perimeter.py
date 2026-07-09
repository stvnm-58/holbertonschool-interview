#!/usr/bin/python3
"""
Module pour la fonction island_perimeter.
"""


def island_perimeter(grid: list[list[int]]) -> int:
    """
    Calcule le périmètre de l'île décrite dans la grille.

    Args:
        grid (list[list[int]]): Une liste de listes d'entiers représentant
                                la grille (0 pour l'eau, 1 pour la terre).

    Returns:
        int: Le périmètre total de l'île.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # On commence par ajouter les 4 côtés de la cellule de terre
                perimeter += 4

                # Si le voisin du haut est aussi de la terre,
                # on retire les 2 côtés partagés (un pour chaque cellule)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Si le voisin de gauche est aussi de la terre,
                # on retire les 2 côtés partagés
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
