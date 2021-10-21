from time import perf_counter
import numpy as np


def lcs(X, Y, i, j):
    if (i == 0 or j == 0):
        return 0
    elif X[i-1] == Y[j-1]:
        return 1 + lcs(X, Y, i-1, j-1)
    else:
        return max(lcs(X, Y, i, j-1), lcs(X, Y, i-1, j))

# def lcs(X, Y, i, j):
#     if c[i][j] >= 0:
#         return c[i][j]
#     if (i == 0 or j == 0):
#         c[i][j] = 0
#     elif X[i-1] == Y[j-1]:
#         c[i][j] = 1 + lcs(X, Y, i-1, j-1)
#     else:
#         c[i][j] = max(lcs(X, Y, i, j-1), lcs(X, Y, i-1, j))
#     return c[i][j]


start = perf_counter()

X = "eeeeeeeeeeeeeeeeeeee"
Y = "rrrrrrrrrrrrrrrrrrrr"
lX = len(X)
lY = len(Y)
# uncomment the next line to initialize c (for memoization)
#c = [[-1 for k in range(lY+1)] for l in range(lX+1)]

start = perf_counter()
lcs(X, Y, lX, lY)
end = perf_counter()

print("time passed: ", end-start)
