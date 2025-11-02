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
    #sets starting player to dark
    current_player= "-Dark"
    end_game = False
    while end_game == False and move_counter != 0:
        player_selected = False

        #checks there are legal moves
        while player_selected == False:
            for i in range (7):
                for j in range (7):
                    is_valid= components.legal_move(current_player,(j,i),board)
                    if is_valid[0] == True:
                        player_selected = True

            if current_player =="-Dark":
                current_player = "Light"
            else:
                current_player = "-Dark"
            player_selected = True
        
        coord_chosen = False
        print(f"{current_player}'s Turn")
        while coord_chosen == False:
            coord=cli_coords_input()

            if components.legal_move(current_player, coord,board) == True:
                #change counters
                #change player
                coord_chosen = True
                #decrements move counter
                move_counter -= 1
            
            else:
                print("move is not valid")
                

            


            

simple_game_loop()








