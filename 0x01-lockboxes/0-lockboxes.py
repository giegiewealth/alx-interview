#!/usr/bin/python3

# lockboxes


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    for key in range(1, len(boxes) - 1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = key in boxes[idx] and key != idx
            if ctr:
                break
        if ctr is False:
            return ctr
    return True
