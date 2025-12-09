import time, copy, sys
start = time.time()

def part_one():
    with open("9.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    points = set()
    for line in lines:
        x, y = line.split(",") 
        points.add((int(x), int(y)))

    area = 0 
    for point_a in points:
        for point_b in points:
            if point_a == point_b: continue 
            next_area = getArea(point_a, point_b) 
            if next_area > area:
                area = next_area

    return area

def getArea(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def part_two():
    with open("9.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    red_points = set()
    global points 
    points = dict()
    points["y"] = {}
    points["x"] = {}

    # Get red and green tile grid outline 
    last_x, last_y = lines[-1].split(",")
    last_x = int(last_x)
    last_y = int(last_y)

    for line in lines:
        cur_x, cur_y = line.split(",") 
        cur_x = int(cur_x)
        cur_y = int(cur_y)
        red_points.add((cur_x, cur_y))

        for y in range(min(last_y, cur_y), max(last_y, cur_y) + 1):
            if y not in points["y"].keys():
                points["y"][y] = set()
            for x in range(min(last_x, cur_x), max(last_x, cur_x) + 1):
                points["y"][y].add(x)

        for x in range(min(last_x, cur_x), max(last_x, cur_x) + 1):
            if x not in points["x"].keys():
                points["x"][x] = set() 
            for y in range(min(last_y, cur_y), max(last_y, cur_y) + 1):
                points["x"][x].add(y)

        last_x = cur_x
        last_y = cur_y

    for x in points["x"].keys():
        vals = sorted(points["x"][x]) 
        points["x"][x] = [vals[0], vals[-1]]

    for y in points["y"].keys():
        vals = sorted(points["y"][y]) 
        points["y"][y] = [vals[0], vals[-1]]

    areas = {}
    for point_a in red_points:
        for point_b in red_points:
            if point_a == point_b: continue 
            passed_points = areas.keys() 
            if not ((point_a, point_b) in passed_points or (point_b, point_a) in passed_points):
                new_area = getArea(point_a, point_b)
                areas[(point_a, point_b)] = new_area

    areas = dict(sorted(areas.items(), key=lambda area: area[1], reverse=True))

    keys = list(areas.keys())

    enclosed_history = set()
    unenclosed_history = set()

    for i in range(len(keys)):
        point_a, point_b = keys[i] 
        x1, y1 = point_a
        x2, y2 = point_b

        fully_enclosed = True 

        for x in range(min(x1, x2), max(x1, x2) + 1):
            if (x, y1) in enclosed_history: pass
            elif (x, y1) in unenclosed_history:
                fully_enclosed = False
                break
            elif not enclosed((x, y1)):
                unenclosed_history.add((x, y1))
                fully_enclosed = False 
                break
            else:
                enclosed_history.add((x, y1))

            if (x, y2) in enclosed_history: pass
            elif (x, y2) in unenclosed_history:
                fully_enclosed = False
                break
            elif not enclosed((x, y2)):
                unenclosed_history.add((x, y2))
                fully_enclosed = False 
                break
            else:
                enclosed_history.add((x, y2))

        if not fully_enclosed: continue 

        for y in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, y) in enclosed_history: pass
            elif (x1, y) in unenclosed_history:
                fully_enclosed = False
                break
            elif not enclosed((x1, y)):
                unenclosed_history.add((x1, y))
                fully_enclosed = False 
                break
            else:
                enclosed_history.add((x1, y))

            if (x2, y) in enclosed_history: pass
            elif (x2, y) in unenclosed_history:
                fully_enclosed = False
                break
            elif not enclosed((x2, y)):
                unenclosed_history.add((x2, y))
                fully_enclosed = False 
                break
            else:
                enclosed_history.add((x2, y))

        if not fully_enclosed: continue 

        return areas[(keys[i])]

def enclosed(point):
    global points 
    point_x, point_y = point 

    # Check up and down 
    y_coords = points["x"][point_x] 
    if not (y_coords[0] <= point_y <= y_coords[1]):
        return False 

    # Check left and right 
    x_coords = points["y"][point_y]
    if not (x_coords[0] <= point_x <= x_coords[1]):
        return False 

    return True

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
