# Katie Fournier
# CS 162 Spring 2025
# Week 03
# Shortest Path


import copy


class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, other_city, weight):
        self.neighbors[other_city] = weight
        if self not in other_city.neighbors:
            other_city.neighbors[self] = weight


def main():
    paths = [(neighbor, neighbors[neighbor]) in neighbors]
    for path in paths:
        # TODO: implement
        pass


if __name__ == '__main__':
    main()


