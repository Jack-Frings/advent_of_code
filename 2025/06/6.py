import time, copy
start = time.time()

def part_one():
    with open("6.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    for i, line in enumerate(lines):
        lines[i] = line.split()

    sum = 0
    for i in range(len(lines[0])):
        operation = lines[len(lines)-1][i] 

        if operation == "+":
            num = 0
            for line in range(len(lines)-1):
                num += int(lines[line][i]) 

        elif operation == "*":
            num = 1
            for line in range(len(lines)-1):
                num *= int(lines[line][i])

        sum += num


    return sum

def part_two():
    with open("6.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    total = 0 
    stored_nums = []

    for i, line in enumerate(lines):
        lines[i] = line[::-1]

    for x in range(len(lines[0])):
        num = ""
        for y in range(len(lines)):
            char = lines[y][x]
            if char == "+":
                stored_nums.append(int(num))
                total += sum(stored_nums)
                stored_nums = []
                num = ""
            elif char == "*":
                stored_nums.append(int(num))
                total += multiply(stored_nums)
                stored_nums = []
                num = ""
            elif char == " ":
                continue
            else:
                num += char 
        if num != "": 
            stored_nums.append(int(num))

    return total

def multiply(lst):
    val = 1
    for i in lst:
        val *= i 
    return val

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
