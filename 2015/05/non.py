import time 
start = time.time()

def part_one():
    with open("non.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    count = 0

    for line in lines:
        if three_vowels(line) and double_char(line) and not ("ab" in line or "cd" in line or "pq" in line or "xy" in line):
            count += 1 

    return count 

def three_vowels(line):
    count = 0 
    vowels = "aeiou"

    for char in line:
        if char in vowels:
            count += 1 

    return count >= 3

def double_char(line):
    last = ""
    for char in line:
        if char == last:
            return True 
        last = char 

    return False 

def part_two():
    with open("non.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    count = 0 
    for line in lines:
        print(double_repeat(line))
        print(repeat_with_inbetween(line))
        if double_repeat(line) and repeat_with_inbetween(line):
            count += 1 

    return count 

def double_repeat(line):
    for i in range(len(line) - 2):
        if line[i:i+2] in line[i+2:]:
            return True 

    return False


def repeat_with_inbetween(line):
    for i in range(len(line) - 2):
        if line[i] == line[i+2]:
            return True 
    
    return False


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
