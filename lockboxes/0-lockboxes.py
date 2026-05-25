#!/usr/bin/python3
"""Module that checks if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list): List of lists containing keys.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    opened = set([0])
    keys = [0]

    while keys:
        current = keys.pop()

        for key in boxes[current]:
            if key < len(boxes) and key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == len(boxes)
