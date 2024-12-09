class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()
        self.disk_map = self.lines_list[0]
        if self.use_example:
            print('disk map', self.disk_map)

        # initiate disk list
        self.disk_list = self.get_disk_list(self.disk_map)
        if self.use_example:
            print('disk list:', self.disk_list)

        # disk map dict + free space list
        self.disk_map_dict: dict = {}
        self.file_map_list = []
        self.free_space_list = []
        disk_map_counter = 0
        for index, item in enumerate(self.disk_map):
            if index % 2 == 0:
                self.disk_map_dict[disk_map_counter] = int(item)
                disk_map_counter += 1
                self.file_map_list.append(int(item))
            else:
                self.free_space_list.append(int(item))
        if self.use_example:
            print('disk map dict:', self.disk_map_dict)
            print('file map list:', self.file_map_list)
            print('free space list:', self.free_space_list)

        self.result_puzzle_1 = 0
        self.result_puzzle_2 = 0

    @staticmethod
    def get_disk_list(disk_map):
        counter = 0
        disk_list = []
        for index, digit in enumerate(disk_map):
            if index % 2 == 0:  # block file
                for i in range(int(digit)):
                    disk_list.append(counter)
                counter += 1
            else:  # free space
                for i in range(int(digit)):
                    disk_list.append('.')

        return disk_list

    @staticmethod
    def calculate_checksum(disk_list):
        checksum = 0
        for index, item in enumerate(disk_list):
            try:
                checksum += index * int(item)
            except ValueError:
                pass

        return checksum

    @staticmethod
    def remove_dots(disk_list):
        return [item for item in disk_list if item != '.']

    def get_reversed_disk_list_without_dots(self, disk_list):
        reversed_disk_list = disk_list[::-1]
        return self.remove_dots(reversed_disk_list)

    @staticmethod
    def move_individual_blocks(disk_list, reversed_disk_list_without_dots):
        reversed_counter = 0
        for index, original_item in enumerate(disk_list):
            if original_item == '.':
                disk_list[index] = reversed_disk_list_without_dots[reversed_counter]
                reversed_counter += 1

        return disk_list

    def solve_part_1(self):
        reversed_disk_list_without_dots = self.get_reversed_disk_list_without_dots(self.disk_list)
        if self.use_example:
            print('reversed without dots:', reversed_disk_list_without_dots)

        fragmented_disk_list = self.move_individual_blocks(self.disk_list, reversed_disk_list_without_dots)
        fragmented_disk_list = fragmented_disk_list[:len(reversed_disk_list_without_dots)]
        if self.use_example:
            print('fragmented:', fragmented_disk_list)

        return f'\nResult puzzle 1: {self.calculate_checksum(fragmented_disk_list)}\n'

    def solve_part_2(self):
        new_free_space_list = self.free_space_list.copy()
        allocated_free_space_list_dict = {}
        move_file_id_list = []
        decreasing_file_id_list = sorted(list(self.disk_map_dict.keys()))[::-1]
        for reversed_file_index, file_id in enumerate(decreasing_file_id_list):
            file_length = self.disk_map_dict[file_id]
            for free_space_index, free_space_length in enumerate(new_free_space_list):
                if file_length <= free_space_length and file_id > free_space_index:
                    if free_space_index in allocated_free_space_list_dict:
                        allocated_free_space_list_dict[free_space_index].append(file_id)
                    else:
                        allocated_free_space_list_dict[free_space_index] = [file_id]
                    move_file_id_list.append(file_id)

                    # fill free space
                    new_free_space_list[free_space_index] = new_free_space_list[free_space_index] - file_length

                    # create new free space by moving file
                    file_id_index = len(decreasing_file_id_list) - reversed_file_index - 1
                    new_free_space_list[file_id_index - 1] = new_free_space_list[file_id_index - 1] + file_length

                    break
        if self.use_example:
            print('move_file_id_list', move_file_id_list)
            print('allocated_free_space_list_dict:', allocated_free_space_list_dict)
            print('new_free_space_list', new_free_space_list)

        # create new disk list
        new_disk_list = []
        counter = 0
        while counter < len(self.file_map_list) - 1:
            if counter not in move_file_id_list:
                # add original file
                for i in range(self.file_map_list[counter]):
                    new_disk_list.append(counter)

            # add moved file(s)
            if counter in allocated_free_space_list_dict:
                for file_id in allocated_free_space_list_dict[counter]:
                    for i in range(self.disk_map_dict[file_id]):
                        new_disk_list.append(file_id)

            # add free space (if any left)
            for i in range(new_free_space_list[counter]):
                new_disk_list.append('.')

            counter += 1

        if self.use_example:
            print('new_disk_list:', new_disk_list)

        return f'\nResult puzzle 2: {self.calculate_checksum(new_disk_list)}'


example = """
2333133121414131402
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
