import time, copy
start = time.time()

def part_one():
    with open("ingredients.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    sum = 0

    ranges = set()
    vals = set()
    passed = False
    for line in lines:
        if line == "":
            passed = True
        elif not passed:
            ranges.add(line)
        else:
            vals.add(line)

    for val in vals:
        val = int(val)
        fresh = False
        for bounds in ranges:
            lower, upper = bounds.split("-")
            if (int(lower) <= val <= int(upper)):
                fresh = True
                break 

        if fresh:
            sum += 1
            
    return sum

def part_two():
    with open("ingredients.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    bounds_set = set()
    for line in lines:
        if line == "":
            break
        else:
            x, y = line.split("-")
            bounds_set.add((int(x), int(y)))

    change = True
    while change == True:    
        change = False 
        copy_bounds = copy.deepcopy(bounds_set)

        for bounds in bounds_set:
            for other_bounds in bounds_set:
                if bounds == other_bounds: continue 
                
                lower, upper = bounds
                other_lower, other_upper = other_bounds

                if not (upper < other_lower or other_upper < lower):
                    change = True
                    try: copy_bounds.remove(bounds)
                    except KeyError: pass
                    try: copy_bounds.remove(other_bounds)
                    except KeyError: pass
                    copy_bounds.add((min(lower, other_lower), max(upper, other_upper)))

        bounds_set = copy.deepcopy(copy_bounds)

    sum = 0
    for bounds in bounds_set:
        x, y = bounds 
        sum += y - x + 1

    return sum

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
