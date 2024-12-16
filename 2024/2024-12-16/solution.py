class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.position_start = None
        self.position_end = None
        self.visited_position_direction_list_dict = {}
        for y, line in enumerate(self.lines_list):
            for x, i in enumerate(line):
                if i == 'S':
                    self.position_start = (x, y)
                elif i == 'E':
                    self.position_end = (x, y)

                # Initialize visited directions for each position
                if (x, y) not in self.visited_position_direction_list_dict:
                    self.visited_position_direction_list_dict[(x, y)] = {}
                for direction in ['up', 'down', 'left', 'right']:
                    # Store best known score for each direction at (x,y)
                    self.visited_position_direction_list_dict[(x, y)][direction] = None

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

        # Set that contains all positions of all minimal score paths
        self.lowest_score_positions_set = set()

    def get_score(self, x, y, direction='right', score=0, lowest_score=0, path=None):
        if path is None:
            path = []
        path = path + [(x, y)]

        # Prune route if walking in circles
        best_score_at_this_position = self.visited_position_direction_list_dict[(x, y)][direction]
        if best_score_at_this_position is not None and best_score_at_this_position < score:
            return score, lowest_score

        self.visited_position_direction_list_dict[(x, y)][direction] = score

        # Reached the end
        if (x, y) == self.position_end:
            if lowest_score == 0 or score < lowest_score:
                lowest_score = score
                self.lowest_score_positions_set = set(path)
                if self.use_example:
                    print('new lowest score:', score)
            elif score == lowest_score:
                self.lowest_score_positions_set = self.lowest_score_positions_set.union(path)

            return score, lowest_score

        # Abandon too costly paths
        if lowest_score != 0 and score >= lowest_score:
            return score, lowest_score

        # Try to go left
        new_x, new_y = x - 1, y
        if self.lines_list[new_y][new_x] in ['.', 'E']:
            temp_score, temp_lowest = None, None
            if direction == 'up':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'left', score + 1001, lowest_score, path)
            elif direction == 'down':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'left', score + 1001, lowest_score, path)
            elif direction == 'left':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'left', score + 1, lowest_score, path)

            if temp_lowest is not None and (lowest_score == 0 or temp_lowest < lowest_score):
                lowest_score = temp_lowest

        # Try to go right
        new_x, new_y = x + 1, y
        if self.lines_list[new_y][new_x] in ['.', 'E']:
            temp_score, temp_lowest = None, None
            if direction == 'up':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'right', score + 1001, lowest_score, path)
            elif direction == 'down':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'right', score + 1001, lowest_score, path)
            elif direction == 'right':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'right', score + 1, lowest_score, path)

            if temp_lowest is not None and (lowest_score == 0 or temp_lowest < lowest_score):
                lowest_score = temp_lowest

        # Try to go up
        new_x, new_y = x, y - 1
        if self.lines_list[new_y][new_x] in ['.', 'E']:
            temp_score, temp_lowest = None, None
            if direction == 'left':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'up', score + 1001, lowest_score, path)
            elif direction == 'right':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'up', score + 1001, lowest_score, path)
            elif direction == 'up':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'up', score + 1, lowest_score, path)

            if temp_lowest is not None and (lowest_score == 0 or temp_lowest < lowest_score):
                lowest_score = temp_lowest

        # Try to go down
        new_x, new_y = x, y + 1
        if self.lines_list[new_y][new_x] in ['.', 'E']:
            temp_score, temp_lowest = None, None
            if direction == 'left':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'down', score + 1001, lowest_score, path)
            elif direction == 'right':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'down', score + 1001, lowest_score, path)
            elif direction == 'down':
                temp_score, temp_lowest = self.get_score(new_x, new_y, 'down', score + 1, lowest_score, path)

            if temp_lowest is not None and (lowest_score == 0 or temp_lowest < lowest_score):
                lowest_score = temp_lowest

        return score, lowest_score

    def solve_part_1(self):
        x, y = self.position_start
        score, lowest_score = self.get_score(x, y, 'right', 0, 100000)

        self.result_puzzle_1 = lowest_score

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        self.result_puzzle_2 = len(self.lowest_score_positions_set)

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


# Example input for testing
example = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
