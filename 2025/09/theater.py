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

    history = set()

    area = 0
    iterations = len(red_points) ** 2 
    i = 0
    for point_a in red_points:
        for point_b in red_points:
            i += 1 
            print(f"{i}/{iterations}")
            if point_a == point_b: continue
            new_area = getArea(point_a, point_b)
            if new_area > area:
                x1, y1 = point_a 
                x2, y2 = point_b
                fully_enclosed = True 

                for x in range(min(x1, x2), max(x1, x2) + 1):
                    if (x, y1) in history: pass
                    elif not enclosed((x, y1)):
                        fully_enclosed = False 
                        break
                    else:
                        history.add((x, y1))

                    if (x, y2) in history: pass
                    elif not enclosed((x, y2)):
                        fully_enclosed = False 
                        break
                    else:
                        history.add((x, y2))

                if not fully_enclosed: continue 

                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if (x1, y) in history: pass
                    elif not enclosed((x1, y)):
                        fully_enclosed = False 
                        break
                    else:
                        history.add((x1, y))

                    if (x2, y) in history: pass
                    elif not enclosed((x2, y)):
                        fully_enclosed = False 
                        break
                    else:
                        history.add((x2, y))

                if not fully_enclosed: continue 

                area = new_area

    return area

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


    # display = list()
    # row = "." * 14
    # for y in range(9):
    #     display.append(copy.deepcopy(row))
    #
    # for point in points:
    #     x, y = point 
    #     display[y] = display[y][:x] + "X" + display[y][x+1:]
    #
    # for point in red_points:
    #     x, y = point 
    #     display[y] = display[y][:x] + "O" + display[y][x+1:]
    #
    # for row in display:
    #     print(row)


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
