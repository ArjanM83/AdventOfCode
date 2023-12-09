class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.sum_of_puzzle_1 = 0
        self.sum_of_puzzle_2 = 0

    @staticmethod
    def get_differences_dict(line, reverse=False):
        if reverse:
            differences_dict = {0: [int(i) for i in line.split(' ')][::-1]}
        else:
            differences_dict = {0: [int(i) for i in line.split(' ')]}

        line_id = 0
        while len([i for i in differences_dict[line_id] if i != 0]) > 0:  # while not all zero's
            line_id += 1
            previous_line_id = line_id - 1
            for index, number in enumerate(differences_dict[previous_line_id]):
                if not index == len(differences_dict[previous_line_id]) - 1:
                    difference = differences_dict[previous_line_id][index + 1] - number
                    if line_id in differences_dict:
                        differences_dict[line_id].append(difference)
                    else:
                        differences_dict[line_id] = [difference]

        return differences_dict

    @staticmethod
    def get_increment(differences_dict):
        increment = differences_dict[len(differences_dict) - 2][0]
        for i in range(len(differences_dict) - 3, -1, -1):
            last_number = differences_dict[i][-1]
            increment = last_number + increment

        return increment


    def solve_part_1(self):
        for line in self.lines_list:
            increment = self.get_increment(self.get_differences_dict(line))
            self.sum_of_puzzle_1 += increment

        return f'\nResult puzzle 1: {self.sum_of_puzzle_1}\n'

    def solve_part_2(self):
        for line in self.lines_list:
            increment = self.get_increment(self.get_differences_dict(line, reverse=True))
            self.sum_of_puzzle_2 += increment

        return f'\nResult puzzle 2: {self.sum_of_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
