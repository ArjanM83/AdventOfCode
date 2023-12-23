from copy import deepcopy


class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.max_z = 0
        self.bricks_list = []
        self.bricks_min_z_dict = {}
        self.bricks_max_z_dict = {}
        for line in self.lines_list:
            brick = [int(i) for i in line.replace('~', ',').split(',')]
            max_z = self.get_brick_max_z(brick)

            if max_z > self.max_z:
                self.max_z = max_z

            self.bricks_list.append(brick)

        for z in range(1, self.max_z + 1):
            self.bricks_min_z_dict[z] = []
            self.bricks_max_z_dict[z] = []

        for brick in self.bricks_list:
            self.bricks_min_z_dict[self.get_brick_min_z(brick)].append(brick)
            self.bricks_max_z_dict[self.get_brick_max_z(brick)].append(brick)

    @staticmethod
    def bricks_have_x_y_overlap(b, sb):
        x_1, y_1, z_1, x_2, y_2, z_2 = b[0], b[1], b[2], b[3], b[4], b[5]
        sx_1, sy_1, sz_1, sx_2, sy_2, sz_2 = sb[0], sb[1], sb[2], sb[3], sb[4], sb[5]

        for x in range(x_1, x_2 + 1):
            for y in range(y_1, y_2 + 1):
                if (sx_1 <= x <= sx_2) and (sy_1 <= y <= sy_2):
                    return True

    def get_above_supported_bricks(self, b):
        above_supported_bricks_list = []
        z = self.get_brick_max_z(b)

        for sb in self.bricks_list:
            sz = self.get_brick_min_z(sb)
            # supporting brick lowest point is 1 above brick's highest point: could be supporting
            if z == sz - 1:
                if self.bricks_have_x_y_overlap(b, sb):
                    above_supported_bricks_list.append(sb)

        return above_supported_bricks_list

    def below_supported_by_multiple_bricks(self, b):
        below_supported_bricks = 0
        z = self.get_brick_min_z(b)

        for sb in self.bricks_list:
            sz = self.get_brick_max_z(sb)
            # supporting brick highest point is 1 below brick's lowest point
            if z == sz + 1:
                if self.bricks_have_x_y_overlap(b, sb):
                    below_supported_bricks += 1

                    if below_supported_bricks > 1:
                        return True

        return False

    def get_fallen_down_new_brick(self, b):
        z = self.get_brick_min_z(b)

        # bricks cannot fall down endlessly
        if z > 1:
            for sb in self.bricks_max_z_dict[z - 1]:
                if self.bricks_have_x_y_overlap(b, sb):
                    return None

            # no overlap: brick can fall down at least 1 step
            return self.get_brick_z_decrement(b)

    def get_final_fallen_down_new_brick(self, b):
        current_fallen_down_new_brick = self.get_fallen_down_new_brick(b)
        last_fallen_down_new_brick = current_fallen_down_new_brick

        while current_fallen_down_new_brick:
            current_fallen_down_new_brick = self.get_fallen_down_new_brick(current_fallen_down_new_brick)

            if current_fallen_down_new_brick:
                last_fallen_down_new_brick = current_fallen_down_new_brick

        return last_fallen_down_new_brick

    @staticmethod
    def get_brick_min_z(b):
        return min(b[2], b[5])

    @staticmethod
    def get_brick_max_z(b):
        return max(b[2], b[5])

    @staticmethod
    def get_brick_z_decrement(b):
        return [b[0], b[1], b[2] - 1, b[3], b[4], b[5] - 1]

    def update_brick(self, original_brick, updated_brick):
        updated_bricks_list = []

        for brick in self.bricks_list:
            if brick != original_brick:
                updated_bricks_list.append(brick)
            else:
                updated_bricks_list.append(updated_brick)

        self.bricks_list = updated_bricks_list

        original_min_z = self.get_brick_min_z(original_brick)
        original_max_z = self.get_brick_max_z(original_brick)
        updated_min_z = self.get_brick_min_z(updated_brick)
        updated_max_z = self.get_brick_max_z(updated_brick)

        self.bricks_min_z_dict[original_min_z].remove(original_brick)
        self.bricks_max_z_dict[original_max_z].remove(original_brick)

        self.bricks_min_z_dict[updated_min_z].append(updated_brick)
        self.bricks_max_z_dict[updated_max_z].append(updated_brick)

    def remove_brick(self, brick):
        self.bricks_list.remove(brick)

        min_z = self.get_brick_min_z(brick)
        max_z = self.get_brick_max_z(brick)

        self.bricks_min_z_dict[min_z].remove(brick)
        self.bricks_max_z_dict[max_z].remove(brick)

    def add_brick(self, brick):
        self.bricks_list.append(brick)

        min_z = self.get_brick_min_z(brick)
        max_z = self.get_brick_max_z(brick)

        self.bricks_min_z_dict[min_z].append(brick)
        self.bricks_max_z_dict[max_z].append(brick)

    def bricks_fall_downward(self):
        bricks_max_z_dict_copy = deepcopy(self.bricks_max_z_dict)

        for z in range(1, self.max_z + 1):
            for brick in bricks_max_z_dict_copy[z]:
                fallen_down_brick = self.get_final_fallen_down_new_brick(brick)

                if fallen_down_brick:
                    print(brick, 'fell down into', fallen_down_brick)
                    self.update_brick(brick, fallen_down_brick)

    def get_above_supported_bricks_that_would_fall(self):
        falling_brick_list = []
        bricks_max_z_dict_copy = deepcopy(self.bricks_max_z_dict)

        for z in range(1, self.max_z + 1):
            for brick in bricks_max_z_dict_copy[z]:
                fallen_down_brick = self.get_final_fallen_down_new_brick(brick)

                if fallen_down_brick:
                    falling_brick_list.append(brick)
                    self.update_brick(brick, fallen_down_brick)

        return falling_brick_list

    def solve_part_1(self):
        sum_of_bricks = 0

        self.bricks_fall_downward()

        for brick in self.bricks_list:
            above_supported_bricks = self.get_above_supported_bricks(brick)
            if not above_supported_bricks:
                print(brick, ': no above supported bricks')
                sum_of_bricks += 1
            else:
                all_above_bricks_supported_by_multiple_bricks = True
                for above_supported_brick in above_supported_bricks:
                    if not self.below_supported_by_multiple_bricks(above_supported_brick):
                        all_above_bricks_supported_by_multiple_bricks = False
                        break

                if all_above_bricks_supported_by_multiple_bricks:
                    print(brick, ': all above supported by multiple bricks')
                    sum_of_bricks += 1
                else:
                    print(brick, ': not all above supported by multiple bricks')

        print('final brick list:', self.bricks_list)

        return sum_of_bricks

    def solve_part_2(self):
        sum_of_bricks = 0
        copy_of_bricks_list = self.bricks_list.copy()
        copy_of_bricks_min_z_dict = deepcopy(self.bricks_min_z_dict)
        copy_of_bricks_max_z_dict = deepcopy(self.bricks_max_z_dict)

        for brick in copy_of_bricks_list:
            # reset state
            self.bricks_list = copy_of_bricks_list.copy()
            self.bricks_min_z_dict = deepcopy(copy_of_bricks_min_z_dict)
            self.bricks_max_z_dict = deepcopy(copy_of_bricks_max_z_dict)

            self.remove_brick(brick)
            number_of_bricks_that_would_fall = len(self.get_above_supported_bricks_that_would_fall())
            sum_of_bricks += number_of_bricks_that_would_fall

        return sum_of_bricks


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
