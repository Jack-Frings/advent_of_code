import time 
start = time.time()

def part_one():
    with open("jolts.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    sum = 0

    for line in lines:
        line = [int(char) for char in line]
        first_val = max(line[:len(line)-1])
        first_index = line.index(first_val)

        second_val = max(line[first_index+1:])

        sum += int(str(first_val) + str(second_val))

    return sum

def part_two():
    with open("jolts.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    sum = 0

    for line in lines:
        line = [int(char) for char in line]
        vals = ""
        start = 0
        for i in range(12):
            vals += str(max(line[start:len(line)-11+i]))
            start = line[start:].index(int(vals[i])) + 1 + start

        sum += int(vals)
        
    return sum


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
