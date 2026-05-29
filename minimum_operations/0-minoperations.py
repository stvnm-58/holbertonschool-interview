#!/usr/bin/env python3
"""Module pour calculer le nombre minimum d'opérations Copy/Paste."""


def minOperations(n):
    """Calcule le plus petit nombre d'opérations pour obtenir exactement n 'H'.

    Args:
        n (int): Le nombre cible de caractères 'H'.

    Returns:
        int: Le nombre minimum d'opérations, ou 0 si n est inférieur ou égal à 1.
    """
    # Si n est inférieur ou égal à 1, il est impossible ou déjà atteint
    if n <= 1:
        return 0

    operations = 0
    diviseur = 2

    # Décomposition en facteurs premiers
    while n > 1:
        # Tant que n est divisible par le diviseur actuel
        while n % diviseur == 0:
            # On ajoute le diviseur au total des opérations
            operations += diviseur
            # On réduit n
            n //= diviseur
        # On passe au diviseur suivant
        diviseur += 1

    return operations