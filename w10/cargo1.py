# Loading Cargo (Lab 11a)
# Katie Fournier


from copy import copy


def load_trucks(cargo, truck1, truck2):
    if len(cargo) == 0:
        return (truck1, truck2)
    for crate in cargo:
        for truck in [truck1, truck2]:
            if crate + sum(truck) <= 14:
                truck.append(crate)
                new_truck1, new_truck2 = load_trucks(cargo[1:], copy(truck1), copy(truck2))
                if sum(new_truck1) == 14 and sum(new_truck2) == 14:
                    return (new_truck1, new_truck2)
    return ([], [])


def main():
    cargo = [9, 7, 3, 4, 5]
    print (cargo, "has a sum of" , sum(cargo))
    cargo.sort(reverse=True)
    truck1, truck2 = load_trucks(cargo, [], [])
    for truck in [truck1, truck2]:
        print (truck, "has a sum of", sum(truck))


if __name__ == "__main__":
    main()


