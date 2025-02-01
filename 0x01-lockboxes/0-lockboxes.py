#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def x(i, vis, boxes):
    """Check if all boxes can be opened by dfs
    Args:
    i (int): List child
        vis (list): List to check visited
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """

    vis[i] = 1
    for it in boxes[i]:
        if it < len(vis) and vis[it] == 0:
            x(it, vis, boxes)


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
        """

    vis = []
    for i in range(0, len(boxes)):
        vis.append(0)
    vis[0] = 1
    x(0, vis, boxes)
    for i in range(0, len(vis)):
        if vis[i] == 0:
            return False
    return True


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
