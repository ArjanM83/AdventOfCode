class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.page_ordering_rules_list = []
        self.pages_to_produce_list = []
        section_two = False
        for line in self.lines_list:
            if line == '':
                section_two = True

            if not section_two:
                first_page = line.split('|')[0]
                second_page = line.split('|')[1]
                self.page_ordering_rules_list.append((first_page, second_page))
            else:
                if line:
                    self.pages_to_produce_list.append(line.split(','))

        self.pages_to_produce_list_incorrect = []

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def page_comes_after(self, first_page, second_page):
        if (first_page, second_page) in self.page_ordering_rules_list:
            return True

    def updates_are_in_the_right_order(self, updates_list):
        for index, update in enumerate(updates_list[:-1]):
            if not self.page_comes_after(update, updates_list[index + 1]):
                return False

        return True

    @staticmethod
    def get_middle_page_number(updates_list):
        return updates_list[int((len(updates_list) - 1) / 2)]

    def get_first_ordering_update(self, updates_list, corrected_updates_list):
        for first_page in updates_list:
            if first_page not in corrected_updates_list:
                first_update = True
                for second_page in updates_list:
                    if second_page != first_page and second_page not in corrected_updates_list:
                        pages_tuple = (first_page, second_page)
                        if pages_tuple not in self.page_ordering_rules_list:
                            first_update = False
                            break

                if first_update:
                    return first_page

    def get_corrected_updates_list(self, updates_list):
        corrected_updates_list = []
        for i in range(len(updates_list) - 1):
            first_update = self.get_first_ordering_update(updates_list, corrected_updates_list)
            corrected_updates_list.append(first_update)

        for last_update in updates_list:
            if last_update not in corrected_updates_list:
                corrected_updates_list.append(last_update)

        return corrected_updates_list

    def solve_part_1(self):
        for line in self.pages_to_produce_list:
            if self.updates_are_in_the_right_order(line):
                self.result_puzzle_1 += int(self.get_middle_page_number(line))
            else:
                self.pages_to_produce_list_incorrect.append(line)

        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        for line in self.pages_to_produce_list_incorrect:
            corrected_line = self.get_corrected_updates_list(line)
            self.result_puzzle_2 += int(self.get_middle_page_number(corrected_line))

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
