class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.location_id_left_list = []
        self.location_id_right_list = []
        for line in self.lines_list:
            location_id_left, location_id_right = line.split('   ')
            self.location_id_left_list.append(int(location_id_left))
            self.location_id_right_list.append(int(location_id_right))

        self.location_id_left_list_sorted = sorted(self.location_id_left_list)
        self.location_id_right_list_sorted = sorted(self.location_id_right_list)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def solve_part_1(self):
        for index, location_id_left in enumerate(self.location_id_left_list_sorted):
            self.result_puzzle_1 += abs(location_id_left - self.location_id_right_list_sorted[index])

        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        for index, location_id_left in enumerate(self.location_id_left_list):
            self.result_puzzle_2 += location_id_left * self.location_id_right_list.count(location_id_left)

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
