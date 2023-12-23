class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.instructions_list = self.lines_list[0]

        self.elements_dict = {}
        for i in range(2, len(self.lines_list)):
            element = self.lines_list[i].split(' = ')[0]
            left_element = self.lines_list[i].split(' = ')[1].split(', ')[0].replace('(', '')
            right_element = self.lines_list[i].split(' = ')[1].split(', ')[1].replace(')', '')
            self.elements_dict[element] = {'L': left_element, 'R': right_element}

    def solve_part_1(self):
        steps = 0
        element = 'AAA'

        while True:
            for instruction in self.instructions_list:
                element = self.elements_dict[element][instruction]
                steps += 1
                if element == 'ZZZ':
                    return f'\nResult puzzle 1: {steps} steps'

    def solve_part_2(self):
        from math import lcm

        steps = 0
        e_1 = 'VNA'
        e_2 = 'AAA'
        e_3 = 'DPA'
        e_4 = 'JPA'
        e_5 = 'DBA'
        e_6 = 'QJA'

        e_1_steps = 0
        e_2_steps = 0
        e_3_steps = 0
        e_4_steps = 0
        e_5_steps = 0
        e_6_steps = 0

        while (e_1_steps == 0 or e_2_steps == 0 or e_3_steps == 0 or
               e_4_steps == 0 or e_5_steps == 0 or e_6_steps == 0):
            for instruction in self.instructions_list:
                e_1 = self.elements_dict[e_1][instruction]
                e_2 = self.elements_dict[e_2][instruction]
                e_3 = self.elements_dict[e_3][instruction]
                e_4 = self.elements_dict[e_4][instruction]
                e_5 = self.elements_dict[e_5][instruction]
                e_6 = self.elements_dict[e_6][instruction]
                steps += 1

                if e_1[2] == 'Z' and not e_1_steps:
                    e_1_steps = steps
                if e_2[2] == 'Z' and not e_2_steps:
                    e_2_steps = steps
                if e_3[2] == 'Z' and not e_3_steps:
                    e_3_steps = steps
                if e_4[2] == 'Z' and not e_4_steps:
                    e_4_steps = steps
                if e_5[2] == 'Z' and not e_5_steps:
                    e_5_steps = steps
                if e_6[2] == 'Z' and not e_6_steps:
                    e_6_steps = steps

        print(e_1_steps, e_2_steps, e_3_steps, e_4_steps, e_5_steps, e_6_steps)

        return f'\nResult puzzle 2: {lcm(e_1_steps, e_2_steps, e_3_steps, e_4_steps, e_5_steps, e_6_steps)} steps'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
