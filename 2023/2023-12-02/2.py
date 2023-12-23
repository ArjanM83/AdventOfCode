sum_of_power_of_games = 0

with open('input.txt', 'r') as file:
    for line in file:
        game_possible = True

        game_id_separator = line.find(': ')
        game_id = line[5:game_id_separator]
        full_game = line[game_id_separator + 2:]
        grabs = full_game.split('; ')

        required_red = 0
        required_green = 0
        required_blue = 0

        for grab in grabs:
            cubes = grab.split(', ')
            for cube in cubes:
                cube_amount, cube_color = cube.split(' ')
                cube_amount = int(cube_amount)

                if 'red' in cube_color:
                    if cube_amount > required_red:
                        required_red = cube_amount
                elif 'green' in cube_color:
                    if cube_amount > required_green:
                        required_green = cube_amount
                elif 'blue' in cube_color:
                    if cube_amount > required_blue:
                        required_blue = cube_amount

        power_of_game = required_red * required_green * required_blue
        sum_of_power_of_games += power_of_game


print('\n')
print(sum_of_power_of_games)
