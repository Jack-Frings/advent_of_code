import time 
start_time = time.time()

def part_one():
    with open("antennas.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    
    letters = {}
    antinodes = set()
    max_x = len(lines[0]) 
    max_y = len(lines)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                if char not in letters.keys():
                    letters[char] = []
                letters[char].append(tuple((x, y)))
    
    for letter in letters.keys():
        for search_point in letters[letter]:
            for point in letters[letter]:
                if search_point == point:
                    continue
                new_antinodes = find_antinodes(search_point, point, max_x, max_y)
                for antinode in new_antinodes:
                    antinodes.add(antinode)

    # (4,3) & (5,5)
    # (3,1) & (6,7)
    return len(antinodes)

def find_antinodes(search_point, point, max_x, max_y):
    antinodes = []
    
    search_x, search_y = search_point
    x, y = point 
    slope = float(search_y - y) / float(search_x - x)

    # Antinode 1  
    antinode_x = search_x*2 - x 
    antinode_y = search_y*2 - y 
    antinode_slope = float(y - antinode_y) / float(x - antinode_x)
    if 0 <= antinode_x < max_x and 0 <= antinode_y < max_y and abs(antinode_slope - slope) < 0.01:
        antinodes.append(tuple((antinode_x, antinode_y)))

    # Antinode 2  
    antinode_x = x*2 - search_x 
    antinode_y = y*2 - search_y 
    antinode_slope = float(y - antinode_y) / float(x - antinode_x)
    if 0 <= antinode_x < max_x and 0 <= antinode_y < max_y and abs(antinode_slope - slope) < 0.01:
        antinodes.append(tuple((antinode_x, antinode_y)))
    return antinodes
    
def part_two():
    with open("antennas.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]
    
    letters = {}
    antinodes = set()
    max_x = len(lines[0]) 
    max_y = len(lines)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                if char not in letters.keys():
                    letters[char] = []
                letters[char].append(tuple((x, y)))
    
    for letter in letters.keys():
        for search_point in letters[letter]:
            for point in letters[letter]:
                if search_point == point:
                    continue
                new_antinodes = find_all_antinodes_with_slope(search_point, point, max_x, max_y)
                for antinode in new_antinodes:
                    antinodes.add(antinode)

    return len(antinodes)

def find_all_antinodes_with_slope(search_point, point, max_x, max_y):
    antinodes = []
    antinodes.append(search_point)
    antinodes.append(point)
    
    search_x, search_y = search_point
    search2_x, search2_y = point 
    search_slope = float(search2_y - search_y) / float(search2_x - search_x)

    for x in range(0, max_x):
        for y in range(0, max_y):
            if x == search_x or y == search_y or x == search2_x or y == search2_y:
                continue 
            
            slope = float(search_y - y) / float(search_x - x) 
            if search_slope == slope:
                antinodes.append(tuple((x, y)))

    return antinodes

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time}")
