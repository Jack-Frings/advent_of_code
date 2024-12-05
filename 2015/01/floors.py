def part_one():
    with open("floors.txt") as file:
        lines = list(file.readlines())
    floor = 0
    for line in lines:
        for char in line:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1 
    return floor

def part_two():
    with open("floors.txt") as file:
        lines = list(file.readlines())
    floor = 0
    for line in lines:
        for index, char in enumerate(line):
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1 
            if floor == -1:
                return index + 1

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
