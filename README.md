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

### Imports

I've used the following Python packages and/or external imported packages.

- `blessed`: used for including color in the terminal
- `random`: used to get a random choice from a list

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://battleships-project-game.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Briant-20/battleships) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/Briant-20/battleships.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Briant-20/battleships)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Briant-20/battleships)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Blessed](https://pypi.org/project/blessed/) |Imported library | Library to add color to the terminal

### Acknowledgements

- I would like to thank my Code Institute mentors, [Tim Nelson](https://github.com/TravelTimN) and [Aleksei Konovalov](https://code-institute-room.slack.com/team/U029X3N2WN9) for their support throughout the development of this project.
