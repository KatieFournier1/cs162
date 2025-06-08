# Loading Cargo (Lab 11a)
# Katie Fournier


from copy import copy
import random

print(random.randint(1,28))

def load_trucks(cargo, truck1, truck2):
    if len(cargo) == 0:
        return (truck1, truck2)
    for crate in cargo:
        for truck in [truck1, truck2]:
            if crate + sum(truck) <= 14:
                truck.append(crate)
                truck1, truck2 = load_trucks(cargo[1:], copy(truck1), copy(truck2))
                if sum(truck1) == 14 and sum(truck2) == 14:
                    return (truck1, truck2)
    return (truck1, truck2)

def main():
    cargo = []
    while (sum(cargo) < 28):
        crate = random.randint(1, 28)
        cargo.append(crate)
    print (cargo, sum(cargo))
    cargo.sort(reverse=True)
    truck1, truck2 = load_trucks(cargo, [], [])
    for truck in [truck1, truck2]:
        print (truck, "has a sum of", sum(truck))

if __name__ == "__main__":
    main()
