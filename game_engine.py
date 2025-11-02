import components

#function that takes co-ordinate inputs from the user and returns them as a tuple
def cli_coords_input():
    valid = False

    #loops until the user enters valid x and y coords
    while valid == False:
        
        #error handling in the case of non-integers being inputted
        try:
            #user inputs for x and y
            x_coord=int(input ("Enter the x co-ordinate") )
            y_coord=int(input ("Enter the y co-ordinate") )

        except ValueError:
            print("inputs must be integers")
            continue
        
        #ensures that chosen coords are in range of the board
        if 0 <= x_coord <= 7 and 0 <= y_coord <= 7:
            valid = True    
        else:
            print("inputs must be in the 8x8 board")
            continue
    
    #creates coord tuple with x and y
    coord=( x_coord, y_coord )
    return coord


def simple_game_loop():
    
    print("Welcome to Othello!")
    # creates board
    board = components.initialise_board()
    #sets move counter
    move_counter = 60
    player_arr=["-Dark","-Light"]
    current_player= player_arr[0]
    end_game = False
    while end_game == False and move_counter != 0:
        
        #checks if there are legal moves for current player
        legal_tuples=[]
        for row in board:
            for space in row:
                if space == current_player:
                    legal_tuples.append( (space.index(), row.index()) )
            










