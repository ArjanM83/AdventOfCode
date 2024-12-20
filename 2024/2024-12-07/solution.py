class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]

        # input
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.adjusted_lines_list = []
        for line in self.lines_list:
            test_value, remaining_numbers = line.split(': ')
            remaining_numbers_list = remaining_numbers.split(' ')
            self.adjusted_lines_list.append([int(test_value)] + [int(i) for i in remaining_numbers_list])

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def equation_can_be_made_true(self, test_value, numbers_list, current_number=0, index=0, append=False):
        if index == len(numbers_list):
            return current_number == test_value

        # Add
        if self.equation_can_be_made_true(
                test_value, numbers_list, current_number + numbers_list[index], index + 1, append=append):
            return True

        # Multiply
        if self.equation_can_be_made_true(
                test_value, numbers_list, current_number * numbers_list[index], index + 1, append=append):
            return True

        # Append
        if append:
            appended_value = int(str(current_number) + str(numbers_list[index]))
            if self.equation_can_be_made_true(test_value, numbers_list, appended_value, index + 1, append=append):
                return True

        return False

    def solve_part_1(self):
        for line_list in self.adjusted_lines_list:
            test_value = line_list[0]
            numbers_list = line_list[1:]

            if self.equation_can_be_made_true(test_value, numbers_list):
                self.result_puzzle_1 += line_list[0]

        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        for line_list in self.adjusted_lines_list:
            test_value = line_list[0]
            numbers_list = line_list[1:]

            if self.equation_can_be_made_true(test_value, numbers_list, append=True):
                self.result_puzzle_2 += line_list[0]

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
