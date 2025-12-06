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

    # Find gaps 
    gaps = []
    for x in range(len(lines[0])):
        gap = True 
        for line in lines:
            if line[x] != " ":
                gap = False 
                break

        if gap:
            gaps.append(x)

    # Separate the lines by the gaps into a 2D array of numbers with the whitespace still included
    new_lines = []

    for line in lines:
        new_line = []
        start  = 0
        for gap in gaps:
            new_line.append(line[start:gap])
            start = gap + 1
        new_line.append(line[start:])
        new_lines.append(new_line)

    # Iterate through to sum and product

    total = 0 
    for i in range(len(new_lines[0])):
        operation = new_lines[len(new_lines)-1][i].strip()

        nums = set()

        # I know this longest iteration sucks but I do not care enough to change it.
        longest = 0 
        for line in range(len(new_lines)-1):
            if len(new_lines[line][i]) > longest:
                longest = len(new_lines[line][i])

        for char in range(longest):
            num = ""
            for line in range(len(new_lines)-1):
                if new_lines[line][i][char] != " ":
                    num += new_lines[line][i][char] 
            nums.add(int(num))


        if operation == "+":
            sum = 0
            for num in nums:
                sum += num 

        elif operation == "*":
            sum = 1
            for num in nums:
                sum *= num

        total += sum

    return total   

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
