import time 
start = time.time()

def part_one():
    global lines 
    with open("hiking.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    global ends
    
    total = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "0":
                ends = set()
                find_trails(x, y, 1)
                total += len(ends)

    return total

def find_trails(x, y, num):
    look_for = str(num)

    if num == 10:
        global ends
        ends.add(tuple((x, y)))
        return
    
    if y > 0:
        if look_for == lines[y-1][x]:
            find_trails(x, y-1, int(num)+1)

    if y < len(lines) - 1:
        if look_for == lines[y+1][x]:
            find_trails(x, y+1, int(num)+1)

    if x > 0:
        if look_for == lines[y][x-1]:
            find_trails(x-1, y, int(num)+1)

    if x < len(lines)-1:
        if look_for == lines[y][x+1]:
            find_trails(x+1, y, int(num)+1)

def part_two():
    global lines 
    with open("hiking.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    global total
    total = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "0":
                find_all_trails(x, y, 1)

    return total

def find_all_trails(x, y, num):
    look_for = str(num)

    if num == 10:
        global total
        total += 1
        return
    
    if y > 0:
        if look_for == lines[y-1][x]:
            find_all_trails(x, y-1, int(num)+1)

    if y < len(lines) - 1:
        if look_for == lines[y+1][x]:
            find_all_trails(x, y+1, int(num)+1)

    if x > 0:
        if look_for == lines[y][x-1]:
            find_all_trails(x-1, y, int(num)+1)

    if x < len(lines)-1:
        if look_for == lines[y][x+1]:
            find_all_trails(x+1, y, int(num)+1)


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
