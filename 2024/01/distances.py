import time 
start_time = time.time()

def part_one():
    with open("distances.txt") as file:
        lines = list(file.readlines())
    for index, line in enumerate(lines):
        lines[index] = line.strip("\n")
    
    left = []
    right = []
    diff = 0

    for line in lines:
        a, b = line.split("   ")
        left.append(int(a))
        right.append(int(b))
    
    left = sorted(left)
    right = sorted(right)

    for left_val, right_val in zip(left, right):
        diff += abs(left_val - right_val)

    return diff

def part_two():
    with open("distances.txt") as file:
        lines = list(file.readlines())
    for index, line in enumerate(lines):
        lines[index] = line.strip("\n")

    left = []
    right = []
    diff = 0

    for line in lines:
        a, b = line.split("   ")
        left.append(int(a))
        right.append(int(b))

    for left_val in left:
        freq = 0
        for right_val in right:
            if left_val == right_val:
                freq += 1
        diff += left_val*freq 

    return diff
    


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")

    end_time = time.time()
    print(f"Execution Time: {end_time - start_time}")
