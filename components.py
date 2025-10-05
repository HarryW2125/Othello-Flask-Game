
#defines function that initialises the board, size is set to 8 by default
def initialise_board(size=8):
    board=[]
    for i in range (size):
        spaces=[]
        for j in range (size):
            spaces.append("-None")
        
        board.append(spaces)

    centre1=int(size/2)-1
    centre2=int(size/2)
    board[centre1][centre1]="Light"
    board[centre2][centre1]="-Dark"
    board[centre1][centre2]="-Dark"
    board[centre2][centre2]="Light"
    return(board)

board= initialise_board()
for row in board:
    print(row)      

    