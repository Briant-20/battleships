import random
def get_player_choice(num_of_ships,grid_size):
    player_choices = {
    }
    for i in range(num_of_ships):
             player_choice = {"":""}
             player_choices[i] = player_choice
    i = 0
    while i < num_of_ships:
        print("Enter coordinates for y axis")
        player_choice_y = input()
        print("Enter coordinates for x axis")
        player_choice_x = input()
        try:
            if int(player_choice_x) > grid_size -1 or int(player_choice_y) > grid_size -1:
                raise ValueError(
                    f"You need to enter a value between 0 and {grid_size-1} inclusive"
                    )
            elif int(player_choice_x) < 0 or int(player_choice_y) < 0:
                raise ValueError(
                    f"You need to enter a value between 0 and {grid_size-1} inclusive"
                    )
            for j in range(num_of_ships):
                if player_choice_y in player_choices[j] and player_choices[j][player_choice_y] == player_choice_x:
                    raise ValueError(
                        f"You cannot enter the same coordinates twice, try again"
                    )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again\n")
            continue
        player_choice = {player_choice_y:player_choice_x}
        player_choices[i] = player_choice
        i += 1
    print(player_choices)
    return player_choices
    
def get_computer_choice(num_of_ships):
    computer_choices = {
    }
    for i in range(num_of_ships):
             computer_choice = {"":""}
             computer_choices[i] = computer_choice
    i = 0
    while i < num_of_ships:
        computer_choice_x = random.randint(0, 4)
        computer_choice_y = random.randint(0, 4)
        try:
            for j in range(num_of_ships):
                if computer_choice_y in computer_choices[j] and computer_choices[j][computer_choice_y] == computer_choice_x:
                        raise ValueError(
                        )
        except ValueError as e:
            continue
        computer_choice = {computer_choice_y:computer_choice_x}
        computer_choices[i] = computer_choice
        i += 1
    print(computer_choices)

def define_grid(grid_size):
    y_axis = []
    for i in range(grid_size):
        x_axis = []
        for i in range(grid_size):
            x_axis.append(0)
        y_axis.append(x_axis)
        grid = y_axis
    return grid

def player_grid(positions_dictionary,num_of_ships,grid_size):
    grid = define_grid(grid_size)
    y = -1
    for row in grid:
        x = 0
        y += 1
        for peg in row:
            for i in range(num_of_ships):
                if str(y) in positions_dictionary[i] and positions_dictionary[i][str(y)] == str(x):
                    peg = "*"
            print(peg ,end="  ")
            x += 1
        print()
get_computer_choice(3)
player_grid(get_player_choice(3,5),3,5)
