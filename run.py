import random
def get_player_choice():
    player_choices = {
    }
    i = 0
    while i < 3:
        print("Enter coordinates for x axis")
        player_choice_x = input()
        print("Enter coordinates for y axis")
        player_choice_y = input()
        try:
            if int(player_choice_x) > 4 or int(player_choice_y) > 4:
                raise ValueError(
                    f"You need to enter a value between 0 and 4"
                    )
            if int(player_choice_x) < 0 or int(player_choice_y) < 0:
                raise ValueError(
                    f"You need to enter a value between 0 and 4"
                    )
            if int(player_choice_y) in player_choices and player_choices[int(player_choice_y)] == int(player_choice_x):
                raise ValueError(
                    f"You cannot enter the same coordinates twice, try again"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again\n")
            continue
        i += 1
        player_choices[int(player_choice_y)] = int(player_choice_x)
    print(player_choices)
    return player_choices
    

def get_computer_choice():
    computer_choice_x = random.randint(0, 4)
    computer_choice_y = random.randint(0, 4)

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
            if y in positions_dictionary and positions_dictionary[y] == x:
                peg = "*"
            print(peg ,end="  ")
            x += 1
        print()
player_grid(get_player_choice())
