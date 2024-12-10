class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()
        if self.use_example:
            print('input:', self.lines_list)

        self.positions_list = []
        for line in self.lines_list:
            self.positions_list.append([int(i) for i in line])
        if self.use_example:
            print('positions:', self.positions_list)

        self.trailheads_list = []
        for y, line in enumerate(self.positions_list):
            for x, i in enumerate(line):
                if i == 0:
                    self.trailheads_list.append((x, y))
        if self.use_example:
            print('trailheads list:', self.trailheads_list)

        self.width = len(self.lines_list[0])
        self.length = len(self.lines_list)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def position_within_mapped_area(self, x, y):
        if 0 <= x < self.width:
            if 0 <= y < self.length:
                return True

    def get_trailhead_score_puzzle_1(self, x, y, score=0, visited_trailheads_list=None):
        current_position = self.positions_list[y][x]
        if self.use_example:
            print((x, y), current_position)

        # check if current position is 9
        if self.positions_list[y][x] == 9:
            visited_trailheads_list.append((x, y))
            score += 1
            if self.use_example:
                print('sub score:', score)
        else:
            # try to go up
            new_x, new_y = x, y - 1
            if self.position_within_mapped_area(new_y, new_x) and (new_x, new_y) not in visited_trailheads_list:
                if self.positions_list[new_y][new_x] == current_position + 1:
                    score = self.get_trailhead_score_puzzle_1(new_x, new_y, score, visited_trailheads_list)

            # try to go down
            new_x, new_y = x, y + 1
            if self.position_within_mapped_area(new_y, new_x) and (new_x, new_y) not in visited_trailheads_list:
                if self.positions_list[new_y][new_x] == current_position + 1:
                    score = self.get_trailhead_score_puzzle_1(new_x, new_y, score, visited_trailheads_list)

            # try to go left
            new_x, new_y = x - 1, y
            if self.position_within_mapped_area(new_y, new_x) and (new_x, new_y) not in visited_trailheads_list:
                if self.positions_list[new_y][new_x] == current_position + 1:
                    score = self.get_trailhead_score_puzzle_1(new_x, new_y, score, visited_trailheads_list)

            # try to go right
            new_x, new_y = x + 1, y
            if self.position_within_mapped_area(new_y, new_x) and (new_x, new_y) not in visited_trailheads_list:
                if self.positions_list[new_y][new_x] == current_position + 1:
                    score = self.get_trailhead_score_puzzle_1(new_x, new_y, score, visited_trailheads_list)

        return score

    def get_trailhead_score_puzzle_2(self, x, y, score=0):
        current_position = self.positions_list[y][x]
        if self.use_example:
            print((x, y), current_position)

        # check if current position is 9
        if self.positions_list[y][x] == 9:
            score += 1
            if self.use_example:
                print('sub score:', score)
        else:
            # try to go up
            new_x, new_y = x, y - 1
            if self.position_within_mapped_area(new_y, new_x):
                if self.positions_list[new_y][new_x] == current_position + 1:
                    score = self.get_trailhead_score_puzzle_2(new_x, new_y, score)

            # try to go down
            new_x, new_y = x, y + 1
            if self.position_within_mapped_area(new_y, new_x):
                if self.positions_list[new_y][new_x] == current_position + 1:
                    score = self.get_trailhead_score_puzzle_2(new_x, new_y, score)

            # try to go left
            new_x, new_y = x - 1, y
            if self.position_within_mapped_area(new_y, new_x):
                if self.positions_list[new_y][new_x] == current_position + 1:
                    score = self.get_trailhead_score_puzzle_2(new_x, new_y, score)

            # try to go right
            new_x, new_y = x + 1, y
            if self.position_within_mapped_area(new_y, new_x):
                if self.positions_list[new_y][new_x] == current_position + 1:
                    score = self.get_trailhead_score_puzzle_2(new_x, new_y, score)

        return score

    def solve_part_1(self):
        for trailhead in self.trailheads_list:
            x, y = trailhead
            score = self.get_trailhead_score_puzzle_1(x, y, 0, [])
            if self.use_example:
                print('score:', (x, y), score)
            self.result_puzzle_1 += score

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        for trailhead in self.trailheads_list:
            x, y = trailhead
            score = self.get_trailhead_score_puzzle_2(x, y, 0)
            if self.use_example:
                print('score:', (x, y), score)
            self.result_puzzle_2 += score

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
