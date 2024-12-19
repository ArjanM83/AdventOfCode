class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.available_towel_patterns_list = self.lines_list[0].split(', ')
        self.designs_list = []
        for line in self.lines_list[2:]:
            self.designs_list.append(line)

        if self.use_example:
            print('available towel patterns:', self.available_towel_patterns_list)
            print('designs:', self.designs_list)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def design_is_possible(self, design):
        design_positions_list = [False] * (len(design) + 1)
        design_positions_list[0] = True
        if self.use_example:
            print('\ndesign puzzle 1:', design)

        for i in range(len(design)):
            if design_positions_list[i]:
                if self.use_example:
                    print('reached position:', i)
                for pattern in self.available_towel_patterns_list:
                    if design.startswith(pattern, i):
                        design_positions_list[i + len(pattern)] = True
                        if self.use_example:
                            print('pattern works:', pattern, design_positions_list)
                    else:
                        if self.use_example:
                            print('pattern does not work:', pattern, design_positions_list)
            else:
                if self.use_example:
                    print('position false:', i)

        design_is_possible = design_positions_list[len(design)]
        if self.use_example:
            print('design is possible:', design_is_possible)
        return design_is_possible

    def get_number_of_designs_possible(self, design):
        design_positions_list = [0] * (len(design) + 1)
        design_positions_list[0] = 1
        if self.use_example:
            print('\ndesign puzzle 2:', design)

        for i in range(len(design)):
            if design_positions_list[i] > 0:
                if self.use_example:
                    print(f'position:', i)
                for pattern in self.available_towel_patterns_list:
                    if design.startswith(pattern, i):
                        design_positions_list[i + len(pattern)] += design_positions_list[i]
                        if self.use_example:
                            print('pattern works:', pattern, design_positions_list)
                        else:
                            if self.use_example:
                                print('pattern does not work:', pattern, design_positions_list)
            else:
                if self.use_example:
                    print(f'position skipped:', i)

        return design_positions_list[len(design)]

    def solve_part_1(self):
        for design in self.designs_list:
            if self.design_is_possible(design):
                self.result_puzzle_1 += 1

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        for design in self.designs_list:
            if self.design_is_possible(design):
                self.result_puzzle_2 += self.get_number_of_designs_possible(design)

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
