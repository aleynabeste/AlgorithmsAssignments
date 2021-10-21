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

    printSolution(dist,  numberOfVertices)

    if dist[source][targetBusTrainStations[0]] <= dist[source][targetBusTrainStations[1]]:  # bus option is better

        return [dist[source][targetBusTrainStations[0]], "bus"]
    else:
        arrivalPoint = targetBusTrainStations[1]  # train is better

        return [dist[source][targetBusTrainStations[1]], "train"]


def printSolution(dist, numberOfVertices):
    print("Following matrix shows the shortest distances:")
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


def makediagonalzero(mat, n, m):

    for i in range(n):
        for j in range(m):

            # right and left diagonal condition
            if i == j:
                mat[i][j] = 0


if __name__ == '__main__':

    runtimes = []
    city_amounts = [10, 20, 30, 40, 50]

    for i in city_amounts:
        numberOfCities = i
        numberOfVertices = 2*numberOfCities

        distanceMatrix = [[random.randint(1, 50) for i in range(
            numberOfVertices)] for j in range(numberOfVertices)]

        makediagonalzero(distanceMatrix, numberOfVertices, numberOfVertices)

        destinadedCity = len(distanceMatrix[0])//2
        destinatedStations = [2*(destinadedCity-1), 2*(destinadedCity-1)+1]

        sourceNode = 0  # ıst-bus
        printSolution(distanceMatrix, numberOfVertices)

        start = time.time()
        resultt = floydWarshall(
            distanceMatrix, numberOfVertices, sourceNode, destinatedStations)
        end = time.time()
        runtime = end-start
        runtimes.append(runtime)

        print("Total minimum cost to target city", destinadedCity,
              "from Istanbul is ", resultt[0], " by arriving at ", resultt[1], "station of the target city")

    plt.plot(city_amounts, runtimes, linewidth=3.0)
    plt.xlabel('Number of Cities')
    plt.ylabel('runtimes Dynamic Programming Algorithm')
    plt.show()
