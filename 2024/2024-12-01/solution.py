class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def solve_part_1(self):
        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        return f'\nResult puzzle 2: {self.result_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
