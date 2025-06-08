# Loading Cargo (Lab 11a)
# Katie Fournier


from copy import copy
import random

def load_trucks(cargo, truck1, truck2):
    if len(cargo) == 0:
        return (truck1, truck2)
    for i in range(len(cargo)):
        crate = cargo[i]
        for truck in [truck1, truck2]:
            if crate + sum(truck) <= 14:
                truck.append(crate)
                updated_cargo = copy(cargo)
                updated_cargo.pop(i)
                return load_trucks(updated_cargo, copy(truck1), copy(truck2))
    return (truck1, truck2)

def main():
    cargo = []
    while (sum(cargo) < 28):
        crate = random.randint(1, min(14, 28 - sum(cargo)))
        cargo.append(crate)
    print (cargo, sum(cargo))

    cargo.sort(reverse=True)
    truck1, truck2 = load_trucks(cargo, [], [])
    for truck in [truck1, truck2]:
        print (truck, "has a sum of", sum(truck))

if __name__ == "__main__":
    main()
