class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()
            self.number_of_lines = len(self.lines_list)

        # prepare numbers for performance reasons
        self.winning_numbers_dict = {}
        self.my_numbers_dict = {}
        for line_number, line in enumerate(self.lines_list):
            winning_numbers_list, my_numbers_list = self.get_number_lists_from_card(line)
            self.winning_numbers_dict[line_number] = winning_numbers_list
            self.my_numbers_dict[line_number] = my_numbers_list

        self.cards_dict = {}

        self.sum_of_puzzle_1 = 0
        self.sum_of_puzzle_2 = 0

    @staticmethod
    def get_number_lists_from_card(line):
        numbers_string = line[line.find(':') + 2:]
        winning_numbers_string, my_numbers_string = numbers_string.split(' | ')
        winning_numbers_list = winning_numbers_string.strip().replace('  ', ' ').split(' ')
        my_numbers_list = my_numbers_string.strip().replace('  ', ' ').split(' ')

        return winning_numbers_list, my_numbers_list

    def get_number_of_matching_card_numbers(self, line_number):
        matching_card_numbers = 0

        for my_number in self.my_numbers_dict[line_number]:
            if my_number in self.winning_numbers_dict[line_number]:
                matching_card_numbers += 1

        return matching_card_numbers

    def register_winning_copies(self, card_number, matching_card_numbers):
        for i in range(matching_card_numbers):
            winning_card_number = card_number + (i + 1)

            if winning_card_number <= self.number_of_lines:
                if winning_card_number in self.cards_dict:
                    self.cards_dict[winning_card_number] += 1
                else:
                    self.cards_dict[winning_card_number] = 1

    def solve_part_1(self):
        for line_number, line in enumerate(self.lines_list):
            card_score = 0
            for i in range(self.get_number_of_matching_card_numbers(line_number)):
                if card_score == 0:
                    card_score = 1
                else:
                    card_score *= 2

            self.sum_of_puzzle_1 += card_score

        return f'\nResult puzzle 1: {self.sum_of_puzzle_1}'

    def solve_part_2(self):
        for line_number, line in enumerate(self.lines_list):
            card_number = line_number + 1

            # add original card to dict
            if card_number not in self.cards_dict:
                self.cards_dict[card_number] = 1
            else:
                self.cards_dict[card_number] += 1

            # process card and add copies to dict
            matching_card_numbers = self.get_number_of_matching_card_numbers(line_number)
            for i in range(self.cards_dict[card_number]):
                self.register_winning_copies(card_number, matching_card_numbers)

        self.sum_of_puzzle_2 = sum(self.cards_dict.values())
        return f'Result puzzle 2: {self.sum_of_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
