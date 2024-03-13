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

    if not boxes:
        return False

    """ Initialize a set to keep track of opened boxes """
    opened_boxes = {0}
    """ Initializa a set to keep tracks of the keys """
    keys = set(boxes[0])

    """ Loop until no new keys are found """
    while keys:
        """ Pops key from the set """
        key = keys.pop()

        """ If key opens a box yet to be opened """
        if key < len(boxes) and key not in opened_boxes:
            """ Adds box to the opened boxes set """
            opened_boxes.add(key)
            """ Adds keys in opened box to keys set """
            keys.update(boxes[key])
    return len(opened_boxes) == len(boxes)
