import time 
start_time = time.time()

def part_one():
    with open("reports.txt") as file:
        lines = list(file.readlines())
    for index, line in enumerate(lines):
        lines[index] = line.strip("\n")
    
    count = 0
    for line in lines:
        safe = True
        line = list(line.split(" "))
        line = [int(val) for val in line]
        if line != sorted(line) and line != sorted(line, reverse=True):
            safe = False
        for index in range(len(line)-1):
            if not (3 >= abs(int(line[index]) - int(line[index+1])) >= 1):
                safe = False
        if safe:
            count += 1

    return count

def part_two():
    with open("reports.txt") as file:
        lines = list(file.readlines())
    for index, line in enumerate(lines):
        lines[index] = line.strip("\n")
    
    count = 0
    for line in lines:
        safe = False
        line = list(line.split(" "))
        line = [int(val) for val in line]
        for n in range(len(line)):
            test_line = line[0:n] + line[n+1:]
            if line_safe(test_line):
                safe = True
                break
        if safe:
            count += 1
    return count


def line_safe(line):
    safe = True
    if line != sorted(line) and line != sorted(line, reverse=True):
        safe = False
    for index in range(len(line)-1):
        if not (3 >= abs(int(line[index]) - int(line[index+1])) >= 1):
            safe = False
    return safe

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time}")
