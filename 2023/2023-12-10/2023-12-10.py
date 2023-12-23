class AdventOfCode:
    def __init__(self, filename, use_cache=False):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.x_list = []
        for line in self.lines_list:
            self.x_list.append(line.replace('7', 'X'))

        self.direction_dict = {
            'west': ['-', 'L', 'F', 'S'],
            'east': ['-', 'J', 'X', 'S'],
            'north': ['|', 'X', 'F', 'S'],
            'south': ['|', 'L', 'J', 'S']
        }

        self.distance_dict = {}
        self.full_result_lines_list = []
        self.simplified_result_lines_list = []

        self.comma_dict = {}
        self.dot_comma_result_lines_list = []

        self.main_loop_dict = {}

        if use_cache:  # using cache for performance
            import distance_dict_cache
            self.distance_dict = distance_dict_cache.distance_dict

    def line_exists(self, line_index):
        if 0 <= line_index < len(self.x_list):
            return True

    def pipe_exists(self, pipe_index):
        if 0 <= pipe_index < len(self.x_list[0]):
            return True

    @staticmethod
    def get_character_id(line_index, character_index):
        return f'{line_index}_{character_index}'

    def get_distance(self, line_index, pipe_index):
        pipe_id = self.get_character_id(line_index, pipe_index)
        if pipe_id in self.distance_dict:
            return self.distance_dict[pipe_id]
        else:
            return -1

    def check_pipe_connection(self, line_index, pipe_index, direction):
        if self.line_exists(line_index) and self.pipe_exists(pipe_index):
            if self.x_list[line_index][pipe_index] in self.direction_dict[direction]:
                return True

    def register_new_distance(self, line_index, line):
        distance_found = False

        for pipe_index, pipe in enumerate(line):
            pipe_id = self.get_character_id(line_index, pipe_index)
            if pipe_id not in self.distance_dict:
                if pipe == 'S':
                    self.distance_dict[pipe_id] = 0
                    distance_found = True
                elif pipe == '|':
                    if (self.check_pipe_connection(line_index - 1, pipe_index, 'north') and
                            self.check_pipe_connection(line_index + 1, pipe_index, 'south')):
                        distance_neighbour = max(self.get_distance(line_index - 1, pipe_index),
                                                 self.get_distance(line_index + 1, pipe_index))
                        if distance_neighbour >= 0:
                            self.distance_dict[pipe_id] = int(distance_neighbour) + 1
                            distance_found = True
                elif pipe == '-':
                    if (self.check_pipe_connection(line_index, pipe_index - 1, 'west') and
                            self.check_pipe_connection(line_index, pipe_index + 1, 'east')):
                        distance_neighbour = max(self.get_distance(line_index, pipe_index - 1),
                                                 self.get_distance(line_index, pipe_index + 1))
                        if distance_neighbour >= 0:
                            self.distance_dict[pipe_id] = int(distance_neighbour) + 1
                            distance_found = True
                elif pipe == 'L':
                    if (self.check_pipe_connection(line_index - 1, pipe_index, 'north') and
                            self.check_pipe_connection(line_index, pipe_index + 1, 'east')):
                        distance_neighbour = max(self.get_distance(line_index - 1, pipe_index),
                                                 self.get_distance(line_index, pipe_index + 1))
                        if distance_neighbour >= 0:
                            self.distance_dict[pipe_id] = int(distance_neighbour) + 1
                            distance_found = True
                elif pipe == 'J':
                    if (self.check_pipe_connection(line_index - 1, pipe_index, 'north') and
                            self.check_pipe_connection(line_index, pipe_index - 1, 'west')):
                        distance_neighbour = max(self.get_distance(line_index - 1, pipe_index),
                                                 self.get_distance(line_index, pipe_index - 1))
                        if distance_neighbour >= 0:
                            self.distance_dict[pipe_id] = int(distance_neighbour) + 1
                            distance_found = True
                elif pipe == 'X':
                    if (self.check_pipe_connection(line_index, pipe_index - 1, 'west') and
                            self.check_pipe_connection(line_index + 1, pipe_index, 'south')):
                        distance_neighbour = max(self.get_distance(line_index, pipe_index - 1),
                                                 self.get_distance(line_index + 1, pipe_index))
                        if distance_neighbour >= 0:
                            self.distance_dict[pipe_id] = int(distance_neighbour) + 1
                            distance_found = True
                elif pipe == 'F':
                    if (self.check_pipe_connection(line_index, pipe_index + 1, 'east') and
                            self.check_pipe_connection(line_index + 1, pipe_index, 'south')):
                        distance_neighbour = max(self.get_distance(line_index, pipe_index + 1),
                                                 self.get_distance(line_index + 1, pipe_index))
                        if distance_neighbour >= 0:
                            self.distance_dict[pipe_id] = int(distance_neighbour) + 1
                            distance_found = True
                elif pipe == '.':
                    self.distance_dict[f'{line_index}_{pipe_index}'] = -1
                    distance_found = True

        if distance_found:
            return 1
        else:
            return 0

    def create_full_result_lines_list(self):
        for line_index, line in enumerate(self.x_list):
            line_composition = ''
            for pipe_index, pipe in enumerate(line):
                pipe_id = self.get_character_id(line_index, pipe_index)
                if pipe_id in self.distance_dict:
                    distance = self.distance_dict[pipe_id]
                    if distance == -1:
                        line_composition += '.'
                    else:
                        line_composition += pipe.replace('X', '7')
                else:
                    line_composition += '.'

            self.full_result_lines_list.append(line_composition)

    def create_dot_comma_result_lines_list(self):
        for line_index, line in enumerate(self.full_result_lines_list):
            line_composition = ''
            for character_index, character in enumerate(line):
                character_id = self.get_character_id(line_index, character_index)
                if character_id in self.comma_dict:
                    line_composition += ','
                else:
                    line_composition += character.replace('X', '7')

            self.dot_comma_result_lines_list.append(line_composition)

    def create_simplified_result_lines_list(self):
        for line in self.full_result_lines_list:
            self.simplified_result_lines_list.append(
                line.replace('|', 'X').replace('-', 'X').replace('L', 'X').replace('J', 'X').replace('7', 'X').
                replace('F', 'X').replace('S', 'X'))

    def register_new_comma(self, line_index, line):
        # input
        self.comma_dict['0_0'] = ','

        # example 3
        # self.comma_dict['0_19'] = ','
        # self.comma_dict['9_0'] = ','
        # self.comma_dict['9_9'] = ','
        # self.comma_dict['9_12'] = ','
        # self.comma_dict['9_19'] = ','

        connecting_dot_found = False

        for character_index, character in enumerate(line):
            if character == '.':
                character_id = self.get_character_id(line_index, character_index)
                if character_id not in self.comma_dict:
                    character_id_north = self.get_character_id(line_index - 1, character_index)
                    character_id_north_east = self.get_character_id(line_index - 1, character_index + 1)
                    character_id_east = self.get_character_id(line_index, character_index + 1)
                    character_id_east_south = self.get_character_id(line_index + 1, character_index + 1)
                    character_id_south = self.get_character_id(line_index + 1, character_index)
                    character_id_south_west = self.get_character_id(line_index + 1, character_index - 1)
                    character_id_west = self.get_character_id(line_index, character_index - 1)
                    character_id_west_north = self.get_character_id(line_index - 1, character_index - 1)
                    for adjacent_character_id in [
                        character_id_north, character_id_north_east, character_id_east, character_id_east_south,
                        character_id_south, character_id_south_west, character_id_west, character_id_west_north
                    ]:
                        if adjacent_character_id in self.comma_dict:
                            self.comma_dict[character_id] = ','
                            connecting_dot_found = True
                            break

        if connecting_dot_found:
            return 1
        else:
            return 0

    def print_visual_1(self):
        print('\n')

        for line_index, line in enumerate(self.x_list):
            print_line = ''
            for character_index, character in enumerate(line):
                character_id = self.get_character_id(line_index, character_index)
                if character_id in self.distance_dict:
                    distance = self.distance_dict[character_id]
                    if distance == -1:
                        distance = '.'
                    print_line += f'{distance}'[-1]
                else:
                    print_line += '.'
            print(print_line)

        print('\n')

    @staticmethod
    def get_line_visual(line):
        return line.replace(
            '7', '┓').replace('F', '┏').replace('J', '┛').replace('L', '┗').replace('|', '┃').replace('-', '─')

    def print_visual_2(self, version):
        print('\n')

        print_line_list = []
        if version == 'simplified':
            print_line_list = self.simplified_result_lines_list
        elif version == 'full':
            print_line_list = self.full_result_lines_list
        elif version == 'comma':
            print_line_list = self.dot_comma_result_lines_list

        print(f'version: {version}')
        for line in print_line_list:
            if version == 'comma':
                print(self.get_line_visual(line))
            else:
                print(line)

    def solve_part_1(self):
        distance_found = 1
        while distance_found > 0:
            distance_found = 0
            for index, line in enumerate(self.x_list):
                distance_found += self.register_new_distance(index, line)

        self.print_visual_1()

        return max(self.distance_dict.values())

    def solve_part_2(self):
        self.create_full_result_lines_list()
        self.create_simplified_result_lines_list()

        # create dot comma result lines list
        connecting_dot_found = 1
        while connecting_dot_found > 0:
            connecting_dot_found = 0
            for index, line in enumerate(self.simplified_result_lines_list):
                connecting_dot_found += self.register_new_comma(index, line)
        self.create_dot_comma_result_lines_list()

        self.print_visual_2('full')
        self.print_visual_2('simplified')
        self.print_visual_2('comma')
        print('\n')

        # find all enclosed tiles
        enclosed_tiles = 0
        for line_index, line in enumerate(self.dot_comma_result_lines_list):
            inside_main_loop = False
            l_active = False
            f_active = False

            for character_index, character in enumerate(line):
                character_id = self.get_character_id(line_index, character_index)

                if inside_main_loop and self.distance_dict.get(character_id, -1) == -1:
                    if character != ',':
                        enclosed_tiles += 1

                if character == 'L':
                    l_active = True

                if character == '7' and l_active:
                    if not inside_main_loop:
                        inside_main_loop = True
                    elif inside_main_loop:
                        inside_main_loop = False

                if character == 'F':
                    f_active = True

                if character == 'J' and f_active:
                    if not inside_main_loop:
                        inside_main_loop = True
                    elif inside_main_loop:
                        inside_main_loop = False

                if character != '-':
                    l_active = False
                    f_active = False

                if character == '|' and character_id in self.distance_dict:
                    if not inside_main_loop:
                        inside_main_loop = True
                    elif inside_main_loop:
                        inside_main_loop = False

        return enclosed_tiles


puzzle = AdventOfCode('input.txt', use_cache=True)
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
