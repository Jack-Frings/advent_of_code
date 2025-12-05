import hashlib
import time 
start = time.time()

def part_one():
    with open("coins.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    line = lines[0]

    i = 0
    while True:
        msg = line + str(i)
        hash = hashlib.md5(msg.encode()).hexdigest()
        if hash[:5] == "00000":
            return i

        i += 1


def part_two():
    with open("coins.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    line = lines[0]

    i = 0
    while True:
        msg = line + str(i)
        hash = hashlib.md5(msg.encode()).hexdigest()
        if hash[:6] == "000000":
            return i

        i += 1

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
