# Katie Fournier
# CS 162 Spring 2025
# Week 03
# Shortest Path


class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.weights = []

    def add_connection(self, city, weight):
        if city not in neighbors:
            self.neighbors.append(city)
            self.weights.append(weight)
        else:
            raise ValueError('neighbor already added')


def init_cities(city_names: [str], weights: [int]) -> {str: City}:
    n = len(city_names)
    cities = {name: City(name) for name in city_names}
    for i in range(1, n):
        city1 = city_names[i-1]
        weights = weights[i]
        for j in range(i, len(weights)):
            weight = weights[i]
            if weight ~= 0:
                city2 = city_names[j]
                cities[city1].add_connection(city2, weight)
                cities[city2].add_connection(city1, weight)
    return cities


def traverse(starting_city: City, target_city: City, cities: [City],
             routes: [[City]], total_costs: [int]):
    if routes == []:
        routes.append(starting_city)
    for route in routes:
        if route[-1] = starting_city:
            for next_city in starting_city.neighbors:
                # TODO: complete
                pass


def main():
    city_names = ['Bend', 'Medford', 'K Falls', 'Reno', 'S.F.']
    weights = [[0,  50,  40,  0,   0  ],
               [50, 0,   0,   0,   200],
               [40, 0,   0,   130, 175],
               [0,  0,   130, 0,   180],
               [0,  200, 175, 180, 0  ]]
    cities = init_cities(city_names, weights)
    routes = []


if __name__ == '__main__':
    main()


