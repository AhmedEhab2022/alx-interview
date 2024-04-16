#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
  """ determines if all the boxes can be opened """

  n = len(boxes)
  openedBoxes = set(boxes[0])
  openedBoxes.add(0)
  newBoxes = openedBoxes.copy()
  while True:
    for box in newBoxes:
      for key in boxes[box]:
        if key not in openedBoxes and key < n:
          openedBoxes.add(key)
    if len(openedBoxes) == len(newBoxes):
      break
    newBoxes = openedBoxes.copy()

  return len(newBoxes) >= n