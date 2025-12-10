import time, copy
import numpy as np
start = time.time()

def part_one():
    with open("10.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    button_presses = 0
    for line in lines:
        items = list(line.split(" "))[:-1]
        goal_lights = items[0][1:-1].replace(".", "0").replace("#", "1")
        goal_lights = [bool(int(char)) for char in goal_lights]

        buttons = get_buttons(items[1:])

        start = [False for val in goal_lights] 

        frontier = [(start, 0)]
        history = set()

        not_found = True
        while not_found:
            cur_lights, buttons_pressed = frontier.pop(0)
            history.add(tuple(cur_lights))

            for button in buttons:
                future_lights = copy.deepcopy(cur_lights)
                for change in button:
                    future_lights[change] = not future_lights[change]
                if future_lights == goal_lights:
                    button_presses += buttons_pressed + 1
                    not_found = False
                    break 
                else:
                    future_lights_tuple = tuple(future_lights)
                    if future_lights_tuple not in history:
                        frontier.append((future_lights, buttons_pressed+1))
                        history.add(future_lights_tuple)

    return button_presses

def part_two():
    with open("10.txt") as file:
        lines = list(file.readlines())
        lines = [line.strip("\n") for line in lines]

    length = len(lines)

    button_presses = 0
    for line in lines:
        items = list(line.split(" "))[1:]

        buttons, length = get_variable_based_buttons(items[:-1])
        joltages = get_joltages(items[-1])


        equations = [] 
        for i in range(len(joltages)):
            equation = []
            for j in range(length):
                if j in buttons[i]:
                    equation.append(1)
                else:
                    equation.append(0)
            equations.append(equation)

        coefficients = np.array(equations)
        joltages = np.array(joltages)
        estimated_val = sum(list(np.linalg.lstsq(coefficients, joltages))[0].tolist())
        print(estimated_val)

    return button_presses

def get_buttons(buttons):
    int_buttons = []
    for button in buttons:
        button = button[1:-1] 
        button = [int(num) for num in button.split(",")]
        int_buttons.append(button)

    return int_buttons

def get_variable_based_buttons(buttons):
    maximum = -1
    int_buttons = []
    for button in buttons:
        button = button[1:-1] 
        button = [int(num) for num in button.split(",")]
        if button[-1] > maximum:
            maximum = button[-1]
        int_buttons.append(button)

    variable_based_buttons = []
    for i in range(maximum+1):
        buttons = []
        for j, button in enumerate(int_buttons):
            if i in button:
                buttons.append(j)
        variable_based_buttons.append(buttons)

    return variable_based_buttons, len(int_buttons)


def get_joltages(joltages):
    joltages = joltages[1:-1]
    return [int(joltage) for joltage in joltages.split(",")]


if __name__ == "__main__":
    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
    print(f"Execution Time: {time.time() - start}")
