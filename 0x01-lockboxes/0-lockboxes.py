#!/usr/bin/python3
"""
Module for canUnlockAll method.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list): A list of lists representing locked boxes and their keys.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    """ Initialize a set with keys available in the first box (box 0) """
    keys = set([0] + boxes[0])
    """ Initialize a set to keep track of locked boxes """
    locked = set()
    
    """ Iterate through each box and check if it can be opened """
    for i, box in enumerate(boxes):
        if i not in keys:
            locked.add(i)
        else:
            keys |= set(box)
    
    """ Loop through locked boxes and try to unlock using available keys """
    for key in list(locked):
        if key in keys:
            keys |= set(boxes[key])
            locked.remove(key)
    
    return not bool(locked)
