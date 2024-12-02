class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.reports_line_list = []
        for line in self.lines_list:
            reports = line.split(' ')
            self.reports_line_list.append([int(i) for i in reports])

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    @staticmethod
    def difference_is_max_3(report_x, report_y):
        if abs(report_x - report_y) <= 3:
            return True

    def line_is_increasing(self, report_line):
        if (report_line[1] > report_line[0]) and self.difference_is_max_3(report_line[0], report_line[1]):
            return True
        elif (report_line[1] < report_line[0]) and self.difference_is_max_3(report_line[0], report_line[1]):
            return False
        else:
            return False

    def line_is_safe(self, report_line):
        if (report_line[1] > report_line[0]) and self.difference_is_max_3(report_line[0], report_line[1]):
            increasing = True
        elif (report_line[1] < report_line[0]) and self.difference_is_max_3(report_line[0], report_line[1]):
            increasing = False
        else:
            return False

        for index, report in enumerate(report_line):
            if index + 2 <= len(report_line) - 1:
                if self.difference_is_max_3(report_line[index + 1], report_line[index + 2]):
                    if report_line[index + 2] > report_line[index + 1] and increasing:
                        pass
                    elif report_line[index + 2] < report_line[index + 1] and not increasing:
                        pass
                    else:
                        return False
                else:
                    return False

        return True

    @staticmethod
    def remove_outlier_having_too_much_distance(report_line):
        # Check if the first element is an outlier
        if abs(report_line[0] - report_line[1]) > 3:
            return report_line[1:]

        # Check the middle elements
        for i in range(1, len(report_line) - 1):
            if abs(report_line[i] - report_line[i - 1]) > 3 and abs(report_line[i] - report_line[i + 1]) > 3:
                return report_line[:i] + report_line[i + 1:]

        # Check if the last element is an outlier
        if abs(report_line[-1] - report_line[-2]) > 3:
            return report_line[:-1]

        return report_line

    @staticmethod
    def remove_outlier_going_up_or_down(report_line):
        candidates = []

        for i in range(len(report_line)):
            test_line = report_line[:i] + report_line[i + 1:]

            is_increasing = all(test_line[j] < test_line[j + 1] for j in range(len(test_line) - 1))
            is_decreasing = all(test_line[j] > test_line[j + 1] for j in range(len(test_line) - 1))

            if is_increasing or is_decreasing:
                candidates.append(test_line)

        if candidates:
            return min(candidates, key=lambda x: report_line.index(x[0]))

        return report_line

    @staticmethod
    def remove_outlier_being_equal(report_line):
        for i in range(1, len(report_line) - 1):
            if report_line[i] == report_line[i - 1] or report_line[i] == report_line[i + 1]:
                return report_line[:i] + report_line[i + 1:]
        return report_line

    def dampener_makes_line_safe(self, report_line):
        if self.line_is_safe(self.remove_outlier_having_too_much_distance(report_line)):
            return True
        else:
            if self.line_is_safe(self.remove_outlier_going_up_or_down(report_line)):
                return True
            else:
                if self.line_is_safe(self.remove_outlier_being_equal(report_line)):
                    return True

    def solve_part_1(self):
        for report_line in self.reports_line_list:
            if self.line_is_safe(report_line):
                self.result_puzzle_1 += 1

        return f'Result puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        for index, report_line in enumerate(self.reports_line_list):
            if self.line_is_safe(report_line):
                self.result_puzzle_2 += 1
            else:
                if self.dampener_makes_line_safe(report_line):
                    self.result_puzzle_2 += 1

        return f'Result puzzle 2: {self.result_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
