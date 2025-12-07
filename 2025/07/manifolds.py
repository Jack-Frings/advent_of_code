import time, copy
start = time.time()

def part_one():
    with open("manifolds.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    # Initialize frontier at starting position 
    frontier = set()
    frontier.add((0, lines[0].index("S")))
    splits = set()

    while len(frontier) > 0:
        y, x = frontier.pop()
        if (lines[y][x] == "." or lines[y][x] == "S") and y < len(lines) - 1:
            frontier.add((y+1, x))

        if lines[y][x] == "^":
            splits.add((y, x))
            frontier.add((y, x-1))
            frontier.add((y, x+1))

    return len(splits)

def part_two():
    with open("manifolds.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    length = len(lines)

    x = lines[0].index("S")
    for y in range(length):
        if lines[y][x] == "^":
            break 

    start = (y, x)
    frontier = set()
    frontier.add(start)

    history = set()

    global choices 
    choices = {}

    while len(frontier) > 0:
        point = frontier.pop()
        y, x = point
        history.add(point)

        results = []
        for x_delta in [-1, 1]:
            new_x = x + x_delta
            for new_y in range(y, length):
                if lines[new_y][new_x] == "^":
                    results.append((new_y, new_x))
                    if (new_y, new_x) not in history:
                        frontier.add((new_y, new_x))
                    break 


        if len(results) == 0:
            results.append(1)
        if len(results) == 1:
            results.append(1)

        choices[point] = results

    return getTimelines(start)

    
def getTimelines(point):
    global choices 
    total = 0 
    
    for val in choices[point]:
        if type(val) == int:
            total += val
        else:
            total += getTimelines(val)
    
    choices[point] = [total]
    return total

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
