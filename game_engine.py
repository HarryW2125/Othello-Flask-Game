'''Implements 2-player game of othello through command line'''
import components

def cli_coords_input():
    '''Takes co-ordinate inputs from the user and returns them as a tuple.'''
    valid = False

    #loops until the user enters valid x and y coords
    while valid is False:

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
    '''Implements 2 player othello game through the command line.'''
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

    #runs whilst the game has not ended
    while end_game is False and move_counter != 0:

        player_selected = False
        swap_counter = 0

        #checks there are legal moves for the current player
        while player_selected is False:
            valid_arr=[]

            #loops through every coord on the board
            for i in range (8):

                for j in range (8):
                    #checks move for current coord
                    is_valid,direction = components.legal_move( current_player, (j,i), board )

                    #if valid adds true to the valid array
                    if is_valid is True:
                        valid_arr.append(True)

                    else:
                        valid_arr.append(False)

            #if at least one move is legal for that player
            if True in valid_arr:
                #exits inner loop as player has been selected
                player_selected = True
                swap_counter = 0

            else:
                #changes player
                print(f"no legal move for {current_player}, swapping to next player")
                current_player = player_swap(current_player)
                #increments swap counter
                swap_counter += 1

                #if both players have invalid moves, break to outer loop
                if swap_counter >= 2:
                    end_game = True
                    break

        #if both players have invalid moves, breaks outer loop
        if swap_counter >= 2:
            break

        coord_chosen = False
        print(f"{current_player}'s Turn")
        #runs whilst current player hasnt selected a valid coord
        while coord_chosen is False:
            coord=cli_coords_input()
            #checks if move is valid for coord
            is_valid,directions = components.legal_move( current_player, coord, board )

            #if move is valid
            if is_valid is True:
                #sets initial variables used in loop
                x = coord[0]
                y = coord[1]
                #flank count initially set to 1 as initial tile is already flipped
                flank_count =1
                replace_count =0
                #changes initial tile to current player
                board[y][x] = current_player

                #runs for every valid direction
                for direction in directions:
                    flip_arr = []
                    #moves x and y one step in the right direction
                    current_x = x + direction[0]
                    current_y = y + direction[1]

                    #runs whilst the tile is on the board
                    while 0<= current_x <=7 and 0<= current_y <=7:
                        #if current tile is empty breaks out of the loop
                        if board[current_y][current_x] == "-None":
                            break

                        # if the tile is the colour of the current player
                        if board[current_y][current_x] == current_player:

                            #flip tiles in flip_arr to current colour
                            for current_x,current_y in flip_arr:
                                flank_count+=1
                                board[current_y][current_x] = current_player
                            break

                        #increment replace count +add the coord to the flip arr
                        replace_count += 1
                        flip_arr.append((current_x,current_y))

                        #moves x and y one step in the right direction
                        current_x += direction[0]
                        current_y += direction[1]

                #outputs board after changes in game state
                for row in board:
                    print(row)

                # updates tile counts for both players
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

            #prints error message
            else:
                print("move is not valid")

    #after game ends, prints who won and tile counts
    if light_count > dark_count:
        print(f"Light has won with {light_count} tiles, against Black's {dark_count} tiles")

    elif dark_count > light_count:
        print(f"Dark has won with {dark_count} tiles, against Light's {light_count} tiles")

    else:
        print(f"Draw, Light count: {light_count} and Dark count: {dark_count}")


def player_swap(current_player):
    '''Function that swaps to the other player.'''

    if current_player =="-Dark":
        current_player = "Light"
    else:
        current_player = "-Dark"

    return str(current_player)


if __name__ == '__main__':
    simple_game_loop()
