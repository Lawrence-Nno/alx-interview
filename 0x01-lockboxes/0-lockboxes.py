#!/usr/bin/python3
"""
A script to determine if all n number of locked boxes can be opened. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
  # a function to determine if all the boxes can be opened
  if not boxes:
      return False
  amount = len(boxes)
  result = {}
  index = 0

  for box in boxes:
      if len(box) == 0 or index == 0:
          result[index] = -1
      for key in box:
          if key < amount and key != index:
              result[key] = key
      if len(result) == amount:
          return True
      index += 1
  return False
