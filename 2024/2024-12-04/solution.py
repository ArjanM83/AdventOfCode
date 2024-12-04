class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.xmas_x_y_list = []

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def get_xmas_horizontal(self, line, y):
        count_xmas = 0
        for x, i in enumerate(line):
            if i == 'X':
                if x <= (len(line) - 4):
                    if line[x + 1] == 'M' and line[x + 2] == 'A' and line[x + 3] == 'S':
                        count_xmas += 1
                        self.xmas_x_y_list.append((x, y))
                        self.xmas_x_y_list.append((x + 1, y))
                        self.xmas_x_y_list.append((x + 2, y))
                        self.xmas_x_y_list.append((x + 3, y))
                if x >= 3:
                    if line[x - 1] == 'M' and line[x - 2] == 'A' and line[x - 3] == 'S':
                        count_xmas += 1
                        self.xmas_x_y_list.append((x, y))
                        self.xmas_x_y_list.append((x - 1, y))
                        self.xmas_x_y_list.append((x - 2, y))
                        self.xmas_x_y_list.append((x - 3, y))

        return count_xmas

    def get_xmas_vertical(self, line, y):
        count_xmas = 0
        for x, i in enumerate(line):
            if i == 'X':
                if y <= (len(self.lines_list) - 4):
                    if (self.lines_list[y + 1][x] == 'M'
                            and self.lines_list[y + 2][x] == 'A' and self.lines_list[y + 3][x] == 'S'):
                        count_xmas += 1
                        self.xmas_x_y_list.append((x, y))
                        self.xmas_x_y_list.append((x, y + 1))
                        self.xmas_x_y_list.append((x, y + 2))
                        self.xmas_x_y_list.append((x, y + 3))
                if y >= 3:
                    if (self.lines_list[y - 1][x] == 'M'
                            and self.lines_list[y - 2][x] == 'A' and self.lines_list[y - 3][x] == 'S'):
                        count_xmas += 1
                        self.xmas_x_y_list.append((x, len(self.lines_list) - y))
                        self.xmas_x_y_list.append((x, len(self.lines_list) - y + 1))
                        self.xmas_x_y_list.append((x, len(self.lines_list) - y + 2))
                        self.xmas_x_y_list.append((x, len(self.lines_list) - y + 3))

        return count_xmas

    def get_xmas_diagonal(self, line, y):
        count_xmas = 0
        for x, i in enumerate(line):
            if i == 'X':
                if y <= (len(self.lines_list) - 4):  # down
                    # down right
                    if x <= (len(line) - 4):
                        if (self.lines_list[y + 1][x + 1] == 'M'
                                and self.lines_list[y + 2][x + 2] == 'A' and self.lines_list[y + 3][x + 3] == 'S'):
                            count_xmas += 1
                            self.xmas_x_y_list.append((x, y))
                            self.xmas_x_y_list.append((x + 1, y + 1))
                            self.xmas_x_y_list.append((x + 2, y + 2))
                            self.xmas_x_y_list.append((x + 3, y + 3))
                    # down right
                    if x >= 3:
                        if (self.lines_list[y + 1][x - 1] == 'M'
                                and self.lines_list[y + 2][x - 2] == 'A' and self.lines_list[y + 3][x - 3] == 'S'):
                            count_xmas += 1
                            self.xmas_x_y_list.append((x, y))
                            self.xmas_x_y_list.append((x - 1, y + 1))
                            self.xmas_x_y_list.append((x - 2, y + 2))
                            self.xmas_x_y_list.append((x - 3, y + 3))
                if y >= 3:  # up
                    # up right
                    if x <= (len(line) - 4):
                        if (self.lines_list[y - 1][x + 1] == 'M'
                                and self.lines_list[y - 2][x + 2] == 'A' and self.lines_list[y - 3][x + 3] == 'S'):
                            count_xmas += 1
                            self.xmas_x_y_list.append((x, y))
                            self.xmas_x_y_list.append((x + 1, y - 1))
                            self.xmas_x_y_list.append((x + 2, y - 2))
                            self.xmas_x_y_list.append((x + 3, y - 3))
                    # up right
                    if x >= 3:
                        if (self.lines_list[y - 1][x - 1] == 'M'
                                and self.lines_list[y - 2][x - 2] == 'A' and self.lines_list[y - 3][x - 3] == 'S'):
                            count_xmas += 1
                            self.xmas_x_y_list.append((x, y))
                            self.xmas_x_y_list.append((x - 1, y - 1))
                            self.xmas_x_y_list.append((x - 2, y - 2))
                            self.xmas_x_y_list.append((x - 3, y - 3))

        return count_xmas

    def print_part_1(self):
        for y, line in enumerate(self.lines_list):
            line_print = ''
            for x, i in enumerate(line):
                if (x, y) in self.xmas_x_y_list:
                    line_print += i
                else:
                    line_print += '.'
            print(line_print)

    def count_x_mas(self):
        for y, line in enumerate(self.lines_list):
            for x, i in enumerate(line):
                if i == 'A':
                    x_mas_counter = 0
                    if 1 <= x <= (len(line) - 2) and 1 <= y <= (len(self.lines_list) - 2):
                        # upper left to lower right
                        if self.lines_list[y - 1][x - 1] == 'M' and self.lines_list[y + 1][x + 1] == 'S':
                            x_mas_counter += 1
                        # upper right to lower left
                        if self.lines_list[y - 1][x + 1] == 'M' and self.lines_list[y + 1][x - 1] == 'S':
                            x_mas_counter += 1
                        # lower left to upper right
                        if self.lines_list[y + 1][x - 1] == 'M' and self.lines_list[y - 1][x + 1] == 'S':
                            x_mas_counter += 1
                        # lower right to upper left
                        if self.lines_list[y + 1][x + 1] == 'M' and self.lines_list[y - 1][x - 1] == 'S':
                            x_mas_counter += 1

                    if x_mas_counter == 2:
                        self.result_puzzle_2 += 1

    def solve_part_1(self):
        for y, line in enumerate(self.lines_list):
            self.result_puzzle_1 += self.get_xmas_horizontal(line, y)
            self.result_puzzle_1 += self.get_xmas_vertical(line, y)
            self.result_puzzle_1 += self.get_xmas_diagonal(line, y)

        self.xmas_x_y_list = list(set(self.xmas_x_y_list))
        self.print_part_1()

        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        self.count_x_mas()

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
