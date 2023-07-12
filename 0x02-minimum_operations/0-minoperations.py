#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
  """A method that returns the fewest num of operations"""
  num_of_operations = 0
  index = 2
  if n <= 1:
    return 0
  while (index < n + 1):
    """checks if n is divisible"""
    while n % index == 0:
      num_of_operations += index
      n /= index
    index += 1
  return num_of_operations
