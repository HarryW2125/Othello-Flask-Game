'''Module that creates functions to be used in othello'''

def initialise_board(size=8):
    '''Function that initialises the board, size is set to 8 by default.'''
    #sets board array to empty
    board=[]

    #nested loop to create a board thats size x size
    for i in range(size):
        #sets spaces array to empty for each row
        spaces=[]

        for j in range(size):
            #initially sets every space to none
            spaces.append("-None")
        #adds spaces array to board array
        board.append(spaces)

    #creates centre variables that represent the positions of the central spaces
    #centre variables change depending on size of the grid
    centre1=int(size/2)-1
    centre2=int(size/2)
    #initialises 4 central spaces to their corresponding colours
    board[centre1][centre1]="Light"
    board[centre2][centre1]="-Dark"
    board[centre1][centre2]="-Dark"
    board[centre2][centre2]="Light"

    #returns board array
    return board


#print normal characters
def print_board(board):
    '''Prints an ASCII representation of a board object.'''

    for row in board:
        print(row)


def legal_move(colour,coord,board):
    '''Function that checks if a move is legal, returns true or false, and valid directions.'''
    #sets x and y variables - increases readability
    x=coord[0]
    y=coord[1]

    #sets the opposite colour
    if colour =="Light":
        opposite_colour = "-Dark"

    else:
        opposite_colour = "Light"

    # if coord is not empty then a tile cannot be placed
    if board[y][x] != "-None":
        return False, None

    #contains all directions that neighbor around the chosen coord
    direction_arr= [
        (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)
        ]
    #initialises array that stores all valid directions
    valid_direction_arr =[]

    #loops through all possible directions
    for direction in direction_arr:
        #sets initial variables needed for while loop
        current_x= x
        current_y= y
        #moves x and y one step in current direction
        current_x += direction[0]
        current_y += direction[1]

        #runs while x,y are in bounds and the tiles are opponents colour
        while (0<= current_x <=7 and 0<= current_y <=7) and (board[current_y][current_x] == opposite_colour):
            # keeps moving x and y in the same direction
            current_x += direction[0]
            current_y += direction[1]

            #breaks out of the loop if either x or y is out of bounds after moving another step
            if current_x < 0 or current_x > 7 or current_y < 0 or current_y > 7:
                break

            #if current tile is the right colour + start tile is empty, adds direction to valid arr
            if board[current_y][current_x] == colour:
                valid_direction_arr.append(direction)

    #if no directions/moves are valid
    if not valid_direction_arr:
        #returns false, no valid move found
        return False, None

    #if there is at least one valid move
    return True, valid_direction_arr
