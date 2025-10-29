
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



#COME BACK TO THIS 
def print_board(board):
    ascii_board=[]
    for row in board:
        ascii_spaces=[]
        for space in row:
            #space=str(space)
            ascii_tile=[ord(char) for char in space]
            ascii_tile=int(''.join(map(str,ascii_tile)))
            ascii_spaces.append(ascii_tile)
        ascii_board.append(ascii_spaces)
    for row in ascii_board:
        print(row)


def legal_move(colour,coord,board):

    #sets the opposite colour
    if colour=="Light":    
        oppositeColour="-Dark"
    else:
        oppositeColour="Light"
    
    # if coord is not empty then a tile cannot be placed
    if board[coord[0]][coord[1]] != "-None":
        return False

    #if board[coord[0]-1,coord[1]]== oppositeColour:
    for i in range(-1,2):
        for j in range(-1,2):
            print(board[coord[0]+i][coord[1]+j])

board=initialise_board()
print_board(board)
#move=legal_move("-Dark",(7,7),board)

    