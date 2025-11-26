# Othello Game Project

This project is a Flask implementation of the board game Othello, with an AI that plays against you and a dynamically updating board on the webpage. This game can also be played through the command line using a seperate module that doesnt use Flask.

## Components Module

This module has a series of functions that are essential to computing the core aspects of the game: initialising the board, printing the board and checking the validity of moves.

### initialise_board function

---
![alt text](image-4.png)

This function passes through a default value for size as 8, this ensures that the board is created with 64 spaces default whilst allowing the user to change the size themselves. I have used a nested loop here to add none to all of the tiles initially as this will create a board that has size * size
