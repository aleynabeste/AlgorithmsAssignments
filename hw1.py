
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


# start = perf_counter()

arr = []


X_arr = ["cttccatacagacacggttc", "aacgtattgcgcgcctcgga", "acccacagctacactaaggg", "caaaaggtaattggaactta", "tactcgggttgggaatcaag", "ggagtatacgcaagtgccat", "tacggaattgggcacgcaga", "gagaagcgggagtcggatag", "cagagaggcccttgcttatt", "gctataatcgtcagcgccca", "ccgagttatcgactcttttg", "agcaaaaacacccctggtta", "taatgaaagacctcgagcgt", "ggctctcggcagcgtactag", "gcaacttaaaattgaatccg",
         "acacagacagcagaggatgg", "atgatagtattattggttaa", "atgagaattggttaggtttt", "cagatttagttcgatggcgt", "tgcagagcaaaatagcctat", "ctaaaaacgggtctcctacc", "ttagagtacgcagactcctc", "ttagcatgagcgaggttcac", "gctcgctagctatggtagat", "agaattttagaagctccaac", "cttttagattgtgaaacctc", "gctgaatcgtgttgtaacac", "ctttaggttcggaacgcact", "taacttaagagcaatcttcg", "ctcatcaacattccgtggct"]
Y_arr = ["tcgcggtgagatcctgttgg", "ctgacttgacgttgcgcgtt", "gttaatggcaagtatcaccg", "gaaaaggcggcaaggtgtgt", "tcatctaaatacgtgttaca", "caagaaagttatggacgctc", "ttcatcccccgtggatgttg", "ttcgacccggcatccctgcg", "taacgcagcttgcacgataa", "atcgagggccgaccagtcaa", "aatttcacaacattagctgc", "taccgtgatttcgagttaat", "cgtgacggaacttgcaatgc", "gtctgcaaatggtaagagca", "agcacttgacgcgccacaac",
         "ccgcaaccacgttctaaata", "gatggcaatatgaccagctt", "tctcgtctcggtgcatagct", "tgtcggagtccggaaggcat", "cggacgtagtgtctcatgta", "aagtgcccattccaaagaat", "gcgaggctcaacttgttgtt", "atcgtgtcgacagcaacata", "ggctgcaacaccagttgaga", "tagaagcacccggcgctaat", "gcctgcctcggacgttcgtc", "actgctggagttccatcgca", "tgacaacatgccctatttct", "gcgccacctgggctgcagcg", "agctaatgtgaatgggctag"]

for i in range(0, len(X_arr)):

    #c = [[-1 for k in range(len(Y_arr[i])+1)] for l in range(len(X_arr[i])+1)]
    start = perf_counter()
    lcs(X_arr[i], Y_arr[i], len(X_arr[i]), len(Y_arr[i]))
    end = perf_counter()
    i = i+1

    arr.append(end-start)

for t in range(0, len(arr)):
    print(arr[t])

a = np.array(arr)
print("std:", np.std(a))

print("mean:", np.mean(a))
print(len(arr))

# lX = len(X)
# lY = len(Y)
# # uncomment the next line to initialize c (for memoization)
# #c = [[-1 for k in range(lY+1)] for l in range(lX+1)]
# print("Length of LCS is ", lcs(X, Y, lX, lY))

# end = perf_counter()
# print("time passed: ", end-start)
