def part_one():
    with open("search.txt") as file:
        lines = list(file.readlines())
    
    count = 0
    for col in range(len(lines[0])-1):
        for row in range(len(lines)):
            # Horizontals 
            try:
                if lines[row][col] + lines[row][col+1] + lines[row][col+2] + lines[row][col+3] == "XMAS":
                    count += 1 
            except IndexError:
                pass 
            try:
                if col - 3 < 0:
                    raise IndexError
                if lines[row][col] + lines[row][col-1] + lines[row][col-2] + lines[row][col-3] == "XMAS":
                    count += 1 
            except IndexError:
                pass
            # Verticals
            try:
                if lines[row][col] + lines[row+1][col] + lines[row+2][col] + lines[row+3][col] == "XMAS":
                    count += 1
            except IndexError:
                pass
            try:
                if row - 3 < 0:
                    raise IndexError
                if lines[row][col] + lines[row-1][col] + lines[row-2][col] + lines[row-3][col] == "XMAS":
                    count += 1
            except IndexError:
                pass

            # Diagonals
            try:
                if lines[row][col] + lines[row+1][col+1] + lines[row+2][col+2] + lines[row+3][col+3] == "XMAS":
                    count += 1 
            except IndexError:
                pass
            try:
                if col - 3 < 0:
                    raise IndexError
                if lines[row][col] + lines[row+1][col-1] + lines[row+2][col-2] + lines[row+3][col-3] == "XMAS":
                    count += 1 
            except IndexError:
                pass 
            try:
                if row - 3 < 0:
                    raise IndexError
                if lines[row][col] + lines[row-1][col+1] + lines[row-2][col+2] + lines[row-3][col+3] == "XMAS":
                    count += 1 
            except IndexError:
                pass 
            try:
                if row - 3 < 0 or col - 3 < 0:
                    raise IndexError
                if lines[row][col] + lines[row-1][col-1] + lines[row-2][col-2] + lines[row-3][col-3] == "XMAS":
                    count += 1 
            except IndexError:
                pass
    return count

def part_two():
    with open("search.txt") as file:
        lines = list(file.readlines())
    
    count = 0
    for col in range(1, len(lines[0])-1):
        for row in range(1, len(lines)):
            first = False
            second = False
            try:
                if lines[row-1][col-1] + lines[row][col] + lines[row+1][col+1] in ["MAS", "SAM"]:
                    first = True
            except IndexError:
                pass 
            try:
                if lines[row+1][col-1] + lines[row][col] + lines[row-1][col+1] in ["MAS", "SAM"]:
                    second = True
            except IndexError:
                pass 
            if first and second:
                count += 1

    return count

if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
