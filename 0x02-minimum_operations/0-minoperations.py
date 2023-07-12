#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
  """A method that returns the fewest num of operations"""
  num_of_operations = 0
  if n <= 1:
    return 0

  for i in range(2, n + 1):
    """checks if n is divisible"""
    while n % i == 0:
      n = n / i
      num_of_operations += 1
  return num_of_operations
