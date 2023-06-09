import random
from blessed import Terminal

# Initialise variables
term = Terminal()
choice_increment = 1
computer_hit = 0
player_hit = 0
num_ships = 0
player_attack_positions = {
}
player_attack_position = {"": ""}
computer_attack_positions = {
}
computer_attack_position = {"": ""}


# Define class GameArea
class GameArea:
    def __init__(self, num_of_ships, grid_size,
                 positions_dictionary, attack_position,
                 user, attack):
        self.num_of_ships = num_of_ships
        self.grid_size = grid_size
        self.positions_dictionary = positions_dictionary
        self.attack_position = attack_position
        self.user = user
        self.attack = attack
        global num_ships
        num_ships = self.num_of_ships

    # Define function to create a template grid
    def define_grid(self):
        print()
        y_axis = []
        for _ in range(self.grid_size):
            x_axis = []
            for _ in range(self.grid_size):
                x_axis.append(0)
            y_axis.append(x_axis)
            grid = y_axis
        return grid

    # Print out a grid to the terminal
    def print_grid(self):
        global player_hit
        global computer_hit
        global choice_increment
        computer_hit = 0
        grid = self.define_grid()
        if self.user == "Player":
            player_hit = 0
            print(term.blue(f"{self.user} grid"))
        else:
            print(term.red(f"{self.user} grid"))
        y = -1
        for row in grid:
            x = 0
            y += 1
            for peg in row:
                for i in range(self.num_of_ships):
                    position = False
                    if str(y) in self.positions_dictionary[
                        i] and self.positions_dictionary[i][str(
                            y)] == str(x):
                        peg = term.yellow("%")
                        position = True
                        if self.user == "Computer":
                            peg = 0
                        if self.attack:
                            for j in range(choice_increment):
                                if position:
                                    if str(y) in self.attack_position[
                                        j] and self.attack_position[j][str(
                                            y)] == str(x):
                                        peg = term.orange("*")
                                        if self.user == "Player":
                                            player_hit += 1
                                        if self.user == "Computer":
                                            computer_hit += 1
                    if self.attack:
                        for k in range(choice_increment):
                            if position is False and peg != term.orange("*"):
                                if str(y) in self.attack_position[
                                    k] and self.attack_position[
                                        k][str(y)] == str(x):
                                    peg = term.red("X")
                print(peg, end="  ")
                x += 1
            print()
        print()
        if self.attack and self.user == "Computer":
            choice_increment += 1


# Define class Choices
class Choices:
    def __init__(self, num_of_ships, grid_size,
                 player_increment, computer_increment):
        self.num_of_ships = num_of_ships
        self.grid_size = grid_size
        self.player_increment = player_increment
        self.computer_increment = computer_increment

    # Function to get the players choice for their ships positions
    def get_player_choice(self):
        player_choices = {
        }
        for i in range(self.num_of_ships):
            player_choice = {"": ""}
            player_choices[i] = player_choice
        i = 0
        while i < self.num_of_ships:
            print(
                "Coordinates are between "
                "0 "
                f"and {self.grid_size-1}")
            print(f"Enter coordinates on the y axis for ship {i+1}")
            player_choice_y = input()
            print(f"Enter coordinates on the x axis for ship {i+1}")
            player_choice_x = input()
            try:
                if int(player_choice_x) > self.grid_size - \
                        1 or int(player_choice_y) > self.grid_size - 1:
                    raise ValueError(
                        "You need to enter a value between "
                        f"0 and {self.grid_size-1} inclusive"
                    )
                elif int(player_choice_x) < 0 or int(player_choice_y) < 0:
                    raise ValueError(
                        "You need to enter a value between "
                        f"0 and {self.grid_size-1} inclusive"
                    )
                for j in range(self.num_of_ships):
                    if player_choice_y in player_choices[j] and player_choices[
                            j][player_choice_y] == player_choice_x:
                        raise ValueError(
                            "You cannot enter the same coordinates twice, "
                            "try again"
                        )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again\n")
                continue
            player_choice = {player_choice_y: player_choice_x}
            player_choices[i] = player_choice
            i += 1
        return player_choices

    # Function to get the computers choice for their ships positions
    def get_computer_choice(self):
        computer_choices = {
        }
        for i in range(self.num_of_ships):
            computer_choice = {"": ""}
            computer_choices[i] = computer_choice
        i = 0
        while i < self.num_of_ships:
            computer_choice_x = random.randint(0, self.grid_size-1)
            computer_choice_y = random.randint(0, self.grid_size-1)
            try:
                for j in range(self.num_of_ships):
                    if str(computer_choice_y) in computer_choices[
                            j] and computer_choices[j][str(
                            computer_choice_y)] == str(computer_choice_x):
                        raise ValueError(
                        )
            except ValueError:
                continue
            computer_choice = {str(computer_choice_y): str(computer_choice_x)}
            computer_choices[i] = computer_choice
            i += 1
        return computer_choices

    # Function to get the players choice for where to attack the computers grid
    def get_player_attack_position(self):
        k = 0
        while k < 1:
            print(
                "Coordinates are between "
                "0 "
                f"and {self.grid_size-1}")
            print("Enter coordinates to attack on the y axis")
            player_choice_y = input()
            print("Enter coordinates to attack on the x axis")
            player_choice_x = input()
            try:
                if int(player_choice_x) > self.grid_size -  \
                        1 or int(player_choice_y) > self.grid_size - 1:
                    raise ValueError(
                        "You need to enter a value between "
                        f"0 and {self.grid_size-1} inclusive"
                    )
                elif int(player_choice_x) < 0 or int(player_choice_y) < 0:
                    raise ValueError(
                        "You need to enter a value between "
                        f"0 and {self.grid_size-1} inclusive"
                    )
                for j in range(self.player_increment):
                    if player_choice_y in player_attack_positions[
                            j] and player_attack_positions[
                            j][player_choice_y] == player_choice_x:
                        raise ValueError(
                            "You cannot enter the same "
                            "coordinates twice"
                        )
            except ValueError as e:
                print(f"Invalid data: {e}, please try again\n")
                continue
            k += 1
        player_attack_position = {player_choice_y: player_choice_x}
        player_attack_positions[self.player_increment] = player_attack_position
        self.player_increment += 1
        return player_attack_positions

    # Function to get the computers choice for where to attack the players grid
    def get_computer_attack_position(self):
        k = 0
        while k < 1:
            computer_choice_x = random.randint(0, self.grid_size-1)
            computer_choice_y = random.randint(0, self.grid_size-1)
            try:
                for j in range(self.computer_increment):
                    if str(computer_choice_y) in computer_attack_positions[
                        j] and computer_attack_positions[j][str(
                            computer_choice_y)] == str(computer_choice_x):
                        raise ValueError(
                        )
            except ValueError:
                continue
            k += 1
        computer_attack_position = {
            str(computer_choice_y): str(computer_choice_x)}
        computer_attack_positions[
            self.computer_increment] = computer_attack_position
        self.computer_increment += 1
        return computer_attack_positions


