
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
            space=str(space)
            ascii_spaces.append(ord(char) for char in space)
        ascii_board.append(ascii_spaces)
    for row in ascii_board:
        print(row)


def legal_move(colour,coord,board):
    if colour=="Light":    
        oppositeColour="-Dark"
    else:
        oppositeColour="Light"
    if board[coord[0]-1,coord[1]]== oppositeColour:



board=initialise_board()
    

    