import re
import time 
start = time.time()

def main():
    with open("id.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    line = lines[0]

    id_bounds = line.split(",")
    sum_one = 0
    sum_two = 0

    part_one = re.compile(r'^(\d*)\1$')
    part_two = re.compile(r'^(\d*)\1+$')

    for id_bound in id_bounds:
        from_bound, to_bound = id_bound.split("-")
        for id in range(int(from_bound), int(to_bound) + 1):
            if part_one.match(str(id)):
                sum_one += id 
                sum_two += id 
            elif part_two.match(str(id)):
                sum_two += id
                

    return (sum_one, sum_two)

if __name__ == "__main__":
    part_one, part_two = main()
    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")
    print(f"Execution Time: {time.time() - start}")
