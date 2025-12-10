import time, copy
import numpy as np
import scipy
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

    lines_length = len(lines)

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

        """
        I'm so glad this works. I'm just writing a bit of documentation here mostly so that I can remember how this all works for future 
        AoC problems. Basically, I'm creating a matrix for a system of equations here. Each equation has a variable for the number of
        times that each button has been pressed. These variables are then multiplied by a coefficient of 1 or 0 depending on if it affects 
        the joltage while the entire equation is set equal to the end joltage. The minimization_function just adds together all of the button
        presses for all the buttons (as that's what we're minimizing). The bounds specifies that you can't have negative button presses, and 
        the integrality specifies that the solutions have to be integers (cannot have decimals). All of this information is then plugged into 
        scipy.optimize.linprog() [https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog]
        """

        coefficients = np.array(equations)
        joltages = np.array(joltages)

        minimization_function = [1 for i in equation] 
        bounds = [(0, None) for i in equation]
        integrality = [1 for i in equation]

        answer = scipy.optimize.linprog(minimization_function, A_eq=coefficients, b_eq=joltages, bounds=bounds, integrality=integrality)

        button_presses += int(answer['fun'])



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
