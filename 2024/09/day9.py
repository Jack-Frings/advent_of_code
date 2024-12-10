import time 
start_time = time.time()

def part_one():
    with open("day9.txt") as file:
        line = file.readline()
        line = line.strip("\n")
    spaced_line = []

    empty_space = False
    num = 0
    for char in line:
        if not empty_space:
            for _ in range(int(char)):
                spaced_line.append(num)
            num += 1
        else:
            for _ in range(int(char)):
                spaced_line.append(".") 
        empty_space = not empty_space 

    total = 0

    # for i, num in enumerate(spaced_line):
    #     print((float(i)/(len(spaced_line)-1)))
    #     if len(set(spaced_line)) == 1:
    #         break
    #     if num == ".":
    #         for j, back_num in enumerate(spaced_line[::-1]):
    #             if back_num.isdigit():
    #                 total += int(back_num)*i
    #                 eliminate = len(spaced_line) - 1 - j
    #                 spaced_line = spaced_line[0:eliminate] + "." + spaced_line[eliminate+1:]
    #                 break
    #     if num.isdigit():
    #         total += int(num)*i 
    #         spaced_line = spaced_line[0:i] + "." + spaced_line[i+1:]

    formatted = False
    for _ in range(len(spaced_line)):
        # Check if its formatted correctly
        formatted = True
        foundPeriod = False
        for char in spaced_line:
            if char == ".":
                foundPeriod = True 
            if type(char) == int and foundPeriod:
                formatted = False
                break 
        if formatted:
            break

        # Find num to move
        for index, char in enumerate(spaced_line[::-1]):
            if type(char) == int:
                move_num = char 
                index = len(spaced_line) - 1 - index
                spaced_line[index] = "."
                break
        # Place num 
        for index, char in enumerate(spaced_line):
            if char == ".":
                spaced_line[index] = move_num
                break
    for index, char in enumerate(spaced_line):
        if char == ".":
            break 
        total += int(char)*index
    return total

def part_two():
    with open("day9.txt") as file:
        line = file.readline().strip("\n")
    spaced_line = []

    empty_space = False
    num = 0
    for char in line:
        file = []
        if not empty_space:
            file.append(num) # int
            num += 1
        else:
            file.append(".")
        file.append(int(char)) # int
        if file[1] > 0:
            spaced_line.append(file)
        empty_space = not empty_space 

    num -= 1    
    while num >= 0:
        length = 0
        open_space_index = -1
        for index, file in enumerate(spaced_line[::-1]):
            if file[0] == num:
                length = file[1] 
                file_index = index
            if file[0] == "." and file[1] >= length > 0:
                open_space_index = index 


        if open_space_index >= 0:
            file_index = len(spaced_line) - 1 - file_index
            open_space_index = len(spaced_line) - 1 - open_space_index
            spaced_line[open_space_index][1] -= length 
            spaced_line.insert(open_space_index, [num, length])
            spaced_line[file_index+1][0] = "."
        num -= 1
    
    final = []
    total = 0

    for index, file in enumerate(spaced_line):
        for _ in range(file[1]):
            final.append(file[0])

    print(final)

    for index, char in enumerate(final):
        if char != ".":
            total += int(char)*index

    return total

if __name__ == "__main__":
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start_time}")
