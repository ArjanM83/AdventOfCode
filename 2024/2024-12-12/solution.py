from queue import Queue


class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.width = len(self.lines_list[0])
        self.height = len(self.lines_list)

        self.region_coordinates_lists_list = []

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    def position_within_mapped_area(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def get_area_perimeter_and_coordinates_list_for_region(self, x, y):
        coordinates_list = []
        area = 0
        perimeter = 0

        region_character = self.lines_list[y][x]
        visited_coordinates_list = []
        to_visit_queue = Queue()
        to_visit_queue.put((x, y))

        while not to_visit_queue.empty():
            coordinate_x, coordinate_y = to_visit_queue.get()
            if (coordinate_x, coordinate_y) in visited_coordinates_list:
                continue

            visited_coordinates_list.append((coordinate_x, coordinate_y))
            coordinates_list.append((coordinate_x, coordinate_y))
            area += 1

            # Check neighbors
            for diff_x, diff_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = coordinate_x + diff_x, coordinate_y + diff_y
                if self.position_within_mapped_area(new_x, new_y):
                    if self.lines_list[new_y][new_x] == region_character:
                        if (new_x, new_y) not in visited_coordinates_list:
                            to_visit_queue.put((new_x, new_y))
                    else:
                        # Different character next door
                        perimeter += 1
                else:
                    # End of the map
                    perimeter += 1

        return area, perimeter, coordinates_list

    @staticmethod
    def get_area_sides_for_region(region_coordinates_list):
        area = len(region_coordinates_list)
        total_sides = 0

        return area, total_sides

    @staticmethod
    def get_price_puzzle_1(area, perimeter):
        return area * perimeter

    @staticmethod
    def get_price_puzzle_2(area, sides):
        return area * sides

    def solve_part_1(self):
        visited_regions_coordinates_set = set()

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) not in visited_regions_coordinates_set:
                    area, perimeter, coordinates_list = self.get_area_perimeter_and_coordinates_list_for_region(x, y)
                    for coordinates in coordinates_list:
                        visited_regions_coordinates_set.add(coordinates)
                    self.result_puzzle_1 += self.get_price_puzzle_1(area, perimeter)

                    # store the region coordinates
                    self.region_coordinates_lists_list.append(coordinates_list)

        return f'\nResult puzzle 1: {self.result_puzzle_1}'

    def solve_part_2(self):
        for region_coordinates_list in self.region_coordinates_lists_list:
            area, sides = self.get_area_sides_for_region(region_coordinates_list)
            self.result_puzzle_2 += self.get_price_puzzle_2(area, sides)

        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
