class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.star_dict = {}

        self.sum_of_part_numbers = 0
        self.sum_of_gear_ratios = 0

    def symbol_is_adjacent(self, line_number, start_position, end_position):
        for position, character in enumerate(self.lines_list[line_number]):
            if not character.isnumeric() and character != '.':
                if (start_position - 1) <= position <= (end_position + 1):
                    return True

    def is_part_number(self, line_number, start_position, end_position):
        # check previous line
        if line_number > 0:
            if self.symbol_is_adjacent(line_number - 1, start_position, end_position):
                return True

        # check current line
        if self.symbol_is_adjacent(line_number, start_position, end_position):
            return True

        # check next line
        if line_number < (len(self.lines_list) - 1):
            return self.symbol_is_adjacent(line_number + 1, start_position, end_position)

    def register_number_to_star(self, number_string, line_number, start_position, end_position):
        for position, character in enumerate(self.lines_list[line_number]):
            if character == '*':
                if (start_position - 1) <= position <= (end_position + 1):
                    star_identifier = f'{line_number - 1}_{position}'
                    if star_identifier not in self.star_dict:
                        self.star_dict[star_identifier] = [number_string]
                    else:
                        self.star_dict[star_identifier].append(number_string)

    def check_for_adjacent_star(self, number_string, line_number, start_position, end_position):
        # check previous line
        if line_number > 0:
            self.register_number_to_star(number_string, line_number - 1, start_position, end_position)

        # check current line
        self.register_number_to_star(number_string, line_number, start_position, end_position)

        # check next line
        if line_number < (len(self.lines_list) - 1):
            self.register_number_to_star(number_string, line_number + 1, start_position, end_position)

    def calculate_gear_ratios(self):
        for star_identifier in self.star_dict:
            if len(self.star_dict[star_identifier]) == 2:
                self.sum_of_gear_ratios += \
                    (int(self.star_dict[star_identifier][0]) * int(self.star_dict[star_identifier][1]))

    def solve_part_1(self):
        for line_number, line in enumerate(self.lines_list):
            number_string = ''
            start_position = None

            for position, character in enumerate(line):
                if character.isnumeric():
                    number_string = f'{number_string}{character}'
                    if not start_position:
                        start_position = position
                else:
                    if number_string:
                        end_position = position - 1
                        if self.is_part_number(line_number, start_position, end_position):
                            self.sum_of_part_numbers += int(number_string)

                        number_string = ''
                        start_position = None

            # line ended with number
            if number_string:
                end_position = len(self.lines_list[line_number])
                if self.is_part_number(line_number - 1, start_position, end_position):
                    self.sum_of_part_numbers += int(number_string)

        return f'\nResult puzzle 1: {self.sum_of_part_numbers}'

    def solve_part_2(self):
        for line_number, line in enumerate(self.lines_list):
            number_string = ''
            start_position = None

            for position, character in enumerate(line):
                if character.isnumeric():
                    number_string = f'{number_string}{character}'
                    if not start_position:
                        start_position = position
                else:
                    if number_string:
                        end_position = position - 1
                        self.check_for_adjacent_star(number_string, line_number, start_position, end_position)

                        number_string = ''
                        start_position = None

            # line ended with number
            if number_string:
                end_position = len(self.lines_list[line_number])
                self.check_for_adjacent_star(number_string, line_number, start_position, end_position)

        # calculate gear ratios
        self.calculate_gear_ratios()

        return f'\nResult puzzle 2: {self.sum_of_gear_ratios}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
