#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
  """ determines if all the boxes can be opened """

  n = len(boxes)
  openedBoxes = set(boxes[0])
  openedBoxes.add(0)
  for i in range(1, n):
    for j in range(1, n):
      if j in openedBoxes:
        openedBoxes.update(boxes[j])

  return len(openedBoxes) >= n
