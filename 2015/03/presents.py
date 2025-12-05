import time 
start = time.time()

def part_one():
    with open("presents.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    line = lines[0] 

    x = 0 
    y = 0
    sum = 1

    positions = set()
    positions.add((x, y))

    for char in line:
        if char == "^":
            y -= 1 
        elif char == "v":
            y += 1 
        elif char == "<":
            x -= 1 
        elif char == ">":
            x += 1

        if (x, y) not in positions:
            sum += 1 
            positions.add((x, y))

    return sum

def part_two():
    with open("presents.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    line = lines[0] 

    x = 0 
    y = 0 

    robo_x = 0 
    robo_y = 0 

    counter = 0
    sum = 1 
    positions = set() 
    positions.add((0, 0))

    for char in line:
        if counter % 2 == 0:
            if char == "^":
                y -= 1 
            elif char == "v":
                y += 1 
            elif char == "<":
                x -= 1 
            elif char == ">":
                x += 1

            if (x, y) not in positions:
                sum += 1 
                positions.add((x, y))

        else:
            if char == "^":
                robo_y -= 1 
            elif char == "v":
                robo_y += 1 
            elif char == "<":
                robo_x -= 1 
            elif char == ">":
                robo_x += 1

            if (robo_x, robo_y) not in positions:
                sum += 1 
                positions.add((robo_x, robo_y))

        counter += 1

    return sum

        

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
