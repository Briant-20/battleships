import random
def get_player_choice():
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
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")

get_player_choice()
def get_computer_choice():
    computer_choice_x = random.randint(0, 4)
    computer_choice_y = random.randint(0, 4)
    print(computer_choice_x, computer_choice_y)
get_computer_choice()
