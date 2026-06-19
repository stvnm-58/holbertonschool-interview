def validUTF8(data):
    # Number of continuation bytes we are expecting
    remaining_bytes = 0

    for num in data:
        # Get only the 8 least significant bits
        byte = num & 0xFF

        if remaining_bytes > 0:
            # Check if it's a valid continuation byte (starts with 10)
            if (byte >> 6) == 0b10:
                remaining_bytes -= 1
            else:
                return False
        else:
            # Check the prefix to determine the number of bytes for the character
            if (byte >> 7) == 0b0:
                remaining_bytes = 0
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                # Malformed starting byte (e.g., starts with 10xxxxxx or 11111xxx)
                return False

    # If remaining_bytes is 0, all characters were completely processed
    return remaining_bytes == 0
