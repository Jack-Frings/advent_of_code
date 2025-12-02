import re
import time 
start = time.time()

def part_one():
    with open("id.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    line = lines[0]

    id_bounds = line.split(",")
    sum = 0

    regex = re.compile(r'^(\d*)\1$')

    for id_bound in id_bounds:
        from_bound, to_bound = id_bound.split("-")
        for id in range(int(from_bound), int(to_bound) + 1):
            if regex.match(str(id)):
                sum += id 

    return sum

def part_two():
    with open("id.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    line = lines[0]

    id_bounds = line.split(",")
    sum = 0

    regex = re.compile(r'^(\d*)\1+$')

    for id_bound in id_bounds:
        from_bound, to_bound = id_bound.split("-")
        for id in range(int(from_bound), int(to_bound) + 1):
            if regex.match(str(id)):
                sum += id 

    return sum

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
