import time 
start = time.time()

def part_one():
    with open("dials.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
   
    val = 50
    count = 0

    for line in lines:
        direction = line[0]
        magnitude = int(line[1:])
        if direction == "L":
            val -= magnitude
            while val < 0: val += 100 

        elif direction == "R":
            val += magnitude
            while val >= 100: val -= 100 

        if val == 0:
            count += 1

    return count


def part_two():
    with open("dials.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
   
    val = 50
    count = 0

    for line in lines:
        direction = line[0]
        magnitude = int(line[1:])
        if direction == "L":
            for i in range(magnitude):
                val -= 1 
                if val < 0: val += 100 
                if val == 0: count += 1

        elif direction == "R":
            for i in range(magnitude):
                val += 1 
                if val >= 100: val -= 100 
                if val == 0: count += 1

    return count

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
