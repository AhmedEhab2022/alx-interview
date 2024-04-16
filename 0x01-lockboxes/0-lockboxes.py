#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
  """ determines if all the boxes can be opened """

  n = len(boxes)
  openedBoxes = set(boxes[0])
  openedBoxes.add(0)
  newBoxes = set(boxes[0])
  newBoxes.add(0)
  while newBoxes:
    box = newBoxes.pop()
    for key in boxes[box]:
      if key not in openedBoxes:
        newBoxes.add(key)
        openedBoxes.add(key)

  return len(openedBoxes) >= n
