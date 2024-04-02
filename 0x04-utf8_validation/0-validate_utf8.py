#!/usr/bin/python3


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the bytes of the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Loop through each byte in the data set
    for byte in data:
        # If this byte is the start of a new UTF-8 character
        if num_bytes == 0:
            # Determine the number of leading 1s in the byte
            if byte >> 7 == 0b0:
                num_bytes = 1
            elif byte >> 5 == 0b110:
                num_bytes = 2
            elif byte >> 4 == 0b1110:
                num_bytes = 3
            elif byte >> 3 == 0b11110:
                num_bytes = 4
            else:
                # Invalid start of UTF-8 character
                return False
            num_bytes -= 1
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
            if num_bytes > 0:
                return False
    return num_bytes == 0
