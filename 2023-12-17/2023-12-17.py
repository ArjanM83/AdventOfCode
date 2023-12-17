import sys


class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        sys.setrecursionlimit(10000)

        self.width = len(self.lines_list[0])
        self.height = len(self.lines_list)
        self.end_location = self.get_location_id(len(self.lines_list[0]) - 1, len(self.lines_list) - 1)

        self.lowest_heat_loss_puzzle_1 = self.calculate_lowest_heat_loss()
        self.location_heat_loss_dict_puzzle_1 = {self.end_location: self.lowest_heat_loss_puzzle_1}
        self.location_heat_loss_dict_puzzle_2 = {}
        self.location_last_three_directions_heat_loss_dict = {}
        self.location_last_ten_directions_heat_loss_dict = {}

    def get_possible_directions_list_puzzle_1(
            self, current_x, current_y, previous_x, previous_y, last_three_directions_string, heat_loss):
        possible_directions_list = []
        directions_list = []
        width = len(self.lines_list[0])
        height = len(self.lines_list)

        forbidden_direction = ''
        if last_three_directions_string == 'lll':
            forbidden_direction = 'l'
        elif last_three_directions_string == 'rrr':
            forbidden_direction = 'r'
        elif last_three_directions_string == 'uuu':
            forbidden_direction = 'u'
        elif last_three_directions_string == 'ddd':
            forbidden_direction = 'd'

        if current_x == 0:
            if current_y == 0:  # 0,0
                if previous_x != 0:
                    possible_directions_list.append('d')
                if previous_x != 1:
                    possible_directions_list.append('r')
            elif current_y == height - 1:  # 0,height
                if previous_x != 0:
                    possible_directions_list.append('u')
                if previous_x != 1:
                    possible_directions_list.append('r')
            else:  # 0,middle
                if current_y != previous_y:
                    possible_directions_list.append('r')
                if current_y != previous_y + 1:
                    possible_directions_list.append('u')
                if current_y != previous_y - 1:
                    possible_directions_list.append('d')
        elif current_x == width - 1:
            if current_y == 0:  # width,0
                if previous_y != 0:
                    possible_directions_list.append('l')
                if previous_y != 1:
                    possible_directions_list.append('d')
            elif current_y == height - 1:  # width,height
                if previous_x != width - 2:
                    possible_directions_list.append('l')
                if previous_y != height - 2:
                    possible_directions_list.append('u')
            else:  # width,middle
                if current_y != previous_y:
                    possible_directions_list.append('l')
                if current_y != previous_y + 1:
                    possible_directions_list.append('u')
                if current_y != previous_y - 1:
                    possible_directions_list.append('d')
        else:
            if current_y == 0:  # middle,0
                if previous_x != current_x - 1:
                    possible_directions_list.append('l')
                if previous_x != current_x + 1:
                    possible_directions_list.append('r')
                if previous_x != current_x:
                    possible_directions_list.append('d')
            elif current_y == height - 1:  # middle,height
                if previous_x != current_x - 1:
                    possible_directions_list.append('l')
                if previous_x != current_x + 1:
                    possible_directions_list.append('r')
                if previous_x != current_x:
                    possible_directions_list.append('u')
            else:  # middle,middle
                if previous_x != current_x - 1:
                    possible_directions_list.append('l')
                if previous_x != current_x + 1:
                    possible_directions_list.append('r')
                if previous_y != current_y - 1:
                    possible_directions_list.append('u')
                if previous_y != current_y + 1:
                    possible_directions_list.append('d')

        location_id = self.get_location_id(current_x, current_y)
        for possible_direction in possible_directions_list:
            if possible_direction != forbidden_direction:
                location_last_three_directions_id = f'{location_id}_{last_three_directions_string}'
                if location_last_three_directions_id not in self.location_last_three_directions_heat_loss_dict:
                    directions_list.append(possible_direction)
                else:
                    if heat_loss < self.location_last_three_directions_heat_loss_dict[
                            location_last_three_directions_id]:
                        directions_list.append(possible_direction)

        return directions_list

    def get_possible_directions_list_puzzle_2(
            self, current_x, current_y, previous_x, previous_y, last_ten_directions_string, heat_loss):
        possible_directions_dict = {}
        directions_list = []

        current_direction = last_ten_directions_string[9]
        direction_counter = 0
        for direction_index in range(9, -1, -1):
            if current_direction == last_ten_directions_string[direction_index]:
                direction_counter += 1
            else:
                break

        forbidden_directions_dict = {}
        change_forbidden = False
        if direction_counter < 4:
            if current_direction == '.':
                pass
            else:
                change_forbidden = True
        elif direction_counter == 10:
            if last_ten_directions_string == 'llllllllll':
                forbidden_directions_dict['l'] = True
            elif last_ten_directions_string == 'rrrrrrrrrr':
                forbidden_directions_dict['r'] = True
            elif last_ten_directions_string == 'uuuuuuuuuu':
                forbidden_directions_dict['u'] = True
            elif last_ten_directions_string == 'dddddddddd':
                forbidden_directions_dict['d'] = True
        else:
            if current_x > self.width - 1 - 4:
                if current_direction != 'r':
                    forbidden_directions_dict['r'] = True
            if current_x < 4:
                if current_direction != 'l':
                    forbidden_directions_dict['l'] = True
            if current_y > self.height - 1 - 4:
                if current_direction != 'd':
                    forbidden_directions_dict['d'] = True
            if current_y < 4:
                if current_direction != 'u':
                    forbidden_directions_dict['u'] = True

        if current_x == 0:
            if current_y == 0:  # 0,0
                if previous_x != 0:
                    possible_directions_dict['d'] = True
                if previous_x != 1:
                    possible_directions_dict['r'] = True
            elif current_y == self.height - 1:  # 0,height
                if previous_x != 0:
                    possible_directions_dict['u'] = True
                if previous_x != 1:
                    possible_directions_dict['r'] = True
            else:  # 0,middle
                if current_y != previous_y:
                    possible_directions_dict['r'] = True
                if current_y != previous_y + 1:
                    possible_directions_dict['u'] = True
                if current_y != previous_y - 1:
                    possible_directions_dict['d'] = True
        elif current_x == self.width - 1:
            if current_y == 0:  # width,0
                if previous_y != 0:
                    possible_directions_dict['l'] = True
                if previous_y != 1:
                    possible_directions_dict['d'] = True
            elif current_y == self.height - 1:  # width,height
                if previous_x != self.width - 2:
                    possible_directions_dict['l'] = True
                if previous_y != self.height - 2:
                    possible_directions_dict['u'] = True
            else:  # width,middle
                if current_y != previous_y:
                    possible_directions_dict['l'] = True
                if current_y != previous_y + 1:
                    possible_directions_dict['u'] = True
                if current_y != previous_y - 1:
                    possible_directions_dict['d'] = True
        else:
            if current_y == 0:  # middle,0
                if previous_x != current_x - 1:
                    possible_directions_dict['l'] = True
                if previous_x != current_x + 1:
                    possible_directions_dict['r'] = True
                if previous_x != current_x:
                    possible_directions_dict['d'] = True
            elif current_y == self.height - 1:  # middle,height
                if previous_x != current_x - 1:
                    possible_directions_dict['l'] = True
                if previous_x != current_x + 1:
                    possible_directions_dict['r'] = True
                if previous_x != current_x:
                    possible_directions_dict['u'] = True
            else:  # middle,middle
                if previous_x != current_x - 1:
                    possible_directions_dict['l'] = True
                if previous_x != current_x + 1:
                    possible_directions_dict['r'] = True
                if previous_y != current_y - 1:
                    possible_directions_dict['u'] = True
                if previous_y != current_y + 1:
                    possible_directions_dict['d'] = True

        location_id = self.get_location_id(current_x, current_y)

        if change_forbidden:
            if current_direction in possible_directions_dict:
                return [current_direction]
            
        for possible_direction in possible_directions_dict:
            if possible_direction not in forbidden_directions_dict:
                location_last_ten_directions_id = f'{location_id}_{last_ten_directions_string}'
                if location_last_ten_directions_id not in self.location_last_ten_directions_heat_loss_dict:
                    directions_list.append(possible_direction)
                else:
                    if heat_loss < self.location_last_ten_directions_heat_loss_dict[location_last_ten_directions_id]:
                        directions_list.append(possible_direction)

        return directions_list

    @staticmethod
    def get_next_step_coordinates(x_coordinate, y_coordinate, direction):
        if direction == 'l':
            return x_coordinate - 1, y_coordinate
        elif direction == 'r':
            return x_coordinate + 1, y_coordinate
        elif direction == 'u':
            return x_coordinate, y_coordinate - 1
        else:
            return x_coordinate, y_coordinate + 1

    @staticmethod
    def get_location_id(x_coordinate, y_coordinate):
        return f'{x_coordinate}_{y_coordinate}'

    def calculate_heat_loss_paths_puzzle_1(self, current_x, current_y, previous_x, previous_y,
                                           last_three_directions_string, heat_loss):
        directions_list = self.get_possible_directions_list_puzzle_1(
            current_x, current_y, previous_x, previous_y, last_three_directions_string, heat_loss)

        for direction in directions_list:
            new_x, new_y = self.get_next_step_coordinates(current_x, current_y, direction)
            new_heat_loss = heat_loss + int(self.lines_list[new_y][new_x])
            lowest_heat_loss = self.location_heat_loss_dict_puzzle_1.get(self.end_location)

            if new_heat_loss < lowest_heat_loss:
                new_last_three_directions_string = last_three_directions_string[-2:] + direction
                location_id = self.get_location_id(current_x, current_y)

                new_location_id = self.get_location_id(new_x, new_y)
                if new_location_id in self.location_heat_loss_dict_puzzle_1:
                    if new_heat_loss < self.location_heat_loss_dict_puzzle_1[new_location_id]:
                        self.location_heat_loss_dict_puzzle_1[new_location_id] = new_heat_loss
                else:
                    self.location_heat_loss_dict_puzzle_1[new_location_id] = new_heat_loss

                location_last_three_directions_id = f'{location_id}_{last_three_directions_string}'
                if location_last_three_directions_id in self.location_last_three_directions_heat_loss_dict:
                    if heat_loss < self.location_last_three_directions_heat_loss_dict[
                            location_last_three_directions_id]:
                        self.location_last_three_directions_heat_loss_dict[location_last_three_directions_id] = (
                            heat_loss)
                else:
                    self.location_last_three_directions_heat_loss_dict[location_last_three_directions_id] = heat_loss

                self.calculate_heat_loss_paths_puzzle_1(
                    new_x, new_y, current_x, current_y, new_last_three_directions_string, new_heat_loss)

    def calculate_heat_loss_paths_puzzle_2(self, current_x, current_y, previous_x, previous_y,
                                           last_ten_directions_string, heat_loss):
        directions_list = self.get_possible_directions_list_puzzle_2(
            current_x, current_y, previous_x, previous_y, last_ten_directions_string, heat_loss)

        for direction in directions_list:
            new_x, new_y = self.get_next_step_coordinates(current_x, current_y, direction)
            new_heat_loss = heat_loss + int(self.lines_list[new_y][new_x])
            lowest_heat_loss = self.location_heat_loss_dict_puzzle_2.get(self.end_location, 1300)

            if new_heat_loss < lowest_heat_loss:
                new_last_ten_directions_string = last_ten_directions_string[-9:] + direction
                location_id = self.get_location_id(current_x, current_y)

                new_location_id = self.get_location_id(new_x, new_y)
                if new_location_id in self.location_heat_loss_dict_puzzle_2:
                    if new_heat_loss < self.location_heat_loss_dict_puzzle_2[new_location_id]:
                        self.location_heat_loss_dict_puzzle_2[new_location_id] = new_heat_loss
                else:
                    self.location_heat_loss_dict_puzzle_2[new_location_id] = new_heat_loss

                location_last_ten_directions_id = f'{location_id}_{last_ten_directions_string}'
                if location_last_ten_directions_id in self.location_last_ten_directions_heat_loss_dict:
                    if heat_loss < self.location_last_ten_directions_heat_loss_dict[location_last_ten_directions_id]:
                        self.location_last_ten_directions_heat_loss_dict[location_last_ten_directions_id] = heat_loss
                else:
                    self.location_last_ten_directions_heat_loss_dict[location_last_ten_directions_id] = heat_loss

                self.calculate_heat_loss_paths_puzzle_2(
                    new_x, new_y, current_x, current_y, new_last_ten_directions_string, new_heat_loss)

    def calculate_lowest_heat_loss(self):
        lowest_heat_loss = 0
        for character_index, _ in enumerate(self.lines_list[0]):
            if character_index < self.width - 1:
                lowest_heat_loss += int(self.lines_list[character_index][character_index+1])
            lowest_heat_loss += int(self.lines_list[character_index][character_index])

        return lowest_heat_loss

    def solve_part_1(self):
        self.calculate_heat_loss_paths_puzzle_1(0, 0, -1, -1, '...', 0)
        end_location = self.get_location_id(self.width - 1, self.height - 1)
        return 'puzzle 1:', self.location_heat_loss_dict_puzzle_1[end_location]

    def solve_part_2(self):
        self.calculate_heat_loss_paths_puzzle_2(0, 0, -1, -1, '..........', 0)
        end_location = self.get_location_id(self.width - 1, self.height - 1)
        return 'puzzle 2:', self.location_heat_loss_dict_puzzle_2[end_location]


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
