import queue


class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.modules_dict = {'output': {'id': -1, 'function': '', 'recipients': []}}
        self.flip_flop_state_dict = {}
        self.conjunction_input_dict = {}
        self.pulse_queue = queue.Queue()

        self.low_pulse_counter_puzzle_1 = 0
        self.high_pulse_counter_puzzle_1 = 0

        for line_index, line in enumerate(self.lines_list):
            module, recipients = line.split(' -> ')
            function = module[0]
            self.modules_dict[module[1:]] = {
                'id': line_index,
                'function': function,
                'recipients': recipients.split(', ')
            }

            # flip-flop modules
            if function == '%':
                self.flip_flop_state_dict[line_index] = False

            # conjunction inputs
        for line_index, line in enumerate(self.lines_list):
            module, recipients = line.split(' -> ')

            for recipient in recipients.split(', '):
                if recipient in self.modules_dict:
                    if self.modules_dict[recipient]['function'] == '&':
                        module_id = self.modules_dict[recipient]['id']
                        if module_id not in self.conjunction_input_dict:
                            self.conjunction_input_dict[module_id] = {module[1:]: False}
                        else:
                            self.conjunction_input_dict[module_id][module[1:]] = False
        print(self.conjunction_input_dict)

    def conjunction_all_high_pulses_from_inputs(self, module_id):
        # print(module_id, self.conjunction_input_dict)
        all_high = True
        for input_module in self.conjunction_input_dict[module_id]:
            if not self.conjunction_input_dict[module_id][input_module]:
                all_high = False
                break

        return all_high

    def process_button_press(self, module_from, module_to, input_pulse=False):
        # high pulse
        if input_pulse:
            self.high_pulse_counter_puzzle_1 += 1
        # low pulse
        else:
            self.low_pulse_counter_puzzle_1 += 1

        if module_to in self.modules_dict:
            module_id = self.modules_dict[module_to]['id']
            function = self.modules_dict[module_to]['function']

            # broadcaster
            if function == 'b':
                for recipient in self.modules_dict[module_to]['recipients']:
                    self.pulse_queue.put((module_to, recipient, input_pulse))
                    print(f'button press: {function}{module_to} {input_pulse} -> {recipient}')

            # flip-flop
            elif function == '%':
                # low pulse
                if not input_pulse:
                    # turn on and send high pulse
                    if not self.flip_flop_state_dict[module_id]:
                        self.flip_flop_state_dict[module_id] = True
                        for recipient in self.modules_dict[module_to]['recipients']:
                            self.pulse_queue.put((module_to, recipient, True))
                            print(f'button press: {module_to} {True} -> {recipient}')
                    # turn off and send low pulse
                    else:
                        self.flip_flop_state_dict[module_id] = False
                        for recipient in self.modules_dict[module_to]['recipients']:
                            self.pulse_queue.put((module_to, recipient, False))
                            print(f'button press: {module_to} {False} -> {recipient}')
            # conjunction
            elif function == '&':
                self.conjunction_input_dict[module_id][module_from] = input_pulse
                if self.conjunction_all_high_pulses_from_inputs(module_id):
                    # send low pulse
                    for recipient in self.modules_dict[module_to]['recipients']:
                        self.pulse_queue.put((module_to, recipient, False))
                        print(f'button press: {module_to} {False} -> {recipient}')
                else:
                    # send high pulse
                    for recipient in self.modules_dict[module_to]['recipients']:
                        self.pulse_queue.put((module_to, recipient, True))
                        print(f'button press: {module_to} {True} -> {recipient}')
            # output
            else:
                pass

    def solve_part_1(self):
        for i in range(1000):
            print('\npress: ', i + 1)
            self.pulse_queue.put(('button', 'roadcaster', False))
            print(f'button press: button False -> broadcaster')

            while not self.pulse_queue.empty():
                module_from, module_to, signal = self.pulse_queue.get()
                self.process_button_press(module_from, module_to, signal)

        print('\n')
        print('low pulses', self.low_pulse_counter_puzzle_1)
        print('high pulses', self.high_pulse_counter_puzzle_1)
        return self.low_pulse_counter_puzzle_1 * self.high_pulse_counter_puzzle_1

    @staticmethod
    def solve_part_2():
        return 0


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
