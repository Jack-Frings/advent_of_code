def part_one():
    with open("mul.txt") as file:
        lines = list(file.readlines())
    line = ""
    for individual_line in lines:
        line += individual_line

    possible_valids = []

    for i in range(len(line)):
        if line[i:i+4] == "mul(":
            end = i + 4 + int(line[i+4:].index(")"))
            possible_valids.append(line[i+4:end])
    
    total = 0
    for val in possible_valids:
        try: 
            a, b = val.split(",")
            total += int(a)*int(b)
        except Exception:
            continue

    return total
def part_two():
    with open("mul.txt") as file:
        lines = list(file.readlines())
    line = ""
    for individual_line in lines:
        line += individual_line

    possible_valids = []

    for i in range(len(line)):
        if line[i:i+4] == "mul(":
            end = i + 4 + int(line[i+4:].index(")"))
            possible_valids.append(line[i+4:end])
        if line[i:i+4] == "do()":
            possible_valids.append("do()")
        if line[i:i+7] == "don't()":
            possible_valids.append("don't()")
    total = 0
    
    do = True
    for val in possible_valids:
        try: 
            if val == "do()":
                do = True
                continue
            if val == "don't()":
                do = False
                continue
            if do:
                a, b = val.split(",")
                total += int(a)*int(b)
        except Exception:
            continue
    
    return total

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
