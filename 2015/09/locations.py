import time, copy
start = time.time()

def part_one():
    with open("9.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    locations = set()

    global distances 
    distances = {}
    
    for line in lines:
        next_locations, distance = line.split(" = ")
        location_1, location_2 = next_locations.split(" to ")

        locations.add(location_1)
        locations.add(location_2)

        if location_1 not in distances.keys():
            distances[location_1] = {}
        distances[location_1][location_2] = int(distance)

        if location_2 not in distances.keys():
            distances[location_2] = {}
        distances[location_2][location_1] = int(distance)

    min = -1
    for start in locations:
        locations_copy = copy.deepcopy(locations)
        locations_copy.remove(start)
        dist = getMinDistance(start, locations_copy, 0)
        if min == -1 or dist < min:
            min = dist

    return min

def getMinDistance(location, locations, distance_traveled):
    if len(locations) == 0:
        return 0 

    global distances 
    min_dist = -1 

    for next_location in locations:
        resulting_locations = copy.deepcopy(locations)
        resulting_locations.remove(next_location)

        if min_dist == -1:
            min_dist = distances[location][next_location] + getMinDistance(next_location, resulting_locations, distance_traveled)
        else:
            possible_dist = distances[location][next_location] + getMinDistance(next_location, resulting_locations, distance_traveled)
            if possible_dist < min_dist:
                min_dist = possible_dist

    return min_dist


def part_two():
    with open("9.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    locations = set()

    global distances 
    distances = {}
    
    for line in lines:
        next_locations, distance = line.split(" = ")
        location_1, location_2 = next_locations.split(" to ")

        locations.add(location_1)
        locations.add(location_2)

        if location_1 not in distances.keys():
            distances[location_1] = {}
        distances[location_1][location_2] = int(distance)

        if location_2 not in distances.keys():
            distances[location_2] = {}
        distances[location_2][location_1] = int(distance)

    max = -1
    for start in locations:
        locations_copy = copy.deepcopy(locations)
        locations_copy.remove(start)
        dist = getMaxDistance(start, locations_copy, 0)
        if max == -1 or dist > max:
            max = dist

    return max

def getMaxDistance(location, locations, distance_traveled):
    if len(locations) == 0:
        return 0 

    global distances 
    max_dist = -1 

    for next_location in locations:
        resulting_locations = copy.deepcopy(locations)
        resulting_locations.remove(next_location)

        if max_dist == -1:
            max_dist = distances[location][next_location] + getMaxDistance(next_location, resulting_locations, distance_traveled)
        else:
            possible_dist = distances[location][next_location] + getMaxDistance(next_location, resulting_locations, distance_traveled)
            if possible_dist > max_dist:
                max_dist = possible_dist

    return max_dist

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
