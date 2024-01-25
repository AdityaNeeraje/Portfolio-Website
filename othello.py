def display(white_buttons_list, black_buttons_list):
    value = [['.'] * 8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            if 8 * i + j in white_buttons_list:
                value[i][j] = 'W'
            if 8 * i + j in black_buttons_list:
                value[i][j] = 'B'
    for line in value:
        print(line)


from time import sleep


def argmax(given_list):
    index = 0
    maximum = given_list[index]
    max_index = index
    length = len(given_list)
    while index < length:
        if given_list[index] > maximum:
            maximum = given_list[index]
            max_index = index
        index += 1
    return max_index


def clickable_buttons(white_buttons_list, black_buttons_list, black_to_play):
    return [i for i in range(64) if check_if_can_place(i, black_to_play, white_buttons_list, black_buttons_list) != -1]


def check_if_can_place(number, black_to_play, white_buttons_list, black_buttons_list, only_check=True):
    if number in white_buttons_list or number in black_buttons_list:
        return -1
    row_number = number // 8
    column_number = number % 8
    if not black_to_play:
        player1_list = white_buttons_list
        player2_list = black_buttons_list
    else:
        player1_list = black_buttons_list
        player2_list = white_buttons_list
    num_converted = 0
    for list_of_buttons in [range(8 * row_number + column_number, 8 * row_number + 8),
                            range(8 * row_number + column_number, 8 * row_number - 1, -1),
                            range(8 * row_number + column_number, -1, -8), range(8 * row_number + column_number, 64, 8),
                            range(number, 64, 9), range(number, -1, -9), range(number, 64, 7), range(number, -1, -7)]:
        index = 1
        while index < len(list_of_buttons) and list_of_buttons[index] in player2_list:
            index += 1
        if 1 < index < len(list_of_buttons) and list_of_buttons[index] in player1_list:
            num_converted += index - 1
            if not only_check:
                if black_to_play:
                    black_buttons_list.append(number)
                else:
                    white_buttons_list.append(number)
                for button in list_of_buttons[1: index]:
                    if black_to_play:
                        white_buttons_list.remove(button)
                        black_buttons_list.append(button)
                    else:
                        black_buttons_list.remove(button)
                        white_buttons_list.append(button)
    if num_converted:
        return num_converted
    return -1


def check_if_switch_sides(white_buttons_list, black_buttons_list, black_to_play):
    white_clickable_buttons = clickable_buttons(white_buttons_list, black_buttons_list, False)
    black_clickable_buttons = clickable_buttons(white_buttons_list, black_buttons_list, True)
    if not white_buttons_list or not black_buttons_list or (
            not white_clickable_buttons and not black_clickable_buttons):
        if len(white_buttons_list) > len(black_buttons_list):
            print(f"Game Over. The winner is White")
        elif len(white_buttons_list) < len(black_buttons_list):
            print(f"Game Over. The winner is Black")
        elif len(white_buttons_list) == len(black_buttons_list):
            print("Game over. The game resulted in a draw.")
        return None
    if not white_clickable_buttons:
        black_to_play = True
        return black_to_play
    if not black_clickable_buttons:
        black_to_play = False
        return black_to_play
    black_to_play = not black_to_play
    return black_to_play


def button_clicked(button, white_buttons_list, black_buttons_list, black_to_play):
    check_if_can_place(button, black_to_play, white_buttons_list, black_buttons_list, only_check=False)
    black_to_play = check_if_switch_sides(white_buttons_list, black_buttons_list, black_to_play)
    if black_to_play is None:
        return
    if not black_to_play:
        sleep(0.75)
        computer_play(white_buttons_list, black_buttons_list)


def computer_play(white_buttons_list, black_buttons_list):
    choice = argmax(
        [check_if_can_place(i, False, white_buttons_list, black_buttons_list, only_check=True) for i in range(64)])
    check_if_can_place(choice, False, white_buttons_list, black_buttons_list, only_check=False)
    check_if_switch_sides(white_buttons_list, black_buttons_list, False)
