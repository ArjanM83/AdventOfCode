class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.time_list = [int(i) for i in self.lines_list[0].split(':')[1].split(' ') if i]
        self.distance_list = [int(i) for i in self.lines_list[1].split(':')[1].split(' ') if i]

        self.result_of_puzzle_1 = 0

    @staticmethod
    def calculate_number_of_ways_to_win(time, distance):
        number_of_ways_to_win = 0

        for i in range(1, time):
            outcome = i * (time - i)
            if outcome > distance:
                number_of_ways_to_win += 1

        return number_of_ways_to_win

    def solve_part_1(self):
        for index, time in enumerate(self.time_list):
            result = self.calculate_number_of_ways_to_win(time, self.distance_list[index])

            if not self.result_of_puzzle_1:
                self.result_of_puzzle_1 = result
            else:
                self.result_of_puzzle_1 *= result

        return f'\nResult puzzle 1: {self.result_of_puzzle_1}'

    def solve_part_2(self):
        return f'\nResult puzzle 2: {self.calculate_number_of_ways_to_win(59796575, 597123410321328)}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
