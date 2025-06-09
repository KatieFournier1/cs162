# Loading Cargo (Lab 11a)
# Katie Fournier


from copy import copy
from math import floor, ceil
import random

def load_trucks(cargo, truck1, truck2, truck1_max, truck2_max):
    if len(cargo) == 0:
        # There's nothing left to load.
        return (truck1, truck2)
    for i in range(len(cargo)):
        crate = cargo[i]
        for truck, truck_max in zip([truck1, truck2], [truck1_max, truck2_max]):
            if crate + sum(truck) <= truck_max:
                # We can fit this crate on this truck, so load it.
                truck.append(crate)
                updated_cargo = copy(cargo)
                updated_cargo.pop(i)
                # Load the rest of the crates.
                return load_trucks(updated_cargo, copy(truck1), copy(truck2),
                                   truck1_max, truck2_max)
    # We weren't able to load all of the crates.
    return (truck1, truck2)

def main():
    cargo = []
    # Get the total weight from the user.
    total_weight = 0
    while total_weight == 0:
        # Keep trying until the user enters a positive integer.
        try:
            total_weight = int(input("Total weight: "))
            if total_weight < 1:
                print("Must enter an integer greater than 0.")
                total_weight = 0
        except ValueError:
            print("Must enter an integer.")
            total_weight = 0

    # Make sure that the the sum of the capacity of the two trucks is equal to
    # the total weight, even or odd. 
    max_crate_weight = ceil(total_weight / 2)
    truck1_max = max_crate_weight
    # truck2_max is either equal to truck1_max if total_weight is even, or it's
    # one less if it's odd.
    truck2_max = floor(total_weight / 2)

    # Create the random list of crates that sum up to total_weight.
    while (sum(cargo) < total_weight):
        # Avoid creating any crates that can't be loaded by either truck.
        if truck1_max in cargo:
            # The second truck might have a lower capacity.
            max_crate_weight = truck2_max
        crate = random.randint(1, min(max_crate_weight, total_weight - sum(cargo)))
        cargo.append(crate)
    print (cargo, sum(cargo))
    # Always load the largest crates first to maximize what can be loaded.
    cargo.sort(reverse=True)

    # Load the trucks
    truck1, truck2 = load_trucks(cargo, [], [], truck1_max, truck2_max)
    for truck in [truck1, truck2]:
        print (truck, "has a sum of", sum(truck))

if __name__ == "__main__":
    main()
