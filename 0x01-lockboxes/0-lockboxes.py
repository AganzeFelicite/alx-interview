#!/usr/bin/python3
"""this is an interview question on lockboxes"""


def canUnlockAll(boxes):
    """this a module finds a key to unlock all boxes"""
    flag = True
    for i in range(len(boxes)):
        for h in range(len(boxes)):
            for j in range(len(boxes[i])):
                if boxes[i][j] == h:
                    flag = True
                    continue
                elif boxes[i][j] is None:
                    return False
                else:
                    flag = False
                    break
    return flag
