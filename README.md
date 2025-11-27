
# Othello Game Project

<style>body {text-align: justify}</style>

This project is a Flask implementation of the board game Othello, with an AI that plays against you and a dynamically updating board on the webpage. The game can also be played through the command line with 2 players using a seperate module.

## Components Module

This module has a series of functions that are essential to computing the core aspects of the game: initialising the board, printing the board and checking the validity of moves. This is needed as it provides the fundamental functionality needed to implement othello.

### initialise_board function

---
![initialise_board](./flowcharts/initialise_board.png)

This function passes through a default value for size as 8, this ensures that the board is created with 64 spaces default whilst allowing the user to change the size themselves. This function as it creates the board the game is played on. I have used a nested loop here to add none to all of the tiles initially as this will create a board that has size * size dimensions, and in the default case, 8 columns and 8 rows. Setting the 4 central spaces in this arrangement is significant as it sets up the board for starting the game.

### print_board function

---
![print_board](./flowcharts/print_board.png)

This function is fairly simple, a board object is passed through and printed. This is needed to print the board state for the command line version of the game. I have chosen to print the board row by row with a for loop as this gives the board a grid shape. Printing the board in one print statement would not give the 8x8 shape wanted.

### legal_move function

---

![legal_move](./flowcharts/legal_move.png)

This function takes a colour, coord and a board object as parameters to check if there are any legal moves for that colour at the coord passed through. This is needed so that moves can be checked for legality before being commited to the board state. I have set an opposite_colour variable that stores the other colour not passed through as this will be used later in the function to check whether to keep moving in the current direction. An initial check to see if the current tile is empty is necessary as a tile cannot be placed in a space that already has a tile present. In the actual code, I have defined an array containing direction tuples:

`direction_arr= [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]`

All of these directions stored are changes to the x and y coords that allow for checking of all 8 directions including diagonals around the starting coord. E.g. (0,1) will transform (x,y) into (x + 0, y + 1). I have chosen to implement the checking of moves using this array as it allows iterative movement of a coord in a specific direction. This iterates until the conditions are met that determine the validity of a move. The way I have written the code, which is slightly different to the flow diagram, allows multiple directions to be valid for a given coord which is inline with the othello rules. If a coord has more than one valid direction all of those directions will outflank the other colours tiles. I have then used a nested loop with a while and for loop to implement the direction checks. This means that the while loop runs for every direction. The while loop runs while the current coord is on the board and its of the opponents colour. Both x and y coords are incremented once before the start of the while loop because the while loop would not run otherwise as the current tile would never be the opposite colour. The coord is incremented by the current direction at the end of the while loop in the program, so conditions that break the while loop are checked inside. One of the conditions that is checked is if the coord is out of bounds of the board. If the current coord is out of bounds, that means that the move is not valid hence breaking out of the while loop and iterating to the next direction. The other condition that is checked is if the current coord is the current players colour. If it is, this means that the direction is legal as it will trap opponents tiles between 2 tiles.

I have slightly modified this function from the specification, so that it returns the directions of the move if it is valid alongside True or False. This allows for more efficient tile flipping in the main loop without having to check every direction again. In the actual code, the function returns `False, None` when there are no valid moves as there will be no directions to be returned.

## Game Engine Module

This module implements a simple version of othello through the command line for 2 players to play, using a game loop that runs until the game is finished. Functions from the components module are also used within. This module is needed so a simpler version of the game without flask dependancies can be played.

### cli_coords_input

---

![coords_input](./flowcharts/coords_input.png)

This function takes x and y inputs from a user, validates and sanitises the input and returns the coord as a tuple. This is needed to ensure users moves are sent back to the game loop in the right format, and to catch erroneous inputs being entered. I have used a while loop here that runs whilst a valid coord hasnt been entered. This allows for re-entering of x and y values after invalid inputs by the user. In the code I have used try/except error handling to catch errors where integers are not entered. I have used this as it's a good way to catch specific errors or cases. Casting both inputs to integers  can cause a `ValueError` which is caught by the except block. This block prints an error message and I have then used a continue statement to run the next iteration of the while loop. If x and y are accepted as integers an additional check is made to see if both x and y are in bounds of the board. If they aren't another continue statement has been used. If the x and y are within bounds the coord is now valid which will terminate the while loop. A coord tuple with (x,y) is then created and returned to the main game loop.

### player_swap function

---

![player_swap](./flowcharts/player_swap.png)

This is a simple function that takes in the current player as a parameter and swaps this to the other player. I have chosen to create this alongside the functions in the specification as its an extremely common process that needs to happen in both the command line and flask game engines multiple times. Selection has been used here to swap the current player based on the player passed through e.g. light to dark or vice versa.

### simple_game_loop function

---

![simple_game_loop](./flowcharts/simple_game_loop.png)

This function implements the core gameplay loop needed to play Othello through the command line, using other functions from this module and functions from components within. This is needed as it gives the game structure and allows it to actually be played by 2 players. A board object is initialised and other variables are set up before the loop begins. Both `light_count` and `dark_count` are initially set to 2 due to the starting condition of the board. I have used quite a few nested loops in this function to implement the loop. The outermost loop runs whilst the game hasn't ended and `move_counter` is not 0.