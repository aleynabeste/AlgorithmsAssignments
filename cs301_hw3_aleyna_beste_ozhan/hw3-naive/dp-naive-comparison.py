# ALEYNA BESTE OZHAN

import random
import sys
import matplotlib.pyplot as plt
import time
from tourist_problem_class import TouristProblem


'''
Update matrix's diagonal as 0 since shortest path between any s & s = 0 
'''

INF = 10000   # put that value for the edges that are not connected in the real life


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

    runtimes_naive = []
    runtimes_dp = []
    city_amounts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in city_amounts:

        distance_matrix = [[random.randint(1, 50) for i in range(
            i*2)] for j in range(i*2)]

        distance_matrix = makediagonalzero(
            distance_matrix, len(distance_matrix[0]))

        printSolution(distance_matrix, len(distance_matrix[0]))

        start_station = 0  # Bus station in Istanbul
        target_city = len(distance_matrix[0])//2
        target_stations = [2*(target_city-1), 2*(target_city-1)+1]

        tourist_problem = TouristProblem(
            distance_matrix, start_station, target_stations)

        start_naive = time.time()
        resultt = tourist_problem.minimum_cost()
        end_naive = time.time()
        print("the quickest itinerary from Istanbul-Harem bus station to", target_city, "th city is",
              resultt[0], " by arriving at the", resultt[1], "station of the city, by naive")

        runtime_n = end_naive-start_naive
        runtimes_naive.append(runtime_n)

        start_DP = time.time()
        result_dp = floydWarshall(
            distance_matrix, i*2, start_station, target_stations)
        end_DP = time.time()
        print("the quickest itinerary from Istanbul-Harem bus station to", target_city, "th city is",
              result_dp[0], " by arriving at the", result_dp[1], "station of the city, by dp")

        runtime_dp = end_DP-start_DP
        runtimes_dp.append(runtime_dp)

    plt.plot(city_amounts, runtimes_naive, linewidth=1.0)
    plt.plot(city_amounts, runtimes_dp, linewidth=1.0)
    plt.xlabel('Number of Cities')
    plt.ylabel('runtime (s)')
    plt.legend(['Naive Recursive', 'DP-Memoization'], loc='upper left')
    plt.show()


if __name__ == '__main__':
    # set recursion limit to 1500
    sys.setrecursionlimit(1500)
    main()
