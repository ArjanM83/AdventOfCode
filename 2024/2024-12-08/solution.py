class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        use_example = False

        # input
        if not use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.antinode_locations_list_puzzle_1 = []
        self.antinode_locations_list_puzzle_2 = []

        self.frequency_locations_list_dict: dict = {}
        for y, line in enumerate(self.lines_list):
            for x, i in enumerate(line):
                if i != '.':
                    self.antinode_locations_list_puzzle_2.append((x, y))
                    if i in self.frequency_locations_list_dict:
                        self.frequency_locations_list_dict[i].append((x, y))
                    else:
                        self.frequency_locations_list_dict[i] = [(x, y)]

        self.width = len(self.lines_list[0])
        self.length = len(self.lines_list)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def position_within_mapped_area(self, x, y):
        if 0 <= x < self.width:
            if 0 <= y < self.length:
                return True

    def add_antinode(self, location_1, location_2, antinode_locations_list):
        x_1, y_1 = location_1
        x_2, y_2 = location_2

        x_diff = abs(x_1 - x_2)
        y_diff = abs(y_1 - y_2)

        if x_1 < x_2:
            antinode_x = x_1 - x_diff
        elif x_1 > x_2:
            antinode_x = x_1 + x_diff
        else:
            antinode_x = x_1

        if y_1 < y_2:
            antinode_y = y_1 - y_diff
        elif y_1 > y_2:
            antinode_y = y_1 + y_diff
        else:
            antinode_y = y_1

        if self.position_within_mapped_area(antinode_x, antinode_y):
            antinode_locations_list.append((antinode_x, antinode_y))
            return antinode_x, antinode_y

    def add_antinode_resonance(self, location_1, location_2, antinode_locations_list):
        resonance = True
        while resonance:
            try:
                antinode = self.add_antinode(location_1, location_2, antinode_locations_list)
                location_2 = location_1
                location_1 = antinode
            except TypeError:
                resonance = False

    def add_antinodes(self, antinode_locations_list, check_for_resonance=False):
        for frequency in self.frequency_locations_list_dict:
            for frequency_location_1 in self.frequency_locations_list_dict[frequency]:
                other_locations_list = self.frequency_locations_list_dict[frequency].copy()
                other_locations_list.remove(frequency_location_1)
                for frequency_location_2 in other_locations_list:
                    if check_for_resonance:
                        self.add_antinode_resonance(frequency_location_1, frequency_location_2, antinode_locations_list)
                    else:
                        self.add_antinode(frequency_location_1, frequency_location_2, antinode_locations_list)

    def solve_part_1(self):
        self.add_antinodes(self.antinode_locations_list_puzzle_1)
        self.antinode_locations_list_puzzle_1 = list(set(self.antinode_locations_list_puzzle_1))
        self.result_puzzle_1 = len(self.antinode_locations_list_puzzle_1)

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        self.add_antinodes(self.antinode_locations_list_puzzle_2, check_for_resonance=True)
        self.antinode_locations_list_puzzle_2 = list(set(self.antinode_locations_list_puzzle_2))
        self.result_puzzle_2 = len(self.antinode_locations_list_puzzle_2)

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
