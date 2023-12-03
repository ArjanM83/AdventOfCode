sum_of_calibration_values = 0

difficult_translation_dict = {
    'twone': '2ne',
    'threeight': '3ight',
    'fiveight': '5ight',
    'sevenine': '7ine',
    'eightwo': '8wo',
    'eighthree': '8hree',
    'nineight': '9ight'
}

simple_translation_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('input.txt', 'r') as file:
    for line in file:
        for item in difficult_translation_dict:
            line = line.replace(item, difficult_translation_dict[item])

        for item in simple_translation_dict:
            line = line.replace(item, simple_translation_dict[item])

        first_digit = None
        last_digit = None

        for character in line:
            if character.isnumeric():
                if not first_digit:
                    first_digit = character
                last_digit = character

        calibration_value = int(f'{first_digit}{last_digit}')
        sum_of_calibration_values += calibration_value

print(sum_of_calibration_values)
