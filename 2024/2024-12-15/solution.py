class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.positions_list = []
        self.directions_list = []
        self.start_position = None
        directions_found = False
        for y, line in enumerate(self.lines_list):
            if line == '':
                directions_found = True
            if directions_found:
                if line:
                    self.directions_list.append(line)
            else:
                if not self.start_position:
                    for x, i in enumerate(line):
                        if i == '@':
                            self.start_position = (x, y)
                self.positions_list.append(line.replace('@', '.'))

        self.directions_string = ''.join(self.directions_list)

        if self.use_example:
            print('positions:', self.positions_list)
            print('directions:', self.directions_string)
            print('start position:', self.start_position)

        self.width = len(self.lines_list[0])
        self.length = len(self.lines_list)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def position_within_mapped_area(self, x, y):
        if 0 <= x < self.width:
            if 0 <= y < self.length:
                return True

    def move_box_left(self, x, y, box_x, box_y, positions_list):
        line_list = list(positions_list[box_y])

        # Identify chain of boxes
        current_x = box_x
        while current_x >= 0 and line_list[current_x] == 'O':
            current_x -= 1

        # No movement possible
        if current_x < 0 or line_list[current_x] == '#':
            return (x, y), positions_list

        # Shift left
        start_x = current_x + 1
        end_x = start_x
        while end_x < self.width and line_list[end_x] == 'O':
            end_x += 1
        end_x -= 1
        for moving_x in range(start_x, end_x + 1):
            line_list[moving_x - 1] = 'O'
            line_list[moving_x] = '.'
        positions_list[box_y] = ''.join(line_list)
        return (x - 1, y), positions_list

    def move_box_right(self, x, y, box_x, box_y, positions_list):
        line_list = list(positions_list[y])

        # Identify the chain of boxes starting at (box_x, box_y)
        current_x = box_x
        while current_x < self.width and line_list[current_x] == 'O':
            current_x += 1

        # No movement possible
        if current_x >= self.width or line_list[current_x] == '#':
            return (x, y), positions_list

        # Shift right possible
        else:
            end_x = current_x - 1  # last box position
            start_x = box_x
            for moving_x in range(end_x, start_x - 1, -1):
                line_list[moving_x + 1] = 'O'
                line_list[moving_x] = '.'

            # Update positions_list
            positions_list[box_y] = ''.join(line_list)
            return (x + 1, y), positions_list

    def move_box_up(self, x, y, box_x, box_y, positions_list):
        lines_as_lists = [list(row) for row in positions_list]
        current_y = box_y
        while current_y >= 0 and lines_as_lists[current_y][box_x] == 'O':
            current_y -= 1

        # No movement possible
        if current_y < 0 or lines_as_lists[current_y][box_x] == '#':
            return (x, y), positions_list

        # Shift up
        start_y = current_y + 1
        end_y = start_y
        while end_y < self.length and lines_as_lists[end_y][box_x] == 'O':
            end_y += 1
        end_y -= 1
        for moving_y in range(start_y, end_y + 1):
            lines_as_lists[moving_y - 1][box_x] = 'O'
            lines_as_lists[moving_y][box_x] = '.'
        positions_list = [''.join(row) for row in lines_as_lists]
        return (x, y - 1), positions_list

    def move_box_down(self, x, y, box_x, box_y, positions_list):
        lines_as_lists: list = [list(row) for row in positions_list]
        current_y = box_y
        while current_y < self.length and lines_as_lists[current_y][box_x] == 'O':
            current_y += 1

        # No movement possible
        if current_y >= self.length or lines_as_lists[current_y][box_x] == '#':
            return (x, y), positions_list

        # Shift down
        end_y = current_y - 1
        start_y = end_y
        while start_y >= 0 and lines_as_lists[start_y][box_x] == 'O':
            start_y -= 1
        start_y += 1
        for moving_y in range(end_y, start_y - 1, -1):
            lines_as_lists[moving_y + 1][box_x] = 'O'
            lines_as_lists[moving_y][box_x] = '.'
        positions_list = [''.join(row) for row in lines_as_lists]
        return (x, y + 1), positions_list

    def apply_direction(self, position, direction, positions_list):
        x, y = position

        # move left
        if direction == '<':
            if positions_list[y][x - 1] == '#':
                pass
            elif positions_list[y][x - 1] == '.':
                position = (x - 1, y)
            elif positions_list[y][x - 1] == 'O':
                position, positions_list = self.move_box_left(x, y, x - 1, y, positions_list)
        # move right
        elif direction == '>':
            if positions_list[y][x + 1] == '#':
                pass
            elif positions_list[y][x + 1] == '.':
                position = (x + 1, y)
            elif positions_list[y][x + 1] == 'O':
                position, positions_list = self.move_box_right(x, y, x + 1, y, positions_list)
        # move up
        if direction == '^':
            if positions_list[y - 1][x] == '#':
                pass
            elif positions_list[y - 1][x] == '.':
                position = (x, y - 1)
            elif positions_list[y - 1][x] == 'O':
                position, positions_list = self.move_box_up(x, y, x, y - 1, positions_list)
        # move down
        if direction == 'v':
            if positions_list[y + 1][x] == '#':
                pass
            elif positions_list[y + 1][x] == '.':
                position = (x, y + 1)
            elif positions_list[y + 1][x] == 'O':
                position, positions_list = self.move_box_down(x, y, x, y + 1, positions_list)

        return position, positions_list

    @staticmethod
    def get_gps_coordinate(x, y):
        return (100 * y) + x

    def sum_boxes_coordinates(self, positions_list):
        sum_boxes = 0
        for y, line in enumerate(positions_list):
            for x, i in enumerate(line):
                if i == 'O':
                    sum_boxes += self.get_gps_coordinate(x, y)

        return sum_boxes

    def solve_part_1(self):
        positions_list = self.positions_list.copy()
        position = self.start_position
        for direction in self.directions_string:
            position, positions_list = self.apply_direction(position, direction, positions_list)

        self.result_puzzle_1 = self.sum_boxes_coordinates(positions_list)

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
