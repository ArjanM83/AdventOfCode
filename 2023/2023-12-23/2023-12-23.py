from functools import cache
from sys import setrecursionlimit


class AdventOfCode:
    def __init__(self, filename):
        setrecursionlimit(10000)

        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.end_position = (len(self.lines_list[0])-2, len(self.lines_list)-1)
        self.max_route_puzzle_1 = 0
        self.max_route_puzzle_2 = 0

    @cache
    def get_possible_steps(self, position, slippery_slopes=True):
        next_steps_list = []
        x, y = position[0], position[1]

        # left
        try:
            if slippery_slopes:
                if self.lines_list[y][x-1] in ['.', '<']:
                    next_steps_list.append((x-1, y))
            else:
                if self.lines_list[y][x-1] in ['.', '<', '>', '^', 'v']:
                    next_steps_list.append((x-1, y))
        except:
            pass
        # right
        try:
            if slippery_slopes:
                if self.lines_list[y][x+1] in ['.', '>']:
                    next_steps_list.append((x+1, y))
            else:
                if self.lines_list[y][x+1] in ['.', '<', '>', '^', 'v']:
                    next_steps_list.append((x+1, y))
        except:
            pass
        # up
        try:
            if slippery_slopes:
                if self.lines_list[y-1][x] in ['.', '^']:
                    next_steps_list.append((x, y-1))
            else:
                if self.lines_list[y-1][x] in ['.', '<', '>', '^', 'v']:
                    next_steps_list.append((x, y-1))
        except:
            pass
        # down
        try:
            if slippery_slopes:
                if self.lines_list[y+1][x] in ['.', 'v']:
                    next_steps_list.append((x, y+1))
            else:
                if self.lines_list[y+1][x] in ['.', '<', '>', '^', 'v']:
                    next_steps_list.append((x, y+1))
        except:
            pass

        return next_steps_list

    def walk_the_route(self, position, route_dict, slippery_slopes=True):
        possible_next_steps = self.get_possible_steps(position, slippery_slopes)
        for new_position in possible_next_steps:
            if new_position not in route_dict:
                if new_position == self.end_position:
                    route_length = len(route_dict)
                    if slippery_slopes:
                        if route_length > self.max_route_puzzle_1:
                            self.max_route_puzzle_1 = route_length
                    else:
                        if route_length > self.max_route_puzzle_2:
                            self.max_route_puzzle_2 = route_length
                            print(self.max_route_puzzle_2)
                else:
                    new_route_dict = route_dict.copy()
                    new_route_dict[new_position] = True
                    self.walk_the_route(new_position, new_route_dict, slippery_slopes)

    def solve_part_1(self):
        start_position = (1, 0)
        route_dict = {start_position: True}

        self.walk_the_route(start_position, route_dict, slippery_slopes=True)

        return self.max_route_puzzle_1

    def solve_part_2(self):
        start_position = (1, 0)
        route_dict = {start_position: True}

        self.walk_the_route(start_position, route_dict, slippery_slopes=False)

        return self.max_route_puzzle_2

puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
