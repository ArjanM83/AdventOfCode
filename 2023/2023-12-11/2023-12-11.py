class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()
            self.universe_with_expanded_rows_list_puzzle_1 = []
            self.universe_with_expanded_rows_list_puzzle_2 = []
            self.universe_with_expanded_columns = []
            self.universe_list = []
            self.galaxy_coordinates_dict = {}

        self.rows_to_expand_list_puzzle_1 = []
        self.rows_to_expand_list_puzzle_2 = []
        self.columns_to_expand_list_puzzle_1 = []
        self.columns_to_expand_list_puzzle_2 = []

    def solve_part_1(self):
        # find rows to expand
        for line_index, line in enumerate(self.lines_list):
            if len(line) == line.count('.'):
                self.rows_to_expand_list_puzzle_1.append(line_index)

        # find columns to expand
        for column_id, character in enumerate(self.lines_list[0]):
            expand_column = True
            for line_index, line in enumerate(self.lines_list):
                if line[column_id] != '.':
                    expand_column = False
            if expand_column:
                self.columns_to_expand_list_puzzle_1.append(column_id)

        # # create galaxy with expanded rows
        for line_index, line in enumerate(self.lines_list):
            self.universe_with_expanded_rows_list_puzzle_1.append(line)
            if line_index in self.rows_to_expand_list_puzzle_1:
                self.universe_with_expanded_rows_list_puzzle_1.append(line)

        # create galaxy with expanded columns
        for line_index, line in enumerate(self.universe_with_expanded_rows_list_puzzle_1):
            new_line = ''
            for character_index, character in enumerate(line):
                new_line += character
                if character_index in self.columns_to_expand_list_puzzle_1:
                    new_line += character
            self.universe_with_expanded_columns.append(new_line)

        # new universe
        self.universe_list = self.universe_with_expanded_columns

        # print universe
        for line in self.universe_list:
            print(line)

        # create galaxies dict
        galaxy_id = 1
        for line_index, line in enumerate(self.universe_list):
            for character_index, character in enumerate(line):
                if character == '#':
                    self.galaxy_coordinates_dict[galaxy_id] = [line_index, character_index]
                    galaxy_id += 1

        # get number of pairs
        galaxies_list = list(self.galaxy_coordinates_dict.keys())
        galaxy_pairs = ([(a, b) for idx, a in enumerate(galaxies_list) for b in galaxies_list[idx + 1:]])

        # get the shortest paths
        sum_of_shortest_paths = 0
        for galaxy_index, galaxy_pair in enumerate(galaxy_pairs):
            galaxy_id_1 = galaxy_pair[0]
            galaxy_id_2 = galaxy_pair[1]

            g_1_x_coordinate = self.galaxy_coordinates_dict[galaxy_id_1][0]
            g_1_y_coordinate = self.galaxy_coordinates_dict[galaxy_id_1][1]
            g_2_x_coordinate = self.galaxy_coordinates_dict[galaxy_id_2][0]
            g_2_y_coordinate = self.galaxy_coordinates_dict[galaxy_id_2][1]

            x_difference = abs(g_1_x_coordinate - g_2_x_coordinate)
            y_difference = abs(g_1_y_coordinate - g_2_y_coordinate)

            shortest_path = x_difference + y_difference
            sum_of_shortest_paths += shortest_path

        print(self.galaxy_coordinates_dict)

        return sum_of_shortest_paths

    def solve_part_2(self):
        # expand universe
        expand_universe_factor = 999999

        # find rows to expand
        for line_index, line in enumerate(self.lines_list):
            if len(line) == line.count('.'):
                self.rows_to_expand_list_puzzle_2.append(line_index)

        # find columns to expand
        for column_id, character in enumerate(self.lines_list[0]):
            expand_column = True
            for line_index, line in enumerate(self.lines_list):
                if line[column_id] != '.':
                    expand_column = False
            if expand_column:
                self.columns_to_expand_list_puzzle_2.append(column_id)

        # # create galaxy with expanded rows
        for line_index, line in enumerate(self.lines_list):
            self.universe_with_expanded_rows_list_puzzle_2.append(line)
            if line_index in self.rows_to_expand_list_puzzle_2:
                for i in range(expand_universe_factor):
                    self.universe_with_expanded_rows_list_puzzle_2.append(line)

        # new universe
        self.universe_list = self.universe_with_expanded_rows_list_puzzle_2

        # create galaxies dict
        galaxy_id = 1
        for line_index, line in enumerate(self.universe_list):
            for character_index, character in enumerate(line):
                if character == '#':
                    self.galaxy_coordinates_dict[galaxy_id] = [line_index, character_index]
                    galaxy_id += 1

        # get number of pairs
        galaxies_list = list(self.galaxy_coordinates_dict.keys())
        galaxy_pairs = ([(a, b) for idx, a in enumerate(galaxies_list) for b in galaxies_list[idx + 1:]])

        # get the shortest paths
        sum_of_shortest_paths = 0
        for galaxy_index, galaxy_pair in enumerate(galaxy_pairs):
            galaxy_id_1 = galaxy_pair[0]
            galaxy_id_2 = galaxy_pair[1]

            g_1_x_coordinate = self.galaxy_coordinates_dict[galaxy_id_1][0]
            g_1_y_coordinate = self.galaxy_coordinates_dict[galaxy_id_1][1]
            g_2_x_coordinate = self.galaxy_coordinates_dict[galaxy_id_2][0]
            g_2_y_coordinate = self.galaxy_coordinates_dict[galaxy_id_2][1]

            expand_x = 0
            for column_id in self.columns_to_expand_list_puzzle_2:
                if ((g_1_y_coordinate < column_id < g_2_y_coordinate) or
                        (g_2_y_coordinate < column_id < g_1_y_coordinate)):
                    expand_x += 1

            x_difference = abs(g_1_x_coordinate - g_2_x_coordinate)
            y_difference = abs(g_1_y_coordinate - g_2_y_coordinate) + (expand_x * expand_universe_factor)

            shortest_path = x_difference + y_difference
            sum_of_shortest_paths += shortest_path

        print(self.galaxy_coordinates_dict)

        return sum_of_shortest_paths


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
