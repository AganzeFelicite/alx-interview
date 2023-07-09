#!/usr/bin/python3
"""this is an interview question on lockboxes"""


def canUnlockAll(boxes):
    """this a module finds a key to unlock all boxes"""
    for i in range(len(boxes)):
        flag = True
        for j in range(len(boxes[i])):
            if boxes[i][j] == i:
                continue
            else:
                flag = False
                break
    return flag
