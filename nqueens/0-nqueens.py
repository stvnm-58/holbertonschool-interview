#!/usr/bin/python3
"""
Module de résolution du problème des N reines (N-Queens).

Ce script utilise un algorithme de retour sur trace (backtracking) pour placer
N reines sur un échiquier de taille N x N sans qu'elles ne se menacent mutuellement.

Usage:
    ./nqueens.py N
"""

import sys


def est_valide(reines, ligne, colonne):
    """
    Vérifie si une reine peut être placée en toute sécurité à une position donnée.

    Arguments:
        reines (list): Liste des coordonnées [[l1, c1], [l2, c2], ...] des reines déjà placées.
        ligne (int): L'index de la ligne de la position cible.
        colonne (int): L'index de la colonne de la position cible.

    Retour:
        bool: True si la position est valide (non menacée), False sinon.
    """
    for reine in reines:
        # 1. Vérification de la colonne
        if reine[1] == colonne:
            return False
        # 2. Vérification de la diagonale principale (\)
        # Sur cette diagonale, la différence (ligne - colonne) reste constante
        if reine[0] - reine[1] == ligne - colonne:
            return False
        # 3. Vérification de la diagonale secondaire (/)
        # Sur cette diagonale, la somme (ligne + colonne) reste constante
        if reine[0] + reine[1] == ligne + colonne:
            return False
    return True


def resoudre_nreines(N, ligne, reines):
    """
    Explore récursivement l'échiquier ligne par ligne pour placer les reines.

    Arguments:
        N (int): La taille de l'échiquier (et le nombre de reines à placer).
        ligne (int): La ligne actuelle en cours d'évaluation.
        reines (list): Liste des positions des reines déjà validées.
    """
    # Cas de base : si la ligne courante est égale à N, toutes les reines sont placées
    if ligne == N:
        print(reines)
        return

    # Cas récursif : tester toutes les colonnes possibles pour la ligne actuelle
    for colonne in range(N):
        if est_valide(reines, ligne, colonne):
            # Passage à la ligne suivante en ajoutant la nouvelle position valide
            resoudre_nreines(N, ligne + 1, reines + [[ligne, colonne]])


# ==============================================================================
# Bloc d'exécution principal : Validation des entrées et lancement du script
# ==============================================================================
if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Vérification du type de l'argument (doit être un entier)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Vérification de la contrainte de taille minimale
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Lancement de la résolution à partir de la ligne 0 avec un échiquier vide
    resoudre_nreines(N, 0, [])
