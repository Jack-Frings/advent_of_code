import time 
start_time = time.time()

def part_one():
    with open("day7.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    
    total = 0
    global all

    for line in lines:
        result, nums = line.split(": ")
        result = int(result)

        nums = nums = list(map(int, (num for num in nums.split(" "))))
        length = len(nums)-1

        all = set()
        get_operators("", length)
        
        for operators in all:
            cur_val = nums[0]
            for i, num in enumerate(nums):
                if i == 0:
                    continue
                if operators[i-1] == "+":
                    cur_val += num 
                elif operators[i-1] == "*":
                    cur_val *= num
            if cur_val == result:
                total += result 
                break

    return total

def get_operators(operators, num_of_operators):
    if len(operators) == num_of_operators:
        all.add(operators)
        return

    add = get_operators(operators+"+", num_of_operators)
    mult = get_operators(operators+"*", num_of_operators)

def part_two():
    with open("day7.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    
    total = 0
    global all

    for line in lines:
        result, nums = line.split(": ")
        result = int(result)

        nums = nums = list(map(int, (num for num in nums.split(" "))))
        length = len(nums)-1

        all = set()
        get_operators_with_concatenation("", length)
        
        for operators in all:
            cur_val = nums[0]
            for i, num in enumerate(nums):
                if i == 0:
                    continue
                if operators[i-1] == "+":
                    cur_val += num 
                elif operators[i-1] == "*":
                    cur_val *= num
                elif operators[i-1] == "c":
                    cur_val = int(str(cur_val) + str(num))
            if cur_val == result:
                total += result 
                break

    return total

def get_operators_with_concatenation(operators, num_of_operators):
    if len(operators) == num_of_operators:
        all.add(operators)
        return

    add = get_operators_with_concatenation(operators+"+", num_of_operators)
    mult = get_operators_with_concatenation(operators+"*", num_of_operators)
    concat = get_operators_with_concatenation(operators+"c", num_of_operators)

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time}")
