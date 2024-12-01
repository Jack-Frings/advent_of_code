def part_one():
    with open("data.txt") as file:
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
    with open("data.txt") as file:
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
    print(part_two())
