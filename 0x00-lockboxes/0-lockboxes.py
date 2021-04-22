#!/usr/bin/python3
"""Unlock all boxes Module."""


def canUnlockAll(boxes):
    """Open all boxes."""
    keys = {0}
    allkeys = {0}
    i = 0
    v = 0
    if not boxes or len(boxes) <= 1:
        return True
    while i < 1000:
        for key in boxes[v]:
            keys.add(key)
            allkeys.add(key)
        if len(allkeys) >= len(boxes):
            return True
        if keys:
            v = keys.pop()
        else:
            return False
        i += 1
    return False
