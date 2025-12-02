import time 
start = time.time()

def part_one():
    with open("id.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    line = lines[0]

    id_bounds = line.split(",")
    sum = 0

    for id_bound in id_bounds:
        from_bound, to_bound = id_bound.split("-")
        for id in range(int(from_bound), int(to_bound) + 1):
            if isInvalid(id):
                sum += id 

    return sum

def part_two():
    with open("id.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    line = lines[0]

    id_bounds = line.split(",")
    sum = 0

    for id_bound in id_bounds:
        from_bound, to_bound = id_bound.split("-")
        for id in range(int(from_bound), int(to_bound) + 1):
            if isInvalid2(id):
                sum += id 

    return sum

def isInvalid(id):
    id = str(id)
    if len(id) % 2 == 1:
        return False 

    halfway = int(len(id) / 2)

    if id[:halfway] == id[halfway:]:
        return True 

    return False

def isInvalid2(id):
    id = str(id)
    length = len(id)
    halfway = int(len(id) / 2)

    for num in range(1, halfway+1):
        if length % num == 0:
            invalid = True 
            phrase = id[:num] 
            for i in range(num, length-num+1, num):
                if id[i:i+num] != phrase:
                    invalid = False
                    break 

            if invalid:
                return True 

    return False 

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
