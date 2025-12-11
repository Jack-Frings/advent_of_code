import time, copy
import numpy as np
start = time.time()

def part_one():
    with open("11.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    servers = {}
    for line in lines:
        key, vals = line.split(": ") 
        vals = [val for val in vals.split(" ")]
        servers[key] = vals 

    frontier = [["you"]]
    total = 0

    while len(frontier) > 0:
        cur_path = frontier.pop(0)
        last = cur_path[-1] 

        if servers[last][0] == "out":
            total += 1
        else:
            for option in servers[last]:
                frontier.append(cur_path + [option])

    return total

def part_two():
    with open("11.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    global servers
    servers = {}
    for line in lines:
        key, vals = line.split(": ") 
        vals = [val for val in vals.split(" ")]
        servers[key] = vals 

    key_svrs = ["dac", "fft"]
    frontier = ["svr"]
    # Find first instace of "dec" or "fft"
    while True:
        svr = frontier.pop(0)
        if svr in key_svrs:
            break
        else:
            for option in servers[svr]:
                frontier.append(option)

    key1 = svr
    key_svrs.remove(key1) 
    key2 = key_svrs[0]

    global outs
    outs = set()

    a = first_find_paths(key2, "out")
    print(a)

    print(outs)

    exit()
    b = find_paths(key1, key2)
    print(b)
    c = find_paths("svr", key1)
    print(c)

    return a*b*c

def first_find_paths(start, end):
    global servers
    global outs
    count = 0
    frontier = [[start]] 
    while len(frontier) > 0:
        cur_path = frontier.pop(0)
        last = cur_path[-1] 
        if end in servers[last]:
            count += 1 
        elif "out" in servers[last]: 
            pass
        else:
            for option in servers[last]:
                outs.add(option)
                frontier.append(cur_path + [option]) 

    return count

def find_paths(start, end):
    global servers
    count = 0
    frontier = [[start]] 
    while len(frontier) > 0:
        cur_path = frontier.pop(0)
        last = cur_path[-1] 
        if end in servers[last]:
            count += 1 
        elif "out" in servers[last]: 
            pass
        else:
            for option in servers[last]:
                frontier.append(cur_path + [option]) 

    return count


if __name__ == "__main__":
    # print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
