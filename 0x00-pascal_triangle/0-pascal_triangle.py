#!/usr/python3
"""
A function to print the pascal's triangle
"""


def pascal_triangle(n):
    """
    Pascal's Trangle function
    """
    # An empty list for each row
    ans = []
    #An empty list for each row of list
    final_list = []
    if n < 1:
        print(ans)
    for i in range(1, n + 1):
        c = 1
        ans = [c]
        for j in range(1, i):
            c = c * (i - j) // j
            ans.append(c)
        final_list.append(ans)
    return(final_list)
