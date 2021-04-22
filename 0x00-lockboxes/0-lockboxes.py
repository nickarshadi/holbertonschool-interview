#!/usr/bin/python3
"""Lockboxmodule."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
    keys = [0]
    for index in keys:
        for key in boxes[index]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False
