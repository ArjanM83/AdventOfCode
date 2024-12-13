class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.buttons_prizes_list_puzzle_1: list = []
        prize_dict: dict = {}
        for line in self.lines_list:
            if line.startswith('Button A: X+'):
                prize_dict['A_X'], prize_dict['A_Y'] = line[12:].split(', Y+')
            elif line.startswith('Button B: X+'):
                prize_dict['B_X'], prize_dict['B_Y'] = line[12:].split(', Y+')
            elif line.startswith('Prize: X='):
                prize_dict['Prize_X'], prize_dict['Prize_Y'] = line[9:].split(', Y=')
            else:
                self.buttons_prizes_list_puzzle_1.append(prize_dict)
                prize_dict: dict = {}
        self.buttons_prizes_list_puzzle_1.append(prize_dict)

        self.buttons_prizes_list_puzzle_2 = []
        for prize_dict in self.buttons_prizes_list_puzzle_1:
            new_prize_dict: dict = prize_dict.copy()
            new_prize_dict['Prize_X'] = int(new_prize_dict['Prize_X']) + 10000000000000
            new_prize_dict['Prize_Y'] = int(new_prize_dict['Prize_Y']) + 10000000000000
            self.buttons_prizes_list_puzzle_2.append(new_prize_dict)

        if self.use_example:
            for line in self.buttons_prizes_list_puzzle_1:
                print(line)
            print('\n')
            for line in self.buttons_prizes_list_puzzle_2:
                print(line)
            print('\n')

        self.cost_a = 3
        self.cost_b = 1

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def get_minimum_tokens_puzzle_1(self, a_x, a_y, b_x, b_y, prize_x, prize_y):
        minimum_cost = None
        best_solution = None

        for a in range(101):
            if (prize_x - a_x * a) % b_x == 0:
                b = (prize_x - a_x * a) // b_x

                if a_y * a + b_y * b == prize_y and b >= 0:
                    cost = a * self.cost_a + b * self.cost_b
                    if minimum_cost is None or cost < minimum_cost:
                        minimum_cost = cost
                        best_solution = (a, b)

        if self.use_example:
            print('best solution:', best_solution, 'cost:', minimum_cost)

        return minimum_cost

    def get_minimum_tokens_puzzle_2(self, a_x, a_y, b_x, b_y, prize_x, prize_y):
        determinant = a_x * b_y - a_y * b_x
        numerator_n_a = (b_y * prize_x - b_x * prize_y)
        numerator_n_b = (-a_y * prize_x + a_x * prize_y)

        if (numerator_n_a % determinant == 0) and (numerator_n_b % determinant == 0):
            actual_value_n_a = numerator_n_a // determinant
            actual_value_n_b = numerator_n_b // determinant

            if actual_value_n_a >= 0 and actual_value_n_b >= 0:
                total_cost = self.cost_a * actual_value_n_a + self.cost_b * actual_value_n_b
                if self.use_example:
                    print('best solution:', actual_value_n_a, actual_value_n_b, 'cost:', total_cost)
                return total_cost

    @staticmethod
    def get_prize_dict_input(prize_dict):
        return (
            int(prize_dict['A_X']), int(prize_dict['A_Y']),
            int(prize_dict['B_X']), int(prize_dict['B_Y']),
            int(prize_dict['Prize_X']), int(prize_dict['Prize_Y'])
        )

    def solve_part_1(self):
        for prize_dict in self.buttons_prizes_list_puzzle_1:
            a_x, a_y, b_x, b_y, prize_x, prize_y = self.get_prize_dict_input(prize_dict)

            minimum_tokens = self.get_minimum_tokens_puzzle_1(a_x, a_y, b_x, b_y, prize_x, prize_y)
            if self.use_example:
                print(prize_dict, minimum_tokens)

            if minimum_tokens is not None:
                self.result_puzzle_1 += minimum_tokens

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        for prize_dict in self.buttons_prizes_list_puzzle_2:
            a_x, a_y, b_x, b_y, prize_x, prize_y = self.get_prize_dict_input(prize_dict)

            minimum_tokens = self.get_minimum_tokens_puzzle_2(a_x, a_y, b_x, b_y, prize_x, prize_y)
            if self.use_example:
                print(prize_dict, minimum_tokens)

            if minimum_tokens is not None:
                self.result_puzzle_2 += minimum_tokens

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
