#!/usr/bin/python3
"""
Module pour calculer le nombre minimum d'opérations.
"""


def minOperations(n):
    """Calcule le nombre le plus bas d'operations pour obtenir nH.
    Retourne un entier, ou 0 si n est impossible a atteindre.
    """
    if n <= 1:
        return 0

    operations = 0
    facteur = 2

    while n > 1:
        if n % facteur == 0:
            operations += facteur
            n = n // facteur
        else:
            facteur += 1

    return operations
