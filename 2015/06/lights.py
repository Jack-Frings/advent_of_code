import time, copy
start = time.time()

def part_one():
    with open("6.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    row = [] 
    for _ in range(1000):
        row.append(False)

    lights = []
    for _ in range(1000):
        lights.append(copy.deepcopy(row))

    for line in lines:
        line = line.split(" ")
        if line[0] == "turn": # Remove "turn" if in phrase
            line.pop(0) 
        line.pop(2) # Remove "through"

        start = [int(i) for i in line[1].split(",")]
        end = [int(i) for i in line[2].split(",")]

        for y in range(start[1], end[1] + 1):
            for x in range(start[0], end[0] + 1):
                if line[0] == "on": lights[y][x] = True 
                elif line[0] == "off": lights[y][x] = False 
                elif line[0] == "toggle": lights[y][x] = not lights[y][x]

    total = 0
    for row in lights:
        for val in row:
            total += val 

    return total


def part_two():
    with open("6.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    row = [] 
    for _ in range(1000):
        row.append(0)

    lights = []
    for _ in range(1000):
        lights.append(copy.deepcopy(row))

    for line in lines:
        line = line.split(" ")
        if line[0] == "turn": # Remove "turn" if in phrase
            line.pop(0) 
        line.pop(2) # Remove "through"

        start = [int(i) for i in line[1].split(",")]
        end = [int(i) for i in line[2].split(",")]

        for y in range(start[1], end[1] + 1):
            for x in range(start[0], end[0] + 1):
                if line[0] == "on": lights[y][x] += 1
                elif line[0] == "off" and lights[y][x] > 0: lights[y][x] -= 1
                elif line[0] == "toggle": lights[y][x] += 2

    total = 0
    for row in lights:
        for val in row:
            total += val 

    return total

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
