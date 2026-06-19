#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes

    Returns:
        bool: True if valid UTF-8 encoding, else False
    """

    n_bytes = 0

    for num in data:
        byte = num & 0xFF  # consider only 8 least significant bits

        if n_bytes == 0:
            # 1-byte character: 0xxxxxxx
            if (byte >> 7) == 0b0:
                continue

            # 2-byte character: 110xxxxx
            elif (byte >> 5) == 0b110:
                n_bytes = 1

            # 3-byte character: 1110xxxx
            elif (byte >> 4) == 0b1110:
                n_bytes = 2

            # 4-byte character: 11110xxx
            elif (byte >> 3) == 0b11110:
                n_bytes = 3

            else:
                return False
        else:
            # continuation byte must be 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
