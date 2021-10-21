# ALEYNA BESTE OZHAN
import random
import sys
import matplotlib.pyplot as plt
import time
from tourist_problem_class import TouristProblem


'''
Update matrix's diagonal as 0 since shortest path between any s & s = 0 
'''

INF = 10000  # put that value for the edges that are not connected in the real life


def makediagonalzero(matrix, n):

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0

    return matrix


def printSolution(dist, numberOfVertices):
    print("distance matrix")
    for i in range(numberOfVertices):
        str = ""
        for j in range(numberOfVertices):
            if dist[i][j] == INF:
                str += ("%7s" % "INF")
            else:
                str += ("%7d\t" % (dist[i][j]))
            if j == numberOfVertices - 1:
                str += ""
        print(str)


def main():

    # Define matrix

    distance_matrix = [[0, 5, 7,  45],
                       [34, 0, 1, 6],
                       [56, 7, 0, 87],
                       [34, 2, 21, 0]]

    # distance_matrix = [[100, 2, 10, 56, 107, 77],
    #                    [50, 100, 5, 56, 56, 56],
    #                    [21, 100, 100, 56, 5, 56],
    #                    [50, 50, 50, 100, 56, 56],
    #                    [2, 3, 1, 56, 100, 56],
    #                    [50, 50, 50, 56, 56, 100]]

    # distance_matrix = [[0, 10], [2, 0]]

    # distance_matrix = [[INF, INF, INF, INF, INF, INF],
    #                    [INF, INF, INF, INF, INF, INF],
    #                    [INF, INF, INF, INF, INF, INF],
    #                    [INF, INF, INF, INF, INF, INF],
    #                    [INF, INF, INF, INF, INF, INF],
    #                    [INF, INF, INF, INF, INF, INF]
    #                    ]

    # distance_matrix = [[]]

    # distance_matrix = [[0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0],
    #                    [0, 0, 0, 0, 0, 0]
    #                    ]

    # distance_matrix = [[random.randint(1, 25) for i in range(
    #     8)] for j in range(8)]

    distance_matrix = makediagonalzero(
        distance_matrix, len(distance_matrix[0]))

    printSolution(distance_matrix, len(distance_matrix[0]))
    start_station = 0  # Bus station in Istanbul
    target_city = len(distance_matrix[0])//2
    target_stations = [2*(target_city-1), 2*(target_city-1)+1]

    tourist_problem = TouristProblem(
        distance_matrix, start_station, target_stations)

    start = time.time()
    resultt = tourist_problem.minimum_cost()
    end = time.time()
    if resultt[0] == INF:
        print("there is no path from Istanbul-Harem bus statıon to", target_city)
    elif len(distance_matrix[0]) == 0:
        print("empty matrix")
    else:
        print("the quickest itinerary from Istanbul-Harem bus station to", target_city, "th city is",
              resultt[0], " by arriving at the", resultt[1], "station of the city")

    # runtime = end-start
    # runtimes.append(runtime)


if __name__ == '__main__':
    # set recursion limit to 1500
    sys.setrecursionlimit(1500)
    main()
