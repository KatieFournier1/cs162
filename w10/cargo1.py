# Loading Cargo (Lab 11a)
# Katie Fournier


# cargo = [9, 7, 3, 4, 5]
# cargo = [1, 2, 13, 12]
# cargo = [7, 6, 5, 4, 3, 2, 1]
cargo = [1, 2, 3, 4, 5, 6, 7]
print (cargo, "has a sum of" , sum(cargo))
truck1 = []
truck2 = []
for crate in cargo:
    print (crate)
    for truck in [truck1, truck2]:
        if crate + sum(truck) <= 14:
            truck.append(crate)
            break
for truck in [truck1, truck2]:
    print (truck, "has a sum of", sum(truck))
