import time 
start_time = time.time()

def part_one():
    with open("guard.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if lines[y][x] in "^v<>":
                x_pos, y_pos, direction = x, y, char
                lines[y] = lines[y][0:x] + "." + lines[y][x+1:]
                break
    
    spaces = set()

    while True:
        spaces.add(tuple((x_pos, y_pos)))
        new_y_pos = y_pos
        new_x_pos = x_pos
        if direction == "^":
            new_y_pos -= 1 
        elif direction == "v":
            new_y_pos += 1
        elif direction == "<":
            new_x_pos -= 1
        elif direction == ">":
            new_x_pos += 1
        
        try:
            if new_y_pos < 0 or new_x_pos < 0:
                raise IndexError
            if lines[new_y_pos][new_x_pos] == ".":
                y_pos = new_y_pos
                x_pos = new_x_pos
            else:
                direction = rotate(direction)
        except IndexError:
            return len(spaces)

def rotate(direction):
    if direction == "^":
        direction = ">"
    elif direction == ">":
        direction = "v"
    elif direction == "v":
        direction = "<"
    elif direction == "<":
        direction = "^"

    return direction

def part_two():
    with open("guard.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if lines[y][x] in "^v<>":
                x_pos, y_pos, direction = x, y, char
                lines[y] = lines[y][0:x] + "." + lines[y][x+1:]
                break
    
    count = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if lines[y][x] == "#" or (y == y_pos and x == x_pos):
                continue 
            elif lines[y][x] == ".":
                lines[y] = lines[y][0:x] + "#" + lines[y][x+1:]
                looped = loop_test(lines, x_pos, y_pos, direction)
                if looped:
                    count += 1
                lines[y] = lines[y][0:x] + "." + lines[y][x+1:]

    return count

def loop_test(lines, x_pos, y_pos, direction):
    spaces = set()
    sinceFoundNew = set() 

    rotated = False

    while True:
        if tuple((x_pos, y_pos)) not in spaces:
            sinceFoundNew = set()
            spaces.add(tuple((x_pos, y_pos)))
        elif tuple((x_pos, y_pos)) not in sinceFoundNew and not rotated:
            sinceFoundNew.add(tuple((x_pos, y_pos)))
        elif tuple((x_pos, y_pos)) in sinceFoundNew and not rotated:
            return True

        new_y_pos = y_pos
        new_x_pos = x_pos
        if direction == "^":
            new_y_pos -= 1 
        elif direction == "v":
            new_y_pos += 1
        elif direction == "<":
            new_x_pos -= 1
        elif direction == ">":
            new_x_pos += 1
        
        try:
            if new_y_pos < 0 or new_x_pos < 0:
                raise IndexError
            if lines[new_y_pos][new_x_pos] == ".":
                y_pos = new_y_pos
                x_pos = new_x_pos
                rotated = False
            else:
                direction = rotate(direction)
                rotated = True
        except IndexError:
            return False



if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time}")
