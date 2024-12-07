class AdventOfCode:
    def __init__(self, filename):
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


puzzle = AdventOfCode('example.txt')
# puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
