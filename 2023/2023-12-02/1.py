sum_of_ids = 0

red_cubes = 12
green_cubes = 13
blue_cubes = 14

with open('input.txt', 'r') as file:
    for line in file:
        game_possible = True

        game_id_separator = line.find(': ')
        game_id = line[5:game_id_separator]
        full_game = line[game_id_separator + 2:]
        grabs = full_game.split('; ')

        for grab in grabs:
            cubes = grab.split(', ')
            for cube in cubes:
                cube_amount, cube_color = cube.split(' ')

                if 'red' in cube_color:
                    if int(cube_amount) > red_cubes:
                        game_possible = False
                elif 'green' in cube_color:
                    if int(cube_amount) > green_cubes:
                        game_possible = False
                elif 'blue' in cube_color:
                    if int(cube_amount) > blue_cubes:
                        game_possible = False

        if game_possible:
            sum_of_ids += int(game_id)
            print(f'yes: {line.strip()}')
        else:
            print(f'no:  {line.strip()}')

print('\n')
print(sum_of_ids)
