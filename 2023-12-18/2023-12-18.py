from datetime import datetime
from functools import cache


class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.digging_dict = {}

    def register_digging(self, current_x, current_y, direction, meters):
        new_x = current_x
        new_y = current_y

        for meter in range(meters):
            if direction == 'L':
                new_x -= 1
            elif direction == 'R':
                new_x += 1
            elif direction == 'U':
                new_y -= 1
            elif direction == 'D':
                new_y += 1

            if new_y in self.digging_dict:
                self.digging_dict[new_y][new_x] = True
            else:
                self.digging_dict[new_y] = {new_x: True}

        return new_x, new_y

    def print_digging(self):
        y_min = 0
        y_max = 0
        x_min = 0
        x_max = 0
        for y_index, y_key in enumerate(sorted(self.digging_dict.keys())):
            # y min and y max
            if y_key < y_min:
                y_min = y_key
            if y_key > y_max:
                y_max = y_key

            # x min and x max
            sorted_x_keys = sorted(self.digging_dict[y_key].keys())
            if sorted_x_keys[0] < x_min:
                x_min = sorted_x_keys[0]
            if sorted_x_keys[-1] > x_max:
                x_max = sorted_x_keys[-1]

        for y_key in range(y_min, y_max + 1):
            line_string = ''
            for x_key in range(x_min, x_max + 1):
                if y_key in self.digging_dict:
                    if x_key in self.digging_dict[y_key]:
                        line_string += '#'
                    else:
                        line_string += '.'
                else:
                    line_string += '#'

            # print(line_string, self.get_cubic_meters_from_line(y_key))

    def get_cubic_meters_from_line(self, y_key):
        sorted_x_key_list = sorted(self.digging_dict[y_key].keys())

        cubic_meters = 0
        connection_above_active = False
        connection_below_active = False
        x_key_start = None
        for x_key in sorted_x_key_list:
            # coming from below
            if (y_key + 1) in self.digging_dict:
                if x_key in self.digging_dict[y_key + 1]:
                    if not connection_below_active:
                        connection_below_active = True
                        if not connection_above_active:
                            x_key_start = x_key
                    else:
                        connection_below_active = False
                        if not connection_above_active:
                            cubic_meters += x_key - x_key_start + 1

            # coming from above
            if (y_key - 1) in self.digging_dict:
                if x_key in self.digging_dict[y_key - 1]:
                    if not connection_above_active:
                        connection_above_active = True
                        if not connection_below_active:
                            x_key_start = x_key
                    else:
                        connection_above_active = False
                        if not connection_below_active:
                            cubic_meters += x_key - x_key_start + 1

        return cubic_meters

    @cache
    def get_direction_from_hex(self, hex_direction):
        if hex_direction == '0':
            return 'R'
        elif hex_direction == '1':
            return 'D'
        elif hex_direction == '2':
            return 'L'
        elif hex_direction == '3':
            return 'U'

    def solve_part_1(self):
        current_x = 0
        current_y = 0

        for line_index, line in enumerate(self.lines_list):
            direction, meters, color = line.split(' ')
            meters = int(meters)

            current_x, current_y = self.register_digging(current_x, current_y, direction, meters)

        cubic_meters = 0
        for y_key in sorted(self.digging_dict.keys()):
            cubic_meters += self.get_cubic_meters_from_line(y_key)

        self.print_digging()

        return '\npuzzle 1: ', cubic_meters

    def solve_part_2(self):
        self.digging_dict = {}
        current_x = 0
        current_y = 0

        for line_index, line in enumerate(self.lines_list):
            _, _, hex_string = line.split(' ')
            hex_meters = hex_string[2:7]
            hex_direction = hex_string[-2:-1]
            direction = self.get_direction_from_hex(hex_direction)
            meters = int(f'0x{hex_meters}', 0)

            current_x, current_y = self.register_digging(current_x, current_y, direction, meters)

        cubic_meters = 0
        iterations = len(self.digging_dict)
        iteration_check = 1000000
        for y_index, y_key in enumerate(sorted(self.digging_dict.keys())):
            if y_index % iteration_check == 0:
                datetime_now = datetime.now()
                print(f'{datetime_now} - {y_index}/{iterations} - {round((y_index/iterations * 100), 1)}%')

            cubic_meters += self.get_cubic_meters_from_line(y_key)

        return '\npuzzle 2: ', cubic_meters


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
