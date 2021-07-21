#!/usr/bin/python3
"""Lockbox."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be openedboxes is a list of lists.
    Args:
        boxes (list): a list of lists
    Returns:
        True if all boxes can be opened, else return FalseCheck if Boxes
    """
    stack = [0]
    unlocked = [1] + [0] * (len(boxes) - 1)
    i = 0

    if len(boxes) == 0:
        return True
    if not isinstance(boxes, list):
        return False
    while stack:
        p = stack.pop()
        for key in boxes[p]:
            if key > 0 and key < len(boxes) and unlocked[key] == 0:
                unlocked[key] = 1
                stack.append(key)
        i = i + 1

    if 0 in unlocked:
        return False
    else:
        return True
