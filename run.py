import random

choice_increment = 1
computer_hit = 0
player_hit = 0
num_ships = 0
player_attack_positions = {
            }
player_attack_position = {"":""}
computer_attack_positions = {
            }
computer_attack_position = {"":""}

class GameArea:
    def __init__(self,num_of_ships,grid_size,positions_dictionary,attack_position,type,attack):
          self.num_of_ships = num_of_ships
          self.grid_size = grid_size
          self.positions_dictionary = positions_dictionary
          self.attack_position = attack_position
          self.type = type
          self.attack = attack
          self.choice_increment = choice_increment
          self.player_hit = player_hit
          self.computer_hit = computer_hit
          global num_ships
          num_ships = self.num_of_ships

    def define_grid(self):
        y_axis = []
        for i in range(self.grid_size):
            x_axis = []
            for i in range(self.grid_size):
                x_axis.append(0)
            y_axis.append(x_axis)
            grid = y_axis
        return grid
     
    def print_grid(self):
        if self.type == "Player":
            p_hit = 0
        c_hit = 0
        global choice_increment
        global player_hit
        global computer_hit
        grid = self.define_grid()
        print(f"{self.type} grid")
        y = -1
        for row in grid:
            x = 0
            y += 1
            for peg in row:
                for i in range(self.num_of_ships):
                    position = False
                    if str(y) in self.positions_dictionary[i] and self.positions_dictionary[i][str(y)] == str(x):
                        peg = "%"
                        position = True
                        if self.type == "Computer":
                            peg = 0
                        if self.attack == True:
                            for j in range(self.choice_increment):
                                if position == True:
                                    if str(y) in self.attack_position[j] and self.attack_position[j][str(y)] == str(x):
                                        peg = "*"
                                        if self.type == "Player":
                                            p_hit += 1
                                        if self.type == "Computer":
                                            c_hit += 1
                    if self.attack == True:
                        for k in range(self.choice_increment):
                            if position == False and peg != "*":
                                if str(y) in self.attack_position[k] and self.attack_position[k][str(y)] == str(x):
                                    peg = "X"
                print(peg ,end="  ")
                x += 1
                if self.type == "Player":
                    player_hit = p_hit
                computer_hit = c_hit
            print()
        if self.attack == True and self.type == "Computer":
            choice_increment += 1

class Choices:
    def __init__(self,num_of_ships,grid_size,player_increment,computer_increment):
        self.num_of_ships = num_of_ships
        self.grid_size = grid_size
        self.player_increment = player_increment
        self.computer_increment = computer_increment

    def get_player_choice(self):
        player_choices = {
        }
        for i in range(self.num_of_ships):
                player_choice = {"":""}
                player_choices[i] = player_choice
        i = 0
        while i < self.num_of_ships:
            print("Enter coordinates for y axis")
            player_choice_y = input()
            print("Enter coordinates for x axis")
            player_choice_x = input()
            try:
                if int(player_choice_x) > self.grid_size -1 or int(player_choice_y) > self.grid_size -1:
                    raise ValueError(
                        f"You need to enter a value between 0 and {self.grid_size-1} inclusive"
                        )
                elif int(player_choice_x) < 0 or int(player_choice_y) < 0:
                    raise ValueError(
                        f"You need to enter a value between 0 and {self.grid_size-1} inclusive"
                        )
                for j in range(self.num_of_ships):
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
        return player_choices
        
    def get_computer_choice(self):
        computer_choices = {
        }
        for i in range(self.num_of_ships):
                computer_choice = {"":""}
                computer_choices[i] = computer_choice
        i = 0
        while i < self.num_of_ships:
            computer_choice_x = random.randint(0, 4)
            computer_choice_y = random.randint(0, 4)
            try:
                for j in range(self.num_of_ships):
                    if str(computer_choice_y) in computer_choices[j] and computer_choices[j][str(computer_choice_y)] == str(computer_choice_x):
                            raise ValueError(
                            )
            except ValueError:
                continue 
            computer_choice = {str(computer_choice_y):str(computer_choice_x)}
            computer_choices[i] = computer_choice
            i += 1
        return computer_choices
    
    def get_player_attack_position(self):
            k = 0
            while k < 1:
                print("Enter coordinates to attack on the y axis")
                player_choice_y = input()
                print("Enter coordinates to attack on the x axis")
                player_choice_x = input()
                try:
                    if int(player_choice_x) > self.grid_size -1 or int(player_choice_y) > self.grid_size -1:
                        raise ValueError(
                            f"You need to enter a value between 0 and {self.grid_size-1} inclusive"
                            )
                    elif int(player_choice_x) < 0 or int(player_choice_y) < 0:
                        raise ValueError(
                            f"You need to enter a value between 0 and {self.grid_size-1} inclusive"
                            )
                    for j in range(self.player_increment):
                        if player_choice_y in player_attack_positions[j] and player_attack_positions[j][player_choice_y] == player_choice_x:
                            raise ValueError(
                                f"You cannot enter the same coordinates twice, try again"
                            )
                except ValueError as e:
                    print(f"Invalid data: {e}, please try again\n")
                    continue
                k +=1 
            player_attack_position = {player_choice_y:player_choice_x}
            player_attack_positions[self.player_increment] = player_attack_position
            self.player_increment+=1
            return player_attack_positions
    
    def get_computer_attack_position(self):
        k = 0
        while k < 1:
            computer_choice_x = random.randint(0, 4)
            computer_choice_y = random.randint(0, 4)
            try:
                for j in range(self.computer_increment):
                    if str(computer_choice_y) in computer_attack_positions[j] and computer_attack_positions[j][str(computer_choice_y)] == str(computer_choice_x):
                            raise ValueError(
                            )
            except ValueError as e:
                continue 
            k +=1
        computer_attack_position = {str(computer_choice_y):str(computer_choice_x)}
        computer_attack_positions[self.computer_increment] = computer_attack_position
        self.computer_increment+=1
        return computer_attack_positions
    
def play_game():
    choices = Choices(3,5,0,0)
    player_position = choices.get_player_choice()
    computer_position = choices.get_computer_choice()
    player_grid = GameArea(3,5,player_position,player_position,"Player",False)
    hidden_ships_computer_grid = GameArea(3,5,computer_position,computer_position,"Computer",False)
    player_grid.print_grid()
    hidden_ships_computer_grid.print_grid()
    while True:
        player_attack = choices.get_player_attack_position()
        computer_attack = choices.get_computer_attack_position()
        player_grid = GameArea(3,5,player_position,computer_attack,"Player",True)
        computer_grid = GameArea(3,5,computer_position,player_attack,"Computer",True)
        player_grid.print_grid()
        computer_grid.print_grid()
        if computer_hit == num_ships:
             print("Game over you win")
             break
        if player_hit == num_ships:
             print("Game over the computer sunk all your ships")
             break
play_game()