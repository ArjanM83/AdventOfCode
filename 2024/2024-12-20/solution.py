class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = True

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        for y, line in enumerate(self.lines_list):
            if self.use_example:
                print(line)
            for x, i in enumerate(line):
                if i == 'S':
                    self.start_position = (x, y)
                elif i == 'E':
                    self.end_position = (x, y)

        print('\nstart position:', self.start_position)
        print('end position:', self.end_position)

        self.track_list = self.get_track_list()
        if self.use_example:
            print('track_list', self.track_list)

        self.track_list_time = len(self.track_list) - 1
        print('track list total time:', self.track_list_time)

        self.width = len(self.lines_list[0])
        self.length = len(self.lines_list)

        self.puzzle_2_found_cheats_set = set()

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def position_within_mapped_area(self, x, y):
        if 0 <= x < self.width:
            if 0 <= y < self.length:
                return True

    def get_track_list(self):
        track_list = [self.start_position]
        x, y = self.start_position

        while (x, y) != self.end_position:
            if self.use_example:
                print('x, y:', x, y)
            for new_x, new_y in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                if self.lines_list[new_y][new_x] in ['.', 'E'] and (new_x, new_y) not in track_list:
                    track_list.append((new_x, new_y))
                    x, y = new_x, new_y
                    break

        return track_list

    def get_number_of_cheats_puzzle_1(self, minimal_save=0):
        number_of_cheats = 0

        for index, position in enumerate(self.track_list):
            x, y = position

            for new_x, new_y in [(x, y - 2), (x, y + 2), (x - 2, y), (x + 2, y)]:
                new_position = (new_x, new_y)
                if new_position in self.track_list:
                    new_position_index = self.track_list.index(new_position)
                    save_ms = new_position_index - index - 2
                    if save_ms >= minimal_save:
                        number_of_cheats += 1

        return number_of_cheats

    def cheat_with_steps(
            self, start_index, start_pos, current_position, steps_taken, found_cheats_set, minimal_save=0, visited=None
    ):
        if visited is None:
            visited = set()

        if steps_taken == 20:
            return

        # visited position and steps taken
        if (current_position, steps_taken) in visited:
            return
        else:
            visited.add((current_position, steps_taken))

        x, y = current_position
        for new_x, new_y in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if self.position_within_mapped_area(new_x, new_y):
                new_position = (new_x, new_y)

                if self.lines_list[new_y][new_x] in ['.', 'E']:
                    # Potential end of cheat
                    if new_position in self.track_list:
                        new_position_index = self.track_list.index(new_position)
                        save_ms = (new_position_index - start_index) - (steps_taken + 1)
                        if save_ms >= minimal_save:
                            found_cheats_set.add((self.track_list[start_index], new_position))

                    # Also continue from this track cell if we want, since we might find other endings
                    self.cheat_with_steps(
                        start_index, start_pos, new_position, steps_taken + 1, found_cheats_set, minimal_save, visited)
                else:  # cell == '#'
                    self.cheat_with_steps(
                        start_index, start_pos, new_position, steps_taken + 1, found_cheats_set, minimal_save, visited)

    def get_number_of_cheats_puzzle_2(self, minimal_save=0):
        for index, position in enumerate(self.track_list):
            self.cheat_with_steps(index, position, position, 0, self.puzzle_2_found_cheats_set, minimal_save)

        return len(self.puzzle_2_found_cheats_set)

    def solve_part_1(self):
        self.result_puzzle_1 = self.get_number_of_cheats_puzzle_1(100)

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        self.result_puzzle_2 = self.get_number_of_cheats_puzzle_2(100)

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
