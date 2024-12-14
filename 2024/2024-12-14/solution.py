class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.robots_dict = {}
        robot_id_counter = 0
        for line in self.lines_list:
            position, velocity = line.replace('p=', '').replace('v=', '').split(' ')
            position_x = int(position.split(',')[0])
            position_y = int(position.split(',')[1])
            velocity_x = int(velocity.split(',')[0])
            velocity_y = int(velocity.split(',')[1])
            self.robots_dict[robot_id_counter] = {
                'p_x': position_x,
                'p_y': position_y,
                'v_x': velocity_x,
                'v_y': velocity_y
            }
            robot_id_counter += 1

        self.width = 101
        self.height = 103

        if self.use_example:
            print('robots:', self.robots_dict)
            print('width:', self.width, 'height', self.height)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def get_next_position(self, p_x, p_y, v_x, v_y):
        next_p_x = p_x + v_x
        if next_p_x > (self.width - 1):
            next_p_x = next_p_x - self.width
        elif next_p_x < 0:
            next_p_x = self.width + next_p_x

        next_p_y = p_y + v_y
        if next_p_y > (self.height - 1):
            next_p_y = next_p_y - self.height
        elif next_p_y < 0:
            next_p_y = self.height + next_p_y

        return next_p_x, next_p_y

    def get_current_quadrant(self, p_x, p_y):
        if p_x < int(self.width / 2):
            if p_y < int(self.height / 2):
                return 1
            elif p_y > int(self.height / 2):
                return 3
        elif p_x > int(self.width / 2):
            if p_y < int(self.height / 2):
                return 2
            elif p_y > int(self.height / 2):
                return 4

    def detect_christmas_tree(self, robots_dict):
        print_xmas_tree = False

        lines_list = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                line.append(' ')
            lines_list.append(line)

        for robot_id in robots_dict:
            robot_dict = robots_dict[robot_id]
            p_x = robot_dict['p_x']
            p_y = robot_dict['p_y']
            lines_list[p_y][p_x] = '.'

        print_lines_list = []
        for line in lines_list:
            print_line = ''.join(line)
            print_lines_list.append(print_line)

            if '...............................' in print_line:
                print_xmas_tree = True

        if print_xmas_tree:
            for print_line in print_lines_list:
                print(print_line)

            return True

    def solve_part_1(self):
        robots_dict_puzzle_1 = self.robots_dict.copy()
        quadrants_list_dict = {1: [], 2: [], 3: [], 4: []}
        seconds = 100

        for robot_id in robots_dict_puzzle_1:
            robot_dict = robots_dict_puzzle_1[robot_id].copy()
            v_x = robot_dict['v_x']
            v_y = robot_dict['v_y']

            for i in range(seconds):
                robot_dict['p_x'], robot_dict['p_y'] = self.get_next_position(
                    robot_dict['p_x'], robot_dict['p_y'], v_x, v_y)

            current_quadrant = self.get_current_quadrant(robot_dict['p_x'], robot_dict['p_y'])
            if current_quadrant:
                quadrants_list_dict[current_quadrant].append(robot_id)

        if self.use_example:
            print(f'robots after {seconds} seconds:', robots_dict_puzzle_1)
            print('quadrants:', quadrants_list_dict)

        self.result_puzzle_1 = 1
        for quadrant in quadrants_list_dict:
            self.result_puzzle_1 *= len(quadrants_list_dict[quadrant])

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        robots_dict_puzzle_2 = self.robots_dict.copy()
        seconds = 100000

        for i in range(seconds):
            for robot_id in robots_dict_puzzle_2:
                robot_dict = robots_dict_puzzle_2[robot_id]
                v_x = robot_dict['v_x']
                v_y = robot_dict['v_y']

                robot_dict['p_x'], robot_dict['p_y'] = self.get_next_position(
                    robot_dict['p_x'], robot_dict['p_y'], v_x, v_y)

            if self.detect_christmas_tree(robots_dict_puzzle_2):
                self.result_puzzle_2 = i + 1
                return f'\nResult puzzle 2: {self.result_puzzle_2}'
                # 6416 = too low


example = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
