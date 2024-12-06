class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

        self.obstacles_list = []
        self.starting_position = None
        for y, line in enumerate(self.lines_list):
            for x, i in enumerate(line):
                if i == '^':
                    self.starting_position = (x, y)
                elif i == '#':
                    self.obstacles_list.append((x, y))

        self.width = len(self.lines_list[0])
        self.length = len(self.lines_list)

        self.current_position = self.starting_position
        self.starting_direction = 'up'
        self.current_direction = self.starting_direction

        self.visited_positions_list_puzzle_1 = [self.starting_position]
        self.visited_positions_directions_list_puzzle_2 = []
        self.newly_placed_obstacles_list_puzzle_2 = []

    def current_position_within_mapped_area(self):
        x, y = self.current_position
        if 0 <= x < self.width:
            if 0 <= y < self.length:
                return True

    def move_up(self, x, y, obstacles_list):
        if (x, y - 1) not in obstacles_list:
            self.current_position = (x, y - 1)
        else:
            self.current_direction = 'right'

    def move_right(self, x, y, obstacles_list):
        if (x + 1, y) not in obstacles_list:
            self.current_position = (x + 1, y)
        else:
            self.current_direction = 'down'

    def move_down(self, x, y, obstacles_list):
        if (x, y + 1) not in obstacles_list:
            self.current_position = (x, y + 1)
        else:
            self.current_direction = 'left'

    def move_left(self, x, y, obstacles_list):
        if (x - 1, y) not in obstacles_list:
            self.current_position = (x - 1, y)
        else:
            self.current_direction = 'up'

    def move_position(self, obstacles_list):
        x, y = self.current_position

        if self.current_direction == 'up':
            self.move_up(x, y, obstacles_list)
        elif self.current_direction == 'right':
            self.move_right(x, y, obstacles_list)
        elif self.current_direction == 'down':
            self.move_down(x, y, obstacles_list)
        else:
            self.move_left(x, y, obstacles_list)

    def solve_part_1(self):
        while self.current_position_within_mapped_area():
            self.visited_positions_list_puzzle_1.append(self.current_position)
            self.move_position(self.obstacles_list)

        self.result_puzzle_1 = len(list(set(self.visited_positions_list_puzzle_1)))

        return f'\nResult puzzle 1: {self.result_puzzle_1}\n'

    def new_obstacle_causes_loop(self, obstacles_list):
        while self.current_position_within_mapped_area():
            current_position_direction = (*self.current_position, self.current_direction)
            if current_position_direction in self.visited_positions_directions_list_puzzle_2:
                return True
            else:
                self.visited_positions_directions_list_puzzle_2.append(current_position_direction)

            self.move_position(obstacles_list)

    def solve_part_2(self):
        for y, line in enumerate(self.lines_list):
            for x, i in enumerate(line):
                if (x, y) not in self.obstacles_list and (x, y) not in self.starting_position:
                    # reset variables
                    self.current_position = self.starting_position
                    self.current_direction = self.starting_direction
                    self.visited_positions_directions_list_puzzle_2 = []

                    new_obstacle = (x, y)
                    if self.new_obstacle_causes_loop(self.obstacles_list + [new_obstacle]):
                        self.newly_placed_obstacles_list_puzzle_2.append((x, y))

        self.result_puzzle_2 = len(list(set(self.newly_placed_obstacles_list_puzzle_2)))

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


# puzzle = AdventOfCode('example.txt')
puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
