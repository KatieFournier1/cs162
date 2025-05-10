# Katie Fournier
# CS 162 Spring 2025
# Week 03
# Shortest Path


# Allows us to use a class as a type hint in its own function definitions.
from __future__ import annotations


class City:
    """A City has a name and zero or more connections to its neighbors. Each
    neighbor connection has an associated travel cost.
    """

    def __init__(self, name):
        self.__name = name
        self.__neighbors = []
        self.__neighbor_travel_costs = []

    def add_neighbor(self, city: City, travel_cost: int) -> None:
        self.__neighbors += [city]
        self.__neighbor_travel_costs += [travel_cost]

    def name(self) -> str:
        return self.__name

    def neighbors(self) -> list[City]:
        return self.__neighbors

    def neighbor_travel_costs(self) -> list[str]:
        return self.__neighbor_travel_costs

    def __repr__(self):
        return self.name()


def init_cities(city_names: list[str], region_travel_costs: list[list[int]]) -> set[City]:
    """Creates a set of City objects. Each City is given pointers to their neighbor
    cities according to the given weighted adjacency matrix.
    """

    cities = {City(name) for name in city_names}
    # Assign each city its neighbors.
    for city, neighbor_travel_costs in zip(cities, region_travel_costs):
        for neighbor_name, neighbor_travel_cost in zip(city_names, neighbor_travel_costs):
            # There is a direct connection between these two cities.
            if neighbor_travel_cost != 0:
                city.add_neighbor(get_city(cities, neighbor_name), neighbor_travel_cost)
    return cities


def get_city(cities: set[City], city_name: str) -> City:
    """Returns the City object with the given name from a set of City objects."""

    for city in cities:
        if city.name() == city_name:
            return city


def find_routes(current_city: City, target_city: City,
                visited_cities: list[City] = [], total_travel_cost: int = 0) \
        -> list[list[City]]:
    """Recursively find all routes from one city to another."""

    # If we've reached the target city, we're done.
    if current_city is target_city:
        return [{'cities': [city for city in visited_cities] + [current_city], 'cost': total_travel_cost}]

    # Otherwise, for each neighbor, find all paths to target_city that visit that neighbor next.
    routes = []
    for neighbor_city, neighbor_travel_cost in \
            zip(current_city.neighbors(), current_city.neighbor_travel_costs()):
        # A city can only be visited once.
        if neighbor_city not in visited_cities:
            routes += find_routes(neighbor_city, target_city,
                                  [city for city in visited_cities] + [current_city],
                                  total_travel_cost + neighbor_travel_cost)
    return routeS


def main():
    city_names = ['Bend', 'Medford', 'Klamath Falls', 'Reno', 'San Francisco']
    travel_costs = [[0,  50,  40,  0,   0  ],
                    [50, 0,   0,   0,   200],
                    [40, 0,   0,   130, 175],
                    [0,  0,   130, 0,   180],
                    [0,  200, 175, 180, 0  ]]
    # Create a list of City objects.
    cities = init_cities(city_names, travel_costs)

    # Create a list of all valid routes between Bend and SF.
    bend = get_city(cities, 'Bend')
    san_francisco = get_city(cities, 'San Francisco')
    routes = find_routes(bend, san_francisco)

    # Find the cheapest route.
    route_costs = [route['cost'] for route in routes]
    lowest_cost = min(route_costs)
    cheapest_route = routes[route_costs.index(lowest_cost)]

    # Print the results.
    print("VALID ROUTES:")
    for route in routes:
        print(f"{route['cities']}, Cost = {route['cost']}")
    print((f"\nCHEAPEST:\n"
           f"Route taken: {', '.join(map(lambda city: city.name(), route['cities']))}\n"
           f"Total travel cost: {lowest_cost}"))


if __name__ == '__main__':
    main()


