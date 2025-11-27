
# Othello Game Project

<style>body {text-align: justify}</style>

This project is a Flask implementation of the board game Othello, with an AI that plays against you and a dynamically updating board on the webpage. The game can also be played through the command line with 2 players using a seperate module.

## Components Module

This module has a series of functions that are essential to computing the core aspects of the game: initialising the board, printing the board and checking the validity of moves.

### initialise_board function

---
![alt text](image-4.png)

This function passes through a default value for size as 8, this ensures that the board is created with 64 spaces default whilst allowing the user to change the size themselves. I have used a nested loop here to add none to all of the tiles initially as this will create a board that has size * size dimensions, and in the default case, 8 columns and 8 rows. Setting the 4 central spaces in this arrangement is significant as it sets up the board for starting the game.

### print_board function

---
![alt text](image-5.png)

This function is fairly simple, a board object is passed through and printed. I have chosen to print the board row by row with a for loop as this gives the board a grid shape. Printing the board in one print statement would not give the 8x8 shape wanted.

### legal_move function

---

![alt text](image-6.png)

This function takes a colour, coord and a board object as parameters to check if there are any legal moves for that colour at the coord passed through. I have set an opposite_colour variable that stores the other colour not passed through as this will be used later in the function to check whether to keep moving in the current direction. An initial check to see if the current tile is empty is necessary as a tile cannot be placed in a space that already has a tile present.

In the actual code, I have defined an array containing direction tuples:

`direction_arr= [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]`

All of these directions stored are changes to the x and y coords that allow for checking of all 8 directions including diagonals around the starting coord. E.g. (0,1) is the coord (x + 0, y + 1). I have chosen to implement the checking of moves using this array as it allows iterative movement of a coord in a specific direction. This iterates until the conditions are met that determine the validity of a move. The way I have written the code allows multiple directions to be valid for a given coord which is inline with the othello rules. If a coord has more than one valid direction all of those directions will outflank the other colours tiles. I have then used a nested loop with a while and for loop to implement the direction checks. This means that the while loop runs for every direction. The while loop runs while the current coord is on the board and its of the opponents colour. Both x and y coords are incremented once before the start of the while loop because the while loop would not run otherwise as the current tile would never be the opposite colour. The coord is incremented by the current direction at the end of the while loop, so conditions that break the while loop are checked inside. One of the conditions that is checked is if the coord is out of bounds of the board.
