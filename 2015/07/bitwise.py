import time, copy
start = time.time()

def part_one():
    with open("7.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    global operations
    operations = ["AND", "OR", "NOT", "LSHIFT", "RSHIFT"]
    global wires
    wires = {}

    for line in lines:
        input, output = line.split(" -> ")
        if input.isdigit():
            input = int(input)
        else:
            for operation in operations:
                if operation in input:
                    if operation == "NOT":
                        input = ["NOT", input.strip("NOT").strip()]
                    else:
                        x, y = input.split(operation)
                        x = x.strip()
                        if x.isdigit(): x = int(x)
                        y = y.strip() 
                        if y.isdigit(): y = int(y)
                        input = [operation, x, y]

        wires[output] = input


    return getSignal("a")

def getSignal(key):
    global wires 
    equation = wires[key] 

    if type(equation) == int:
        return equation
    elif type(equation) == str:
        wires[key] = getSignal(equation)
        return wires[key]

    operation = equation[0]

    if operation == "NOT":
        if type(equation[1]) == int:
            wires[key] = 65536 + (~ equation[1])
            return wires[key]
        else:
            wires[key] = 65536 + (~ getSignal(equation[1])) 
            return wires[key]

    else:
        val1 = equation[1]
        if type(val1) != int:
            val1 = getSignal(val1)

        val2 = equation[2] 
        if type(val2) != int:
            val2 = getSignal(val2)


        if operation == "AND":
            wires[key] = val1 & val2 
        elif operation == "OR":
            wires[key] = val1 | val2 
        elif operation == "LSHIFT":
            wires[key] = val1 << val2 
        elif operation == "RSHIFT":
            wires[key] = val1 >>  val2

        return wires[key]

def part_two():
    with open("7.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    global operations
    operations = ["AND", "OR", "NOT", "LSHIFT", "RSHIFT"]
    global wires
    wires = {}

    for line in lines:
        input, output = line.split(" -> ")
        if input.isdigit():
            input = int(input)
        else:
            for operation in operations:
                if operation in input:
                    if operation == "NOT":
                        input = ["NOT", input.strip("NOT").strip()]
                    else:
                        x, y = input.split(operation)
                        x = x.strip()
                        if x.isdigit(): x = int(x)
                        y = y.strip() 
                        if y.isdigit(): y = int(y)
                        input = [operation, x, y]

        wires[output] = input

    og_wires = copy.deepcopy(wires)

    og_wires["b"] = getSignal("a")

    wires = og_wires 
    return getSignal("a")


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
