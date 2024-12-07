class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]

        # input
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.adjusted_lines_list = []
        for line in self.lines_list:
            reports = line.split(' ')
            self.adjusted_lines_list.append([int(i) for i in reports])

        for y, line in enumerate(self.lines_list):
            for x, i in enumerate(line):
                print(y, x, i)

        self.width = len(self.lines_list[0])
        self.length = len(self.lines_list)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def solve_part_1(self):
        for index, line_list in enumerate(self.adjusted_lines_list):
            if 1 == 1:
                self.result_puzzle_1 += 1

        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        for index, line_list in enumerate(self.adjusted_lines_list):
            if 1 == 1:
                self.result_puzzle_2 += 1

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
