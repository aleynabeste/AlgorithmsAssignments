# ALEYNA BESTE OZHAN
class TouristProblem:

    def __init__(self, matrix, start_station, targetBusTrainStations):
        self.matrix = matrix
        self.start_station = start_station
        self.targetBusTrainStations = targetBusTrainStations

    '''
    This function calculates the shortest path betwween starting city "s" and target city "t"
    '''

    def shortest_path_recursive(self, s, t):
        if len(self.matrix) < 3:  # for case of 0 city and 1 city
            return 0
        elif s == t:
            return self.matrix[s][t]

        min = self.matrix[s][t]
        for i in range(s+1, t):
            c = self.shortest_path_recursive(s, i) + self.matrix[i][t]
            if c < min:
                min = c
        return min

    '''
    This function returns the minimum cost to reach targetstations from startStation 
    '''

    def minimum_cost(self):

        # ends up at the bus station
        path_ending_at_bus = self.shortest_path_recursive(
            self.start_station, self.targetBusTrainStations[0])
        # ends up at the train station
        path_ending_at_train = self.shortest_path_recursive(
            self.start_station, self.targetBusTrainStations[1])
        if path_ending_at_bus <= path_ending_at_train:

            return [path_ending_at_bus, "bus"]
        else:

            return [path_ending_at_train, "train"]
