# Katie Fournier
# CS 162 Spring 2025
# Week 03
# Shortest Path


class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.neighbor_travel_costs = []

    def __repr__(self):
        return self.name


def init_cities(city_names: list[str], region_travel_costs: list[list[int]]) -> list[City]:
    """Creates a list of City objects that contain pointers to their neighbor
    cities given a weighted adjacency matrix.
    """
    cities = [City(name) for name in city_names]
    for city, neighbor_travel_costs in zip(cities, region_travel_costs):
        for neighbor_name, neighbor_travel_cost in zip(city_names, neighbor_travel_costs):
            if neighbor_travel_cost != 0:
                city.neighbors += [get_city(cities, neighbor_name)]
                city.neighbor_travel_costs += [neighbor_travel_cost]
    return cities


def get_city(cities: set[City], city_name: str) -> City:
    for city in cities:
        if city.name == city_name:
            return city


def find_routes(current_city: City,
                target_city: City,
                visited_cities: list[City] = [],
                total_travel_cost: int = 0) \
        -> list[list[City]]:
    """Recursively finds all routes from one city to another."""
    if current_city is target_city:
        return [{'cities': visited_cities + [current_city], 'cost': total_travel_cost}]
    routes = []
    for neighbor_city, neighbor_travel_cost in \
            zip(current_city.neighbors, current_city.neighbor_travel_costs):
        if neighbor_city not in visited_cities:
            routes += find_routes(neighbor_city,
                                  target_city,
                                  visited_cities + [current_city],
                                  total_travel_cost + neighbor_travel_cost)
    return routes


def main():
    city_names = ['Bend', 'Medford', 'Klamath Falls', 'Reno', 'San Francisco']
    travel_costs = [[0,  50,  40,  0,   0  ],
                    [50, 0,   0,   0,   200],
                    [40, 0,   0,   130, 175],
                    [0,  0,   130, 0,   180],
                    [0,  200, 175, 180, 0  ]]
    cities = init_cities(city_names, travel_costs)
    bend = get_city(cities, 'Bend')
    san_francisco = get_city(cities, 'San Francisco')
    routes = find_routes(bend, san_francisco)

    print("VALID ROUTES:")
    lowest_cost = None
    for route in routes:
        route_cost = route['cost']
        if (lowest_cost is None) or (min(lowest_cost, route_cost) == route_cost):
            lowest_cost = route_cost
            cheapest_route = route
        print(f"{route['cities']}, Cost = {route['cost']}")
        # print(route)
    print((f"\nCHEAPEST:\n"
           f"Route taken: {', '.join(map(lambda city: city.name, route['cities']))}\n"
           f"Total travel cost: {lowest_cost}"))


if __name__ == '__main__':
    main()


