class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.bricks_list = []
        for line in self.lines_list:
            self.bricks_list.append([int(i) for i in line.replace('~', ',').split(',')])

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
            for sb in self.bricks_list:
                sz = self.get_brick_max_z(sb)
                # supporting brick highest point is 1 below brick's lowest point
                if z == sz + 1:
                    if self.bricks_have_x_y_overlap(b, sb):
                        return None

            # no overlap: brick can fall down at least 1 step
            return self.get_brick_z_decrement(b)

    @staticmethod
    def get_brick_min_z(b):
        return min(b[2], b[5])

    @staticmethod
    def get_brick_max_z(b):
        return max(b[2], b[5])

    @staticmethod
    def get_brick_z_decrement(b):
        return [b[0], b[1], b[2] - 1, b[3], b[4], b[5] - 1]

    def bricks_fall_downward(self):
        another_brick_fell_down = True

        while another_brick_fell_down:
            another_brick_fell_down = False

            for check_brick in self.bricks_list:
                fallen_down_brick = self.get_fallen_down_new_brick(check_brick)

                if fallen_down_brick:
                    # print(check_brick, 'fell down into', fallen_down_brick)
                    another_brick_fell_down = True
                    new_bricks_list = []

                    for original_brick in self.bricks_list:
                        if original_brick != check_brick:
                            new_bricks_list.append(original_brick)
                        else:
                            new_bricks_list.append(fallen_down_brick)

                    self.bricks_list = new_bricks_list
                    break

        # print('bricks stopped falling down')

    def solve_part_1(self):
        sum_of_bricks = 0

        self.bricks_fall_downward()

        for brick in self.bricks_list:
            above_supported_bricks = self.get_above_supported_bricks(brick)
            if not above_supported_bricks:
                print(brick, ': no supported bricks')
                sum_of_bricks += 1
            else:
                all_above_bricks_supported_by_multiple_bricks = True
                for above_supported_brick in above_supported_bricks:
                    if not self.below_supported_by_multiple_bricks(above_supported_brick):
                        # print('brick', above_supported_brick, 'is not below supported by multiple bricks')
                        all_above_bricks_supported_by_multiple_bricks = False
                        break

                if all_above_bricks_supported_by_multiple_bricks:
                    print(brick, ': all above supported by multiple bricks')
                    sum_of_bricks += 1
                else:
                    print(brick, ': not all above supported by multiple bricks')

        return sum_of_bricks

    @staticmethod
    def solve_part_2():
        return 0


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
