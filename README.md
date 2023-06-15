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
- [Blessed](https://blessed.readthedocs.io/en/latest/terminal.html) used to add color to the terminal.
- [Visual Studio Code](https://code.visualstudio.com/) used as a source-code editor for development.
