#!/usr/bin/python3
"""
Pascal's Triangle
"""
def pascal_triangle(n):
    ans = []
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
