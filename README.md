# BATTLESHIPS

This is a python command line application that allows the user to play a game of battleship against the computer.

## UX

I used an imported module to add colour to the terminal and make it more of an enjoyable experience.

### Colour Scheme

Blue is used in the terminal to indicate the players grid more clearly and red is used for the computers grid.
When a shot is missed a red X appears. 
Yellow is used for a placed ship and orange is used for a sunken ship.

## Features

### Existing Features

The user is prompted with a choice when running the program. Entering 1 will display the games rules, entering 2 will run the actual game and entering 3 will exit the program.

The user can choose the games parameters at the beginning of the game. They can pick any grid size and number of ships within a certain range as long as there is enough grid space for each ship or else they will be prompted to try again.

The user can then enter the coordinates they wish their ships to be on.
They will then choose which coordinates to attack on the computers grid.

The computer will generate its own random coordinates for both ship and attack positions.

Both sides will continue to enter attack coordinates until they sink all of their opponents ships at which point a message will be displayed declaring the winner and the game will end.

### Future Features

I would like to add a multiplayer aspect in the future where two users could play against each other.

## Tools & Technologies Used

- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Visual Studio Code](https://code.visualstudio.com/) used as a source-code editor for development.

## Data Model

### Classes & Functions

The program uses classes as a blueprint for the project's objects (OOP). This allows for the object to be reusable.

```python
class GameArea:
    """
    This is a class for all the functions that create the game area.
    """
    def __init__(self, num_of_ships, grid_size,
                 positions_dictionary, attack_position,
                 user, attack):
        """
        Initialise GameArea with attributes.
        """
        self.num_of_ships = num_of_ships
        self.grid_size = grid_size
        self.positions_dictionary = positions_dictionary
        self.attack_position = attack_position
        self.user = user
        self.attack = attack
        global num_ships
        num_ships = self.num_of_ships

class Choices:
    """
    A class containing all the functions that get a
    choice from the player and computer.
    """
    def __init__(self, num_of_ships, grid_size,
                 player_increment, computer_increment):
        """
        Initialise Choices with attributes.
        """
        self.num_of_ships = num_of_ships
        self.grid_size = grid_size
        self.player_increment = player_increment
        self.computer_increment = computer_increment
```

The primary functions used on this application are:

- `define_grid()`
    - Sets how big the grid will be depending on the users input.
- `print_grid()`
    - Prints out the grid that was defined with extra symbols depending on the users input.
- `get_player_choice()`
    - Gets inputs from the user and sets it as the choice for their ship positions.
- `get_computer_choice()`
    - Generates random numbers within a certain range to use as the computers ship positions.
- `get_player_attack_position()`
    - Gets inputs from the user and sets it as the choice for their attack positions.
- `get_computer_attack_position()`
    -  Generates random numbers within a certain range to use as the computers attack positions.
- `get_game_parameters()`
    - Get inputs from the user that set the games basic parameters such as the number of ships in play and the grid size.
- `play_game()`
    - Run all program functions.
