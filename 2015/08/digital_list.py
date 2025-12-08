import time
start = time.time()

def part_one():
    with open("8.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    difference = 0

    for line in lines:
        difference += len(line)

        line = line[1:len(line)-1]

        while r'\\' in line:
            i = line.index(r'\\')
            line = line[:i] + r'"' + line[i+2:]

        while r'\"' in line:
            i = line.index(r'\"')
            line = line[:i] + '"' + line[i+2:] 


        while r'\x' in line:
            i = line.index(r'\x')
            line = line[:i] + "x" + line[i+4:]

        difference -= len(line)

    return difference

def part_two():
    with open("8.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    difference = 0 

    for line in lines:
        # Handle Starting quotes 
        difference += 4
        line = line[1:len(line)-1] 

        for char in line:
            if char == '"' or char == "\\":
                difference += 1

    return difference

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
