# Katie Fournier
# CS 162 Spring 2025
# Week 03
# Shortest Path


import copy


class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, other_city, travel_cost):
        self.neighbors[other_city] = travel_cost
        if self not in other_city.neighbors:
            other_city.neighbors[self] = travel_cost

class Map:


class Route:
    def __init__(self, starting_city: City):
        self.cities = [starting_city]
        self.cost = 0

def main():
    city_names = ['Bend', 'Medford', 'K Falls', 'Reno', 'S.F']
    cities = {City(city_name) for city_name in city_names}





if __name__ == '__main__':
    main()


