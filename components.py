
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
    #temp variables used in loop
    xcheck= x
    ycheck= y
    #condition used to ensure that current coord is within bounds
    condition= 0<= x <=7 and 0<= y <=7

    for direction in direction_arr:
        xcheck += direction[0]
        ycheck += direction[1]
        condition= 0<= xcheck <=7 and 0<= ycheck <=7
        if condition == True and board[x][y] == opposite_colour:





board=initialise_board()
print_board(board)
legal_move("Light",(2,4),board)
    