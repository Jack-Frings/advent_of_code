import time 
start = time.time()

def part_one():
    with open("forklifts.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    sum = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            count = 0
            if char == "@":
                # Top
                if y > 0 and x > 0:
                    if lines[y-1][x-1] == "@": count += 1 
                if y > 0:
                    if lines[y-1][x] == "@": count += 1 
                if y > 0 and x < len(line) - 1:
                    if lines[y-1][x+1] == "@": count += 1 
                # Center 
                if x > 0:
                    if lines[y][x-1] == "@": count += 1 
                if x < len(line) - 1:
                    if lines[y][x+1] == "@": count += 1 
                # Bottom 
                if y < len(lines) - 1 and x > 0:
                    if lines[y+1][x-1] == "@": count += 1 
                if y < len(lines) - 1:
                    if lines[y+1][x] == "@": count += 1 
                if y < len(lines) - 1 and x < len(line) - 1:
                    if lines[y+1][x+1] == "@": count += 1 

                if count < 4:
                    sum += 1 
    return sum



def part_two():
    with open("forklifts.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    sum = 0
    change = True 

    while change:
        change = False
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                count = 0
                line = lines[y]
                char = line[x]

                if char == "@":
                    # Top
                    if y > 0 and x > 0:
                        if lines[y-1][x-1] == "@": count += 1 
                    if y > 0:
                        if lines[y-1][x] == "@": count += 1 
                    if y > 0 and x < len(line) - 1:
                        if lines[y-1][x+1] == "@": count += 1 
                    # Center 
                    if x > 0:
                        if lines[y][x-1] == "@": count += 1 
                    if x < len(line) - 1:
                        if lines[y][x+1] == "@": count += 1 
                    # Bottom 
                    if y < len(lines) - 1 and x > 0:
                        if lines[y+1][x-1] == "@": count += 1 
                    if y < len(lines) - 1:
                        if lines[y+1][x] == "@": count += 1 
                    if y < len(lines) - 1 and x < len(line) - 1:
                        if lines[y+1][x+1] == "@": count += 1 

                    if count < 4:
                        sum += 1 
                        lines[y] = line[:x] + "x" + line[x+1:]
                        change = True
    return sum

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
