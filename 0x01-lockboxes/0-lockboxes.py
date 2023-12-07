#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))
    while len(unchecked_boxes) > 0:
        box_idx = unchecked_boxes.pop()
        if not box_idx or box_idx >= n or box_idx < 0:
            continue
        if box_idx not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[box_idx])
            checked_boxes.add(box_idx)
    return n == len(checked_boxes)

