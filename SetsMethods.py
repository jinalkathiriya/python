# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)

# cities.update(cities2)
# print(cities)

# cities3 = cities.intersection(cities2)
# print(cities3)

# cities.intersection_update(cities2)

# cities3 = cities.symmetric_difference(cities2)

# cities.symmetric_difference_update(cities2)

# cities3 = cities.difference(cities2)
# print(cities.difference(cities2))

# print(cities.isdisjoint(cities2))

# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))

# print(cities2.issubset(cities))

# cities.add("Helsinki")
# print(cities)

# cities.update(cities2)
# print(cities)

# cities.remove("Tokyo")
# print(cities)

# item = cities.pop()
# print(cities)
# print(item)

# del cities
# print(cities)

# cities.clear()
# print(cities)


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")