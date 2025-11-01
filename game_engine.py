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
        if x_coord <= 8 and y_coord <= 8:
            valid = True    
        else:
            print("inputs must be in the 8x8 board")
            continue
    
    #creates coord tuple with x and y
    coord=( x_coord, y_coord )
    return coord



