#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''Calculates the fewest number of operations needed to result in exactly
    n H characters in this file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The fewest number of operations needed.
            If n is impossible to achieve, returns 0.
    '''
    pasted_chars = 1  # Number of characters in the file
    clipboard = 0  # Number of 'H's copied
    counter = 0

    while pasted_chars < n:
        if clipboard == 0:  # If clipboard is empty
            clipboard = pasted_chars
            counter += 1

        if pasted_chars == 1:  # If nothing has been pasted yet
            pasted_chars += clipboard
            counter += 1
            continue

        remaining = n - pasted_chars  # Remaining characters to paste
        if remaining < clipboard:  # If impossible to achieve n characters
            return 0

        if remaining % pasted_chars != 0:  # If remaining cannot be divided
            pasted_chars += clipboard
            counter += 1
        else:
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2

    if pasted_chars == n:
        return counter
    else:
        return 0
