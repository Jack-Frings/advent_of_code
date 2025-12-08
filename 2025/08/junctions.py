import time, math, sys
start = time.time()

def getDistances():
    with open("8.txt") as file:
        lines = list(file.readlines())

    global points
    points = set()

    for line in lines:
        x, y, z = line.strip("\n").split(",")
        points.add((int(x), int(y), int(z)))

    # Memorize distance values to avoid needing to recalc
    global distances
    distances = {}
    for point_a in points:
        for point_b in points:
            if point_a == point_b: continue 
            if not ((point_a, point_b) in distances.keys()) and not ((point_b, point_a) in distances.keys()):
                distances[(point_a, point_b)] = getDistance(point_a, point_b)

    # Sort the dictionary by the distance from least to greatest
    distances = dict(sorted(distances.items(), key=lambda dist: dist[1]))

def getDistance(point_a, point_b):
    x1, y1, z1 = point_a
    x2, y2, z2 = point_b 
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def part_one():
    global points 
    global distances
    keys = list(distances.keys())
    circuits = [[point] for point in points] 

    for i in range(1000):
        point_a, point_b = keys[i]

        found_a = False
        found_b = False
        for circuit in circuits:
            if not found_a and point_a in circuit:
                circuit_a = circuit 
                found_a = True 
            if not found_b and point_b in circuit:
                circuit_b = circuit 
                found_b = True 
            if found_a and found_b:
                break

        if circuit_a == circuit_b: continue 

        circuits.remove(circuit_a)
        circuits.remove(circuit_b)
        circuits.append(circuit_a + circuit_b)

    lengths = sorted([len(circuit) for circuit in circuits], reverse=True)
    return lengths[0] * lengths[1] * lengths[2]

        
def part_two():
    global points 
    global distances
    keys = list(distances.keys())
    circuits = [[point] for point in points] 

    i = 0
    while len(circuits) > 1:
        point_a, point_b = keys[i]
        i += 1

        found_a = False
        found_b = False
        for circuit in circuits:
            if not found_a and point_a in circuit:
                circuit_a = circuit 
                found_a = True 
            if not found_b and point_b in circuit:
                circuit_b = circuit 
                found_b = True 
            if found_a and found_b:
                break

        if circuit_a == circuit_b: continue 

        circuits.remove(circuit_a)
        circuits.remove(circuit_b)
        circuits.append(circuit_a + circuit_b)

    x1, y1, z1 = point_a
    x2, y2, z2 = point_b

    return x1*x2


if __name__ == "__main__":
    getDistances()
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
