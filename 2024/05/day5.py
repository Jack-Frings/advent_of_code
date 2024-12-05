def part_one():
    with open("day5.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines] 
    before = []
    after = [] 
    sum = 0

    for line in lines:
        if line == "":
            break
        before.append(line.split("|")[0])
        after.append(line.split("|")[1])

    for line in lines:
        if "|" in line or line == "":
            continue
        valid = True
        line_nums = list(line.split(","))
        for search_index, search_num in enumerate(line_nums):
            # Before 
            for index, num in enumerate(before):
                if search_num == num:
                    if after[index] in line_nums[0:search_index]:
                        valid = False
            # After 
            for index, num in enumerate(after):
                if search_num == num:
                    if before[index] in line_nums[search_index:]:
                        valid = False 
        if valid:
            middle = int((len(line_nums)-1)/2)
            sum += int(line_nums[middle])
    return sum
            
def part_two():
    with open("day5.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines] 
    before = []
    after = [] 
    invalid_lines = []
    sum = 0

    for line in lines:
        if line == "":
            break
        before.append(line.split("|")[0])
        after.append(line.split("|")[1])

    for line in lines:
        if "|" in line or line == "":
            continue
        valid = True
        line_nums = list(line.split(","))
        for search_index, search_num in enumerate(line_nums):
            # Before 
            for index, num in enumerate(before):
                if search_num == num:
                    if after[index] in line_nums[0:search_index]:
                        valid = False
            # After 
            for index, num in enumerate(after):
                if search_num == num:
                    if before[index] in line_nums[search_index:]:
                        valid = False 
        if not valid:
            invalid_lines.append(line)

    for line in invalid_lines:
        line_nums = list(line.split(","))
        original = line_nums
        length = len(line_nums)

        final_line = []

        while len(final_line) < length:
            for search_index, search_num in enumerate(original):
                valid = True
                # Before
                for index, num in enumerate(after):
                    if search_num == num:
                        if before[index] in line_nums:
                            valid = False 
                if valid:
                    final_line.append(search_num)
                    line_nums.remove(search_num)
        middle = int((len(final_line)-1)/2)
        sum += int(final_line[middle])


    return sum

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
