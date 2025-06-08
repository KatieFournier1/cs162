# Loading Cargo (Lab 11a)
# Katie Fournier


cargo = [9, 7, 3, 4, 5]
cargo.sort(reverse=True)
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
