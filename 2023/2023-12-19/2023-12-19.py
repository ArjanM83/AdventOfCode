from collections import OrderedDict


class AdventOfCode:
    def __init__(self, filename):
        self.puzzle_1_ratings_sum = 0
        self.puzzle_2_ratings_sum = 0

        self.x_min = 1
        self.x_max = 4000
        self.m_min = 1
        self.m_max = 4000
        self.a_min = 1
        self.a_max = 4000
        self.s_min = 1
        self.s_max = 4000

        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.workflows_lines_list = []
        self.part_ratings_lines_list = []
        self.ratings_dict = {'x': {}, 'm': {}, 'a': {}, 's': {}}

        # workflows and ratings
        empty_line_found = False
        for line_index, line in enumerate(self.lines_list):
            if line == '':
                empty_line_found = True

            if not empty_line_found:
                self.workflows_lines_list.append(line)
            else:
                if not line == '':
                    self.part_ratings_lines_list.append(line)

        # workflows dict
        self.workflows_dict = OrderedDict()
        for workflow_line in self.workflows_lines_list:
            workflow_key, workflow_instructions = workflow_line.split('{')
            instruction_list = workflow_instructions[:-1].split(',')

            self.workflows_dict[workflow_key] = {}
            for instruction in instruction_list:
                if ':' in instruction:
                    instruction_if, instruction_then = instruction.split(':')
                    self.workflows_dict[workflow_key][instruction_if] = instruction_then
                else:
                    self.workflows_dict[workflow_key]['else'] = instruction

        # parts ratings dict
        self.parts_ratings_dict = {}
        for part_id, part_line in enumerate(self.part_ratings_lines_list):
            ratings_list = part_line[1:-1].split(',')
            self.parts_ratings_dict[part_id] = {}
            for rating in ratings_list:
                character, value = rating.split('=')
                self.parts_ratings_dict[part_id][character] = int(value)

    def check_instruction(self, instruction, part_id):
        character = instruction[0]
        comparison = instruction[1]
        value = int(instruction[2:])

        if comparison == '<':
            if self.parts_ratings_dict[part_id][character] < value:
                return True
            else:
                return False
        else:
            if self.parts_ratings_dict[part_id][character] > value:
                return True
            else:
                return False

    def accept_part(self, part_id):
        for value in self.parts_ratings_dict[part_id].values():
            self.puzzle_1_ratings_sum += value

    def apply_workflow_puzzle_1(self, input_workflow, part_id):
        if input_workflow == 'A':
            print(part_id, self.parts_ratings_dict[part_id], '-> A')
            self.accept_part(part_id)
        elif input_workflow == 'R':
            print(part_id, self.parts_ratings_dict[part_id], '-> R')
            pass
        else:
            instruction_if_applied = False
            for instruction_if in self.workflows_dict[input_workflow]:
                if not instruction_if == 'else' and not instruction_if_applied:
                    instruction_then = self.workflows_dict[input_workflow][instruction_if]
                    if self.check_instruction(instruction_if, part_id):
                        instruction_if_applied = True
                        self.apply_workflow_puzzle_1(instruction_then, part_id)

            if not instruction_if_applied:
                self.apply_workflow_puzzle_1(self.workflows_dict[input_workflow]['else'], part_id)

    def register_combinations_for_path(self, path_string):
        self.x_min = 1
        self.x_max = 4000
        self.m_min = 1
        self.m_max = 4000
        self.a_min = 1
        self.a_max = 4000
        self.s_min = 1
        self.s_max = 4000
        self.ratings_dict = {'x': {}, 'm': {}, 'a': {}, 's': {}}

        path_string = path_string[1:]
        instruction_list = path_string.split(',')

        for instruction in instruction_list:
            character = instruction[0]
            comparison = instruction[1]
            value = int(instruction[2:])

            if comparison == '<':
                if character == 'x':
                    if self.x_max >= value:
                        self.x_max = value - 1
                elif character == 'm':
                    if self.m_max >= value:
                        self.m_max = value - 1
                elif character == 'a':
                    if self.a_max >= value:
                        self.a_max = value - 1
                elif character == 's':
                    if self.s_max >= value:
                        self.s_max = value - 1
            elif comparison == '>':
                if character == 'x':
                    if self.x_min <= value:
                        self.x_min = value + 1
                elif character == 'm':
                    if self.m_min <= value:
                        self.m_min = value + 1
                elif character == 'a':
                    if self.a_min <= value:
                        self.a_min = value + 1
                elif character == 's':
                    if self.s_min <= value:
                        self.s_min = value + 1
            elif comparison == ')':  # >=
                if character == 'x':
                    if self.x_min < value:
                        self.x_min = value
                elif character == 'm':
                    if self.m_min < value:
                        self.m_min = value
                elif character == 'a':
                    if self.a_min < value:
                        self.a_min = value
                elif character == 's':
                    if self.s_min < value:
                        self.s_min = value
            elif comparison == '(':  # <=
                if character == 'x':
                    if self.x_max > value:
                        self.x_max = value
                elif character == 'm':
                    if self.m_max > value:
                        self.m_max = value
                elif character == 'a':
                    if self.a_max > value:
                        self.a_max = value
                elif character == 's':
                    if self.s_max > value:
                        self.s_max = value

        for i in range(self.x_min, self.x_max + 1):
            self.ratings_dict['x'][i] = True
        for i in range(self.m_min, self.m_max + 1):
            self.ratings_dict['m'][i] = True
        for i in range(self.a_min, self.a_max + 1):
            self.ratings_dict['a'][i] = True
        for i in range(self.s_min, self.s_max + 1):
            self.ratings_dict['s'][i] = True

    @staticmethod
    def get_inverted_instruction(instruction):
        comparison = instruction[1]

        if comparison == '<':
            return instruction.replace(comparison, ')')
        elif comparison == '>':
            return instruction.replace(comparison, '(')
        else:
            return instruction

    def get_ratings_combinations(self):
        return (len(self.ratings_dict['x']) * len(self.ratings_dict['m']) * len(self.ratings_dict['a']) *
                len(self.ratings_dict['s']))

    def get_accepted_paths(self, input_workflow, path_string):
        if input_workflow == 'A':
            self.register_combinations_for_path(path_string)
            combinations = self.get_ratings_combinations()
            self.puzzle_2_ratings_sum += combinations
            print(path_string, combinations)
        elif input_workflow == 'R':
            pass
        else:
            for instruction_index, instruction_if in enumerate(self.workflows_dict[input_workflow]):
                instruction_then = self.workflows_dict[input_workflow][instruction_if]

                if not instruction_if == 'else':
                    new_path_string = path_string + f',{instruction_if}'
                    self.get_accepted_paths(instruction_then, new_path_string)
                else:  # last instruction
                    new_path_string = path_string
                    # get previous inverted instructions
                    for i in range(0, instruction_index):
                        for previous_instruction_index, previous_instruction in (
                                enumerate(self.workflows_dict[input_workflow])):
                            if i == previous_instruction_index:
                                new_path_string = (
                                        new_path_string + f',{self.get_inverted_instruction(previous_instruction)}')
                    self.get_accepted_paths(instruction_then, new_path_string)

    def solve_part_1(self):
        workflow_start = 'in'

        for part_id in range(0, len(self.parts_ratings_dict)):
            self.apply_workflow_puzzle_1(workflow_start, part_id)

        return f'\n{self.puzzle_1_ratings_sum}\n'

    def solve_part_2(self):
        # find paths to get accepted
        workflow_start = 'in'
        self.get_accepted_paths(workflow_start, '')

        return f'\n{self.puzzle_2_ratings_sum}'


puzzle = AdventOfCode('example_1.txt')
print(puzzle.solve_part_1())  # wrong: 1740884
print(puzzle.solve_part_2())
