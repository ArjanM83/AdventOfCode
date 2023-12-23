sum_of_calibration_values = 0

with open('input.txt', 'r') as file:
    for line in file:
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
