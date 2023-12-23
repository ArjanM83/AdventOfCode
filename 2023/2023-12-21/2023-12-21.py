class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.steps_dict = {0: {65: [65]}}

    def register_step(self, step, y_coordinate, x_coordinate):
        if step in self.steps_dict:
            if y_coordinate in self.steps_dict[step]:
                self.steps_dict[step][y_coordinate].append(x_coordinate)
            else:
                self.steps_dict[step][y_coordinate] = [x_coordinate]
        else:
            self.steps_dict[step] = {y_coordinate: [x_coordinate]}

        self.steps_dict[step][y_coordinate] = list(set(self.steps_dict[step][y_coordinate]))

    def register_steps(self, step, y_coordinate, x_coordinate):
        try:
            if self.lines_list[y_coordinate + 1][x_coordinate] != '#':
                self.register_step(step, y_coordinate + 1, x_coordinate)
        except:
            pass
        try:
            if self.lines_list[y_coordinate - 1][x_coordinate] != '#':
                self.register_step(step, y_coordinate - 1, x_coordinate)
        except:
            pass
        try:
            if self.lines_list[y_coordinate][x_coordinate + 1] != '#':
                self.register_step(step, y_coordinate, x_coordinate + 1)
        except:
            pass
        try:
            if self.lines_list[y_coordinate][x_coordinate - 1] != '#':
                self.register_step(step, y_coordinate, x_coordinate - 1)
        except:
            pass

    def solve_part_1(self):
        sum_of_steps = 0

        for step in range(1, 65):
            for y_coordinate in self.steps_dict[step - 1]:
                for x_coordinate in self.steps_dict[step - 1][y_coordinate]:
                    self.register_steps(step, y_coordinate, x_coordinate)

            print(step)

        for y_coordinate in self.steps_dict[64]:
            sum_of_steps += len(set(self.steps_dict[64][y_coordinate]))

        return sum_of_steps

    def solve_part_2(self):
        return 0


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
