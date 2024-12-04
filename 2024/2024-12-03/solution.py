class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    @staticmethod
    def get_numbers_tuple_list(input_list):
        numbers_tuple_list = []

        for line in input_list:
            mul_string_list = line.split('mul(')

            for mul_string in mul_string_list:
                number_1 = ''
                number_2 = ''
                number_1_active = True
                corrupt = False
                for i in mul_string:
                    if not corrupt:
                        if number_1_active:
                            if i.isdigit() and len(number_1) <= 2:
                                number_1 += i
                            elif i == ',' and 1 <= len(number_1) <= 3:
                                number_1_active = False
                            else:
                                corrupt = True
                        elif not number_1_active:
                            if i.isdigit() and len(number_2) <= 2:
                                number_2 += i
                            elif i == ')' and 1 <= len(number_2) <= 3:
                                numbers_tuple_list.append((int(number_1), int(number_2)))
                                corrupt = True
                            else:
                                corrupt = True
                        else:
                            corrupt = True

        return numbers_tuple_list

    def get_do_mul_list(self):
        one_big_line = ''
        for line in self.lines_list:
            one_big_line += line

        starting_with_do_list = one_big_line.split('do()')
        only_do_list = []

        for do_string in starting_with_do_list:
            if "don't()" in do_string:
                only_do_list.append(do_string[:do_string.find("don't()")])
            else:
                only_do_list.append(do_string)

        return only_do_list

    def solve_part_1(self):
        numbers_tuple_list = self.get_numbers_tuple_list(self.lines_list)
        for numbers_tuple in numbers_tuple_list:
            self.result_puzzle_1 += numbers_tuple[0] * numbers_tuple[1]

        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        do_mul_list = self.get_do_mul_list()

        for do_string in do_mul_list:
            print(do_string)

        numbers_tuple_list = self.get_numbers_tuple_list(do_mul_list)
        print(numbers_tuple_list)
        for numbers_tuple in numbers_tuple_list:
            self.result_puzzle_2 += numbers_tuple[0] * numbers_tuple[1]

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
