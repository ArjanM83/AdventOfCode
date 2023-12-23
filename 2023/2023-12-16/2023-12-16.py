class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()
            
        self.process_beam_list = []
        self.beam_dict = {}

        # puzzle 2
        self.max_energized_tiles = 0
        self.winning_x_coordinate = 0
        self.winning_y_coordinate = 0
        self.winning_direction = ''
        self.winning_dict = {}

    @staticmethod
    def get_coordinate_key(x_coordinate, y_coordinate):
        return f'{x_coordinate}_{y_coordinate}'

    def process_beam(self, x_coordinate, y_coordinate, direction):
        tile = self.lines_list[y_coordinate][x_coordinate]

        if tile == '.':
            if direction == 'left':
                self.process_beam_list.append([x_coordinate - 1, y_coordinate, direction])
            elif direction == 'right':
                self.process_beam_list.append([x_coordinate + 1, y_coordinate, direction])
            elif direction == 'up':
                self.process_beam_list.append([x_coordinate, y_coordinate - 1, direction])
            elif direction == 'down':
                self.process_beam_list.append([x_coordinate, y_coordinate + 1, direction])
        elif tile == '-':
            if direction == 'left':
                self.process_beam_list.append([x_coordinate - 1, y_coordinate, direction])
            elif direction == 'right':
                self.process_beam_list.append([x_coordinate + 1, y_coordinate, direction])
            elif direction == 'up':
                self.process_beam_list.append([x_coordinate - 1, y_coordinate, 'left'])
                self.process_beam_list.append([x_coordinate + 1, y_coordinate, 'right'])
            elif direction == 'down':
                self.process_beam_list.append([x_coordinate - 1, y_coordinate, 'left'])
                self.process_beam_list.append([x_coordinate + 1, y_coordinate, 'right'])
        elif tile == '|':
            if direction == 'left':
                self.process_beam_list.append([x_coordinate, y_coordinate - 1, 'up'])
                self.process_beam_list.append([x_coordinate, y_coordinate - 1, 'up'])
                self.process_beam_list.append([x_coordinate, y_coordinate + 1, 'down'])
                self.process_beam_list.append([x_coordinate, y_coordinate + 1, 'down'])
            elif direction == 'right':
                self.process_beam_list.append([x_coordinate, y_coordinate - 1, 'up'])
                self.process_beam_list.append([x_coordinate, y_coordinate + 1, 'down'])
            elif direction == 'up':
                self.process_beam_list.append([x_coordinate, y_coordinate - 1, direction])
            elif direction == 'down':
                self.process_beam_list.append([x_coordinate, y_coordinate + 1, direction])
        elif tile == '\\':
            if direction == 'left':
                self.process_beam_list.append([x_coordinate, y_coordinate - 1, 'up'])
            elif direction == 'right':
                self.process_beam_list.append([x_coordinate, y_coordinate + 1, 'down'])
            elif direction == 'up':
                self.process_beam_list.append([x_coordinate - 1, y_coordinate, 'left'])
            elif direction == 'down':
                self.process_beam_list.append([x_coordinate + 1, y_coordinate, 'right'])
        elif tile == '/':
            if direction == 'left':
                self.process_beam_list.append([x_coordinate, y_coordinate + 1, 'down'])
            elif direction == 'right':
                self.process_beam_list.append([x_coordinate, y_coordinate - 1, 'up'])
            elif direction == 'up':
                self.process_beam_list.append([x_coordinate + 1, y_coordinate, 'right'])
            elif direction == 'down':
                self.process_beam_list.append([x_coordinate - 1, y_coordinate, 'left'])

    def register_beam(self, x_coordinate, y_coordinate, direction):
        if 0 <= x_coordinate < len(self.lines_list[0]):
            if 0 <= y_coordinate < len(self.lines_list):
                coordinate_key = self.get_coordinate_key(x_coordinate, y_coordinate)

                if coordinate_key in self.beam_dict:
                    if direction in self.beam_dict[coordinate_key]:
                        pass
                    else:
                        self.beam_dict[coordinate_key][direction] = True
                        self.process_beam(x_coordinate, y_coordinate, direction)
                else:
                    self.beam_dict[coordinate_key] = {direction: True}
                    self.process_beam(x_coordinate, y_coordinate, direction)

    def print_beam(self, x_coordinate, y_coordinate, direction, enabled=True):
        if enabled:
            print('\n', x_coordinate, y_coordinate, direction, 'tiles energized: ', len(self.beam_dict))
            for line_index, line in enumerate(self.lines_list):
                line_print = ''

                for character_index, character in enumerate(line):
                    coordinate_key = self.get_coordinate_key(character_index, line_index)
                    if coordinate_key in self.beam_dict:
                        line_print += '#'
                    else:
                        line_print += '.'

                print(line_print)

    def set_winners_puzzle_2(self, x_coordinate, y_coordinate, direction, energized_tiles):
        self.winning_x_coordinate = x_coordinate
        self.winning_y_coordinate = y_coordinate
        self.winning_direction = direction
        self.winning_dict = self.beam_dict
        self.max_energized_tiles = energized_tiles

    def solve_part_1(self):
        x_coordinate = 0
        y_coordinate = 0
        self.register_beam(x_coordinate, y_coordinate, 'right')

        while self.process_beam_list:
            first_item = self.process_beam_list[0]
            x_coordinate = first_item[0]
            y_coordinate = first_item[1]
            direction = first_item[2]
            self.register_beam(x_coordinate, y_coordinate, direction)
            self.process_beam_list.remove(first_item)

        energized_tiles = len(self.beam_dict.keys())

        self.print_beam(x_coordinate, y_coordinate, 'right', True)

        return f'\npuzzle 1: {energized_tiles}\n'

    def process_part_2(self, x_coordinate, y_coordinate, direction):
        self.process_beam_list = []
        self.beam_dict = {}
        self.register_beam(x_coordinate, y_coordinate, direction)

        while self.process_beam_list:
            first_item = self.process_beam_list[0]
            x_coordinate = first_item[0]
            y_coordinate = first_item[1]
            direction = first_item[2]
            self.register_beam(x_coordinate, y_coordinate, direction)
            self.process_beam_list.remove(first_item)

        energized_tiles = len(self.beam_dict.keys())
        return energized_tiles

    def solve_part_2(self):
        # top edge going down + bottom edge going up
        for x_coordinate, _ in enumerate(self.lines_list[0]):
            for y_coordinate in [0, len(self.lines_list) - 1]:
                for direction in ['up', 'down']:
                    energized_tiles = self.process_part_2(x_coordinate, y_coordinate, direction)
                    if energized_tiles > self.max_energized_tiles:
                        self.set_winners_puzzle_2(x_coordinate, y_coordinate, direction, energized_tiles)

        # left edge going right + right edge going left
        for y_coordinate in range(len(self.lines_list)):
            for x_coordinate in [0, len(self.lines_list[0]) - 1]:
                for direction in ['left', 'right']:
                    energized_tiles = self.process_part_2(x_coordinate, y_coordinate, direction)
                    if energized_tiles > self.max_energized_tiles:
                        self.set_winners_puzzle_2(x_coordinate, y_coordinate, direction, energized_tiles)

        self.beam_dict = self.winning_dict
        self.print_beam(self.winning_x_coordinate, self.winning_y_coordinate, self.winning_direction)

        return f'\npuzzle 2: {self.max_energized_tiles}\n'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
