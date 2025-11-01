
#defines function that initialises the board, size is set to 8 by default
def initialise_board(size=8):
    #sets board array to empty
    board=[]

    #nested loop to create a board thats size x size
    for i in range (size):
        #sets spaces array to empty for each row
        spaces=[]

        for j in range (size):
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
    return(board)

# defines function that prints an ASCII repr. of the board
def print_board(board):

    #creates initial array for ascii board
    ascii_board=[]

    for row in board:
        #creates initial array for each row
        ascii_spaces=[]

        for space in row:
            #converts each character in current space to its ASCII value
            ascii_tile=[ord(char) for char in space]
            # joins each ascii character together to form an ascii repr. of the whole space
            ascii_tile=int(''.join( map ( str,ascii_tile )))
            ascii_spaces.append(ascii_tile)

        ascii_board.append(ascii_spaces)
    
    #prints ascii board
    for row in ascii_board:
        print(row)



#UNFINISHED
#defines function that checks if a move is legal, returns true or false
def legal_move(colour,coord,board):

    #sets x and y variables - increases readability
    x=coord[0]
    y=coord[1]
    #sets the opposite colour
    if colour=="Light":    
        opposite_colour="-Dark"
    else:
        opposite_colour="Light"
    
    # if coord is not empty then a tile cannot be placed
    if board[x][y] != "-None":
        return False

    #contains all directions that neighbor around the chosen coord
    direction_arr= [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    #condition used to ensure that current coord is within bounds
    condition= 0<= current_x <=7 and 0<= current_y <=7

    #loops through all possible directions
    for direction in direction_arr:
        current_x= x
        current_y= y
        #changes x and y to move in the current direction
        current_x += direction[0]
        current_y += direction[1]
        #condition checked in while loop - declared seperately for readability 
        condition= 0<= current_x <=7 and 0<= current_y <=7

        #runs while x,y are in bounds and the tiles are opponents colour
        while condition == True and board[current_x][current_y] == opposite_colour:
            # keeps moving x and y in the same direction
            current_x += direction[0]
            current_y += direction[1]
            
        if board[current_x][current_y] == colour:
            valid_arr.append(True)
        else:
            valid_arr.append(False)

    if True in valid_arr:
        return True
    else:
        return False








board=initialise_board()
print_board(board)
legal_move("Light",(2,4),board)
    