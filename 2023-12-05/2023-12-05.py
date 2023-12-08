class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.seeds_list_puzzle_1 = []

        self.seed_to_soil_map_dict = {}
        self.soil_to_fertilizer_map_dict = {}
        self.fertilizer_to_water_map_dict = {}
        self.water_to_light_map_dict = {}
        self.light_to_temperature_map_dict = {}
        self.temperature_to_humidity_map_dict = {}
        self.humidity_to_location_map_dict = {}

        self.location_number_list_puzzle_1 = []

    @staticmethod
    def get_value_from_map(map_dict, value):
        for line_number in map_dict:
            if map_dict[line_number][1] <= value <= map_dict[line_number][1] + map_dict[line_number][2] - 1:
                return value - map_dict[line_number][1] + map_dict[line_number][0]
        return value

    def solve_part_1(self):
        for line_number, line in enumerate(self.lines_list):
            # seeds
            if line_number == 0:
                self.seeds_list_puzzle_1 = [int(i) for i in line.split(' ') if i.isnumeric()]

            # seed-to-soil map
            if 3 <= line_number <= 39:
                self.seed_to_soil_map_dict[line_number] = [int(i) for i in line.split(' ') if i.isnumeric()]

            # soil-to-fertilizer map
            if 42 <= line_number <= 51:
                self.soil_to_fertilizer_map_dict[line_number] = [int(i) for i in line.split(' ') if i.isnumeric()]

            # fertilizer-to-water map
            if 54 <= line_number <= 89:
                self.fertilizer_to_water_map_dict[line_number] = [int(i) for i in line.split(' ') if i.isnumeric()]

            # water-to-light map
            if 92 <= line_number <= 137:
                self.water_to_light_map_dict[line_number] = [int(i) for i in line.split(' ') if i.isnumeric()]

            # light-to-temperature map
            if 140 <= line_number <= 167:
                self.light_to_temperature_map_dict[line_number] = [int(i) for i in line.split(' ') if i.isnumeric()]

            # temperature-to-humidity map
            if 170 <= line_number <= 209:
                self.temperature_to_humidity_map_dict[line_number] = [int(i) for i in line.split(' ') if i.isnumeric()]

            # humidity-to-location map
            if 212 <= line_number <= 253:
                self.humidity_to_location_map_dict[line_number] = [int(i) for i in line.split(' ') if i.isnumeric()]

        for seed in self.seeds_list_puzzle_1:
            soil = self.get_value_from_map(self.seed_to_soil_map_dict, seed)
            fertilizer = self.get_value_from_map(self.soil_to_fertilizer_map_dict, soil)
            water = self.get_value_from_map(self.fertilizer_to_water_map_dict, fertilizer)
            light = self.get_value_from_map(self.water_to_light_map_dict, water)
            temperature = self.get_value_from_map(self.light_to_temperature_map_dict, light)
            humidity = self.get_value_from_map(self.temperature_to_humidity_map_dict, temperature)
            location = self.get_value_from_map(self.humidity_to_location_map_dict, humidity)

            self.location_number_list_puzzle_1.append(location)

        return f'\nResult puzzle 1: {min(self.location_number_list_puzzle_1)}'

    def solve_part_2(self):
        location_number = 9999999999999999999999

        # seeds
        for seed_id, seed in enumerate(self.seeds_list_puzzle_1):
            print('processing seed: ', seed)
            if seed_id % 2 == 0:
                reported_progress = -1
                location_number = 9999999999999999999999

                for i in range(seed, seed + self.seeds_list_puzzle_1[seed_id+1]):
                    progress = int((i - seed)/self.seeds_list_puzzle_1[seed_id+1]*100)
                    if progress > reported_progress:
                        reported_progress = progress
                        print(f'progress: {reported_progress}%')

                    soil = self.get_value_from_map(self.seed_to_soil_map_dict, i)
                    fertilizer = self.get_value_from_map(self.soil_to_fertilizer_map_dict, soil)
                    water = self.get_value_from_map(self.fertilizer_to_water_map_dict, fertilizer)
                    light = self.get_value_from_map(self.water_to_light_map_dict, water)
                    temperature = self.get_value_from_map(self.light_to_temperature_map_dict, light)
                    humidity = self.get_value_from_map(self.temperature_to_humidity_map_dict, temperature)
                    location = self.get_value_from_map(self.humidity_to_location_map_dict, humidity)

                    if location < location_number:
                        location_number = location

                print('location_number: ', location_number)

        return f'\nResult puzzle 2: {location_number}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
