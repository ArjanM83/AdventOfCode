class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.input_list = self.lines_list[0].split(',')

    @staticmethod
    def get_hash(input_string):
        current_value = 0
        for character in input_string:
            ascii_code = ord(character)
            current_value += ascii_code
            current_value *= 17
            current_value = current_value % 256

        return current_value

    def solve_part_1(self):
        sum_of_results = 0

        for input_string in self.input_list:
            sum_of_results += self.get_hash(input_string)

        return f'\npuzzel 1: {sum_of_results}\n'

    def solve_part_2(self):
        sum_of_results = 0

        boxes_dict = {}
        for i in range(256):
            boxes_dict[i] = []

        for input_string in self.input_list:
            remove = False
            label = ''
            focal_length = 0

            if '=' in input_string:
                label, focal_length = input_string.split('=')
                remove = False
            elif '-' in input_string:
                label = input_string[:-1]
                remove = True

            label_hash = self.get_hash(label)

            if remove:
                new_list = []
                for lens_list in boxes_dict[label_hash]:
                    if lens_list[0] != label:
                        new_list.append(lens_list)
                boxes_dict[label_hash] = new_list
            else:
                updated = False
                # update existing label
                new_list = []
                for lens_list in boxes_dict[label_hash]:
                    if lens_list[0] == label:
                        new_list.append([label, focal_length])
                        updated = True
                    else:
                        new_list.append(lens_list)
                boxes_dict[label_hash] = new_list

                # add new label
                if not updated:
                    boxes_dict[label_hash].append([label, focal_length])

        for box in range(256):
            for lens_list_index, lens_list in enumerate(boxes_dict[box]):
                result = (box + 1) * (lens_list_index + 1) * int(lens_list[1])
                sum_of_results += result

        return f'\npuzzel 2: {sum_of_results}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
