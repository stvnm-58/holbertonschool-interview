#!/usr/bin/python3
"""
Module pour résoudre le problème des N reines
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def est_valide(reines, ligne, colonne):
    """Vérifie si on peut placer une reine à cette position"""
    for reine in reines:
        if reine[1] == colonne:
            return False
        if reine[0] - reine[1] == ligne - colonne:
            return False
        if reine[0] + reine[1] == ligne + colonne:
            return False
    return True


def resoudre_nreines(N, ligne, reines):
    """Fonction récursive pour trouver toutes les solutions"""
    if ligne == N:
        print(reines)
        return

    for colonne in range(N):
        if est_valide(reines, ligne, colonne):
            resoudre_nreines(N, ligne + 1, reines + [[ligne, colonne]])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

resoudre_nreines(N, 0, [])