# Function to call all the necessary functions to play the game
def play_game():
    while True:
        print("Enter 1 for the rules")
        print("Enter 2 to play the game")
        print("Enter 3 to exit")
        choice = input()
        try:
            if int(choice) <= 0 or int(choice) > 3:
                raise ValueError()
        except ValueError as e:
            print(f"Invalid data: {e}, please try again\n")
            continue
        if int(choice) == 1:
            print()
            print(
                ":This is a game of battleships played against the computer.\n"
                ":You will enter the coordinates for your ships "
                "in the beginning.\n"
                ":You will be able to see the location of your ships "
                "but not the computers.\n"
                ":Afterwards you will take turns entering coordinates "
                "to attack each other’s grids.\n"
                ":A single peg on the grid is represented by the 0 symbol.\n"
                f":Your ships are represented by the {term.black('%')} symbol.\n"
                f":A sunken ship is represented by the {term.orange('*')} symbol.\n"
                f":A missed hit is represented by the {term.red('X')} symbol.\n"
                ":When all of a players ships are sunk "
                "they lose and the game ends")
            print()
            continue
        if int(choice) == 2:
            while True:
                print("Choose game parameters")
                print("Enter the number of ships")
                ships = input()
                print("Enter the grid size(e.g. entering 5 will create a 5 x 5 grid area)")
                grid = input()
                try:
                    if int(grid) <= 0 or int(ships) <= 0:
                        raise ValueError()
                    if int(grid) * int(grid) % int(ships) == int(grid) * int(grid):
                        raise ValueError("You have too many ships and not enough grid space")
                except ValueError as e:
                    print(f"Invalid data: {e}, please try again\n")
                    continue
                ships = int(ships)
                grid = int(grid)
                choices = Choices(ships, grid, 0, 0)
                player_position = choices.get_player_choice()
                computer_position = choices.get_computer_choice()
                player_grid = GameArea(
                    ships, grid, player_position, player_position, "Player", False)
                hidden_ships_computer_grid = GameArea(
                    ships, grid, computer_position, computer_position, "Computer", False)
                player_grid.print_grid()
                hidden_ships_computer_grid.print_grid()
                break
            while True:
                player_attack = choices.get_player_attack_position()
                computer_attack = choices.get_computer_attack_position()
                player_grid = GameArea(
                    ships, grid, player_position, computer_attack, "Player", True)
                computer_grid = GameArea(
                    ships, grid, computer_position, player_attack, "Computer", True)
                player_grid.print_grid()
                computer_grid.print_grid()
                if computer_hit == num_ships:
                    print("Game over, congratulations you win!")
                    print()
                    break
                elif player_hit == num_ships:
                    print("Game over, the computer sunk all your ships.")
                    print()
                    break
        if int(choice) == 3:
            break
        break


# Call the play_game function
play_game()