class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.trajectories_list = []
        for line in self.lines_list:
            t_list = [int(i) for i in line.replace('@', ',').replace(' ', '').split(',')]
            t_point_1 = (t_list[0], t_list[1], t_list[2])
            t_point_2 = (t_list[0] + t_list[3], t_list[1] + t_list[4], t_list[2] + t_list[5])
            t_diff = (t_list[3], t_list[4], t_list[5])
            self.trajectories_list.append((t_point_1, t_point_2, t_diff))

    @staticmethod
    def get_line_intersection(line_a, line_b):
        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        line_a_diff = (line_a[0][0] - line_a[1][0], line_b[0][0] - line_b[1][0])
        line_b_diff = (line_a[0][1] - line_a[1][1], line_b[0][1] - line_b[1][1])

        div = det(line_a_diff, line_b_diff)
        if div == 0:
            return 0, 0
        else:
            d = (det(*line_a), det(*line_b))
            x = det(d, line_a_diff) / div
            y = det(d, line_b_diff) / div
            return x, y

    @staticmethod
    def intersection_in_the_past(line, intersection, diff):
        if ((line[0][0] > intersection[0] and diff[0] >= 0) or (line[0][0] < intersection[0] and diff[0] <= 0) or
                (line[0][1] > intersection[1] and diff[1] >= 0) or (line[0][1] < intersection[1] and diff[1] <= 0)):
            return True

    def solve_part_1(self):
        sum_of_intersections = 0

        x_min = 7
        x_min = 200000000000000
        x_max = 27
        x_max = 400000000000000
        y_min = 7
        y_min = 200000000000000
        y_max = 27
        y_max = 400000000000000

        for t_a_index, trajectory_a in enumerate(self.trajectories_list):
            for t_b_index, trajectory_b in enumerate(self.trajectories_list[t_a_index + 1:]):
                line_a = (trajectory_a[0], trajectory_a[1])
                line_a_diff = trajectory_a[2]
                line_b = (trajectory_b[0], trajectory_b[1])
                line_b_diff = trajectory_b[2]

                line_intersection = self.get_line_intersection(line_a, line_b)
                if line_intersection == (0, 0):
                    print('never', line_a[0], line_b[0], line_intersection)
                elif (x_min <= line_intersection[0] <= x_max) and (y_min <= line_intersection[1] <= y_max):
                    if (self.intersection_in_the_past(line_a, line_intersection, line_a_diff) or
                            self.intersection_in_the_past(line_b, line_intersection, line_b_diff)):
                        print('in the past', line_a[0], line_b[0], line_intersection)
                    else:
                        print('inside', line_a[0], line_b[0], line_intersection)
                        sum_of_intersections += 1
                else:
                    print('outside', line_a[0], line_b[0], line_intersection)

        return sum_of_intersections

    @staticmethod
    def solve_part_2():
        return 0


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
