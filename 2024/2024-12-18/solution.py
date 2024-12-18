from collections import deque


class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.coordinates_list = []
        for line in self.lines_list:
            self.coordinates_list.append((int(line.split(',')[0]), int(line.split(',')[1])))

        if self.use_example:
            self.width = 7
            self.height = 7
            self.bytes = 12
        else:
            self.width = 71
            self.height = 71
            self.bytes = 1024

        self.start_position = (0, 0)
        self.exit_position = (self.width - 1, self.height - 1)

        if self.use_example:
            print('coordinates list:', self.coordinates_list)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def position_within_mapped_area(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_minimum_steps_to_exit(self, x, y, corrupted_coordinates_list):
        queue = deque([(x, y, 0)])  # (current x, current y, current steps)
        visited = set()
        visited.add((x, y))

        while queue:
            current_x, current_y, steps = queue.popleft()

            if (current_x, current_y) == self.exit_position:
                return steps
            else:
                for x_diff, y_diff in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    new_x = current_x + x_diff
                    new_y = current_y + y_diff

                    if self.position_within_mapped_area(new_x, new_y):
                        if (new_x, new_y) not in visited and (new_x, new_y) not in corrupted_coordinates_list:
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y, steps + 1))

    def route_to_exit_is_possible(self, x, y, corrupted_coordinates_list):
        queue = deque([(x, y)])
        visited = {(x, y)}

        while queue:
            current_x, current_y = queue.popleft()

            if (current_x, current_y) == self.exit_position:
                return True

            for x_diff, y_diff in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_x = current_x + x_diff
                new_y = current_y + y_diff

                if self.position_within_mapped_area(new_x, new_y):
                    if (new_x, new_y) not in visited and (new_x, new_y) not in corrupted_coordinates_list:
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))

    def solve_part_1(self):
        x, y = self.start_position
        self.result_puzzle_1 = self.get_minimum_steps_to_exit(x, y, self.coordinates_list[:self.bytes])
        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def solve_part_2(self):
        x, y = self.start_position
        for i in range(len(self.coordinates_list)):
            if self.use_example:
                print('using coordinates list:', self.coordinates_list[:-(i+1)])

            if not self.route_to_exit_is_possible(x, y, self.coordinates_list[:-(i+1)]):
                if self.use_example:
                    print(self.coordinates_list[len(self.coordinates_list)-(i+1)])
            else:
                coordinates = self.coordinates_list[len(self.coordinates_list)-(i+1)]
                self.result_puzzle_2 = f'{coordinates[0]},{coordinates[1]}'
                break

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
