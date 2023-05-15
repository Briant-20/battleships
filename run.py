import random
def get_player_choice():
    player_choices = {
        1:{"":""},
        2:{"":""},
        3:{"":""}
    }
    i = 0
    while i < 3:
        print("Enter coordinates for y axis")
        player_choice_y = input()
        print("Enter coordinates for x axis")
        player_choice_x = input()
        try:
            if int(player_choice_x) > 4 or int(player_choice_y) > 4:
                raise ValueError(
                    f"You need to enter a value between 0 and 4"
                    )
            elif int(player_choice_x) < 0 or int(player_choice_y) < 0:
                raise ValueError(
                    f"You need to enter a value between 0 and 4"
                    )
            if player_choice_y in player_choices[1] and player_choices[1][player_choice_y] == player_choice_x:
                raise ValueError(
                    f"You cannot enter the same coordinates twice, try again"
                )
            elif player_choice_y in player_choices[2] and player_choices[2][player_choice_y] == player_choice_x:
                raise ValueError(
                    f"You cannot enter the same coordinates twice, try again"
                )
            elif player_choice_y in player_choices[3] and player_choices[3][player_choice_y] == player_choice_x:
                raise ValueError(
                    f"You cannot enter the same coordinates twice, try again"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again\n")
            continue
        i += 1
        player_choice = {player_choice_y:player_choice_x}
        player_choices[i] = player_choice
    return player_choices
    

def get_computer_choice():
    computer_choices = {
        0:{"":""},
        1:{"":""},
        2:{"":""}
    }
    i = 0
    while i < 3:
        computer_choice_x = random.randint(0, 4)
        computer_choice_y = random.randint(0, 4)
        try:
            if computer_choice_y in computer_choices[0] and computer_choices[0][computer_choice_y] == computer_choice_x:
                    raise ValueError(
                    )
            elif computer_choice_y in computer_choices[1] and computer_choices[1][computer_choice_y] == computer_choice_x:
                    raise ValueError(
                    )
            elif computer_choice_y in computer_choices[2] and computer_choices[2][computer_choice_y] == computer_choice_x:
                    raise ValueError(
                    )
        except ValueError as e:
            continue
        computer_choice = {computer_choice_y:computer_choice_x}
        computer_choices[i] = computer_choice
        i += 1

def define_grid():
    y_axis = []
    for i in range(5):
        x_axis = []
        for i in range(5):
            x_axis.append(0)
        y_axis.append(x_axis)
        grid = y_axis
    return grid

def player_grid(positions_dictionary):
    grid = define_grid()
    y = -1
    for row in grid:
        x = 0
        y += 1
        for peg in row:
            if str(y) in positions_dictionary[1] and positions_dictionary[1][str(y)] == str(x):
                peg = "*"
            elif str(y) in positions_dictionary[2] and positions_dictionary[2][str(y)] == str(x):
                peg = "*"
            elif str(y) in positions_dictionary[3] and positions_dictionary[3][str(y)] == str(x):
                peg = "*"
            print(peg ,end="  ")
            x += 1
        print()
player_grid(get_player_choice())