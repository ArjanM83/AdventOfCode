class AdventOfCode:
    def __init__(self, example_input, filename):
        # example
        self.lines_list = example_input.splitlines()[1:]
        self.use_example = False

        # input
        if not self.use_example:
            with open(filename, 'r') as f:
                self.lines_list = f.read().splitlines()

        self.register_a = None
        self.register_b = None
        self.register_c = None
        self.program_list = []
        for line in self.lines_list:
            if line.startswith('Register A: '):
                self.register_a = int(line[12:])
            elif line.startswith('Register B: '):
                self.register_b = int(line[12:])
            elif line.startswith('Register C: '):
                self.register_c = int(line[12:])
            elif line.startswith('Program: '):
                self.program_list = [int(i) for i in line[9:].split(',')]

        if self.use_example:
            print('Register A:', self.register_a)
            print('Register B:', self.register_b)
            print('Register C:', self.register_c)
            print('Program List:', self.program_list)

        self.result_puzzle_1 = []
        self.result_puzzle_2 = []

    @staticmethod
    def get_combo_operand_value(combo_operand, reg_a, reg_b, reg_c):
        if combo_operand <= 3:
            return combo_operand
        elif combo_operand == 4:
            return reg_a
        elif combo_operand == 5:
            return reg_b
        elif combo_operand == 6:
            return reg_c

    def run_opcode_instruction(self, opcode, combo_operand, reg_a, reg_b, reg_c):
        if opcode == 0:  # adv: division
            denominator = 2 ** self.get_combo_operand_value(combo_operand, reg_a, reg_b, reg_c)
            reg_a //= denominator
        elif opcode == 1:  # bxl: bitwise XOR
            reg_b ^= combo_operand
        elif opcode == 2:  # bst: combo operand modulo 8
            reg_b = self.get_combo_operand_value(combo_operand, reg_a, reg_b, reg_c) % 8
        elif opcode == 3:  # jnz: jump if A != 0
            if reg_a != 0:
                return reg_a, reg_b, reg_c, combo_operand  # Set new instruction pointer
        elif opcode == 4:  # bxc: bitwise XOR of B and C
            reg_b ^= reg_c
        elif opcode == 5:  # out: output combo operand % 8
            return reg_a, reg_b, reg_c, self.get_combo_operand_value(combo_operand, reg_a, reg_b, reg_c) % 8
        elif opcode == 6:  # bdv: division result stored in B
            denominator = 2 ** self.get_combo_operand_value(combo_operand, reg_a, reg_b, reg_c)
            reg_b = reg_a // denominator
        elif opcode == 7:  # cdv: division result stored in C
            denominator = 2 ** self.get_combo_operand_value(combo_operand, reg_a, reg_b, reg_c)
            reg_c = reg_a // denominator
        return reg_a, reg_b, reg_c, None

    def solve_part_1(self):
        instruction_pointer = 0
        reg_a, reg_b, reg_c = self.register_a, self.register_b, self.register_c

        while instruction_pointer < len(self.program_list):
            opcode = self.program_list[instruction_pointer]
            combo_operand = self.program_list[instruction_pointer + 1] \
                if instruction_pointer + 1 < len(self.program_list) \
                else 0

            reg_a, reg_b, reg_c, result = self.run_opcode_instruction(opcode, combo_operand, reg_a, reg_b, reg_c)
            if opcode == 5 and result is not None:  # Collect output
                self.result_puzzle_1.append(result)
            elif opcode == 3 and result is not None:  # Handle jump
                instruction_pointer = result
                continue  # Skip incrementing instruction pointer

            instruction_pointer += 2

        return f"\nResult puzzle 1: {','.join(map(str, self.result_puzzle_1))}"

    def solve_part_2(self):
        return f'\nResult puzzle 2: {self.result_puzzle_2}'


example = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

puzzle = AdventOfCode(example, 'input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
