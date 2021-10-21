# I mostly took the code from here: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
# ALEYNA BESTE OZHAN
import random
import sys
import matplotlib.pyplot as plt
import time

INF = 10000  # put that value for the edges that are not connected in the real life


def floydWarshall(graph, numberOfVertices, source, targetBusTrainStations):

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    # We initialize the solution matrix same as the input graph matrix as a first step
    # dist[][] will be the output matrix that will finally  have the shortest distances between every pair of vertices

    for k in range(numberOfVertices):  # intermediate vertices,
        # The idea is to one by one pick all vertices and
        # updates all shortest paths which include the picked vertex as an intermediate vertex in the shortest path
        for i in range(numberOfVertices):   # pick all city station as source one by one

            # pick all city stations as destination for the kth city
            for j in range(numberOfVertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
    print("Following matrix shows the shortest distances:")
    printSolution(dist,  numberOfVertices)

    if(numberOfVertices == 0):
        return [0]

    elif dist[source][targetBusTrainStations[0]] <= dist[source][targetBusTrainStations[1]]:  # bus option is better

        return [dist[source][targetBusTrainStations[0]], "bus"]
    else:
        arrivalPoint = targetBusTrainStations[1]  # train is better

        return [dist[source][targetBusTrainStations[1]], "train"]


def printSolution(dist, numberOfVertices):
    print("")
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


def makediagonalzero(mat, n):

    for i in range(n):
        for j in range(n):

            # right and left diagonal condition
            if i == j:
                mat[i][j] = 0


if __name__ == '__main__':

    # distanceMatrix = [[random.randint(1, 50) for i in range(
    #     8)] for j in range(8)]

    # distanceMatrix = [[INF, INF, INF, INF, INF, INF],
    #                   [INF, INF, INF, INF, INF, INF],
    #                   [INF, INF, INF, INF, INF, INF],
    #                   [INF, INF, INF, INF, INF, INF],
    #                   [INF, INF, INF, INF, INF, INF],
    #                   [INF, INF, INF, INF, INF, INF]
    #                   ]

    # distanceMatrix = [[0, 10], [2, 0]]

    # distanceMatrix = [[100, 2, 10, 56, 107, 77],
    #                   [50, 100, 5, 56, 56, 56],
    #                   [21, 100, 100, 56, 5, 56],
    #                   [50, 50, 50, 100, 56, 56],
    #                   [2, 3, 1, 56, 100, 56],
    #                   [50, 50, 50, 56, 56, 100]]

    # distanceMatrix = [[]]

    # distanceMatrix = [[0, 0, 0, 0, 0, 0],
    #                   [0, 0, 0, 0, 0, 0],
    #                   [0, 0, 0, 0, 0, 0],
    #                   [0, 0, 0, 0, 0, 0],
    #                   [0, 0, 0, 0, 0, 0],
    #                   [0, 0, 0, 0, 0, 0]
    #                   ]

    distanceMatrix = [[0, 5, 7,  45],
                      [34, 0, 1, 6],
                      [56, 7, 0, 87],
                      [34, 2, 21, 0]]

    makediagonalzero(distanceMatrix, len(distanceMatrix[0]))

    destinadedCity = len(distanceMatrix[0])//2
    destinatedStations = [2*(destinadedCity-1), 2*(destinadedCity-1)+1]

    sourceNode = 0  # ıst-bus
    print("initial matrix")
    printSolution(distanceMatrix, len(distanceMatrix[0]))

    resultt = floydWarshall(
        distanceMatrix, len(distanceMatrix[0]), sourceNode, destinatedStations)

    if len(resultt) == 1:
        print("empty matrix")

    elif resultt[0] == INF:
        print("there is no path from source to target city", destinadedCity)
    else:
        print("the quickest itinerary from Istanbul-Harem bus station to", destinadedCity, "th city is",
              resultt[0], " by arriving at the", resultt[1], "station of the city")
