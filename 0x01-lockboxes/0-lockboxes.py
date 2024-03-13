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
    
    for box in boxes:
        ibox = boxes.index(box)
        if ibox not in keys:
            if max(keys) > ibox:
                locked.add(ibox)
                continue
        keys |= set(box)
    for key in locked:
        if key in keys:
            keys |= set(boxes[key])
    return not bool(locked - keys)
