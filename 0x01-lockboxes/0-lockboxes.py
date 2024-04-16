#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
  """ determines if all the boxes can be opened """

  n = len(boxes)
  openedKeys = set(boxes[0])
  openedKeys.add(0)
  for j in range(2):
    for i in range(1, n):
      if i in openedKeys:
        openedKeys.update(boxes[i])

  if len(openedKeys) >= n:
    return True
  else:
    return False
