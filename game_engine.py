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
    #sets initial colour counts to 2
    dark_count = 2
    light_count = 2

    while end_game == False and move_counter != 0:
        player_selected = False
        swap_counter = 0
        #checks there are legal moves
        while player_selected == False:
            valid_arr=[]

            for i in range (7):

                for j in range (7):
                    is_valid,direction = components.legal_move( current_player, (j,i), board )
                    if is_valid == True:
                        valid_arr.append(True)
                    else:
                        valid_arr.append(False)

            if True in valid_arr:
                player_selected = True
                swap_counter = 0
            else:
                #changes player
                print(f"no legal move for {current_player}, swapping to next player")
                current_player = player_swap(current_player)
                swap_counter += 1
                if swap_counter >= 2:
                    end_game = True
                    break
                
        if swap_counter >= 2:
                break
        coord_chosen = False
        print(f"{current_player}'s Turn")
        while coord_chosen == False:
            coord=cli_coords_input()
            is_valid,direction = components.legal_move( current_player, coord, board )
            if is_valid == True:
                # counters
                x = coord[0] 
                y = coord[1]
                board[y][x] = current_player   
                flip_arr = []
                flank_count =1
                replace_count =0
                x += direction[0]
                y += direction[1]

                while 0<= x <=7 and 0<= y <=7:
                    if board[y][x] == "-None":
                         break
                     
                    elif board[y][x] == current_player:
                        
                        for x,y in flip_arr:
                            flank_count+=1
                            print("flank",flank_count)
                            board[y][x] = current_player
                        break
                    else:
                        replace_count += 1
                        print(replace_count)
                        flip_arr.append((x,y))
                    x += direction[0]
                    y += direction[1]
                    

                for row in board:
                    print(row)
                
                if current_player =="-Dark":
                    dark_count += flank_count
                    light_count -= replace_count
                    print(f"Outflanked! {current_player} tile count: {dark_count}")
                else:
                    light_count += flank_count
                    dark_count -= replace_count
                    print(f"Outflanked! {current_player} tile count: {light_count}")
                
                #changes player
                current_player = player_swap(current_player)
                #decrements move counter
                move_counter -= 1            
                coord_chosen = True
            else:
                print("move is not valid")

    if light_count > dark_count:
        print(f"Light has won with {light_count} tiles, against Black's {dark_count} tiles")
    elif dark_count > light_count:
        print(f"Dark has won with {dark_count} tiles, against Light's {light_count} tiles")
    else:
        print(f"Draw, Light count: {light_count} and Dark count: {dark_count}")
                       

#swaps the current player          
def player_swap(current_player):

    if current_player =="-Dark":
                current_player = "Light"
    else:
            current_player = "-Dark"
    
    return str(current_player)


            

simple_game_loop()








