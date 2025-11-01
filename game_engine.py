
def cli_coords_input():
    valid = False

    while valid == False:

        try:
            x_coord=int(input ("Enter the x co-ordinate") )
            y_coord=int(input ("Enter the y co-ordinate") )

        except ValueError:
            print("inputs must be integers")
            continue

        if x_coord <= 8 and y_coord <= 8:
            valid = True    
        else:
            print("inputs must be in the 8x8 grid")
            continue
    
    coord=( x_coord, y_coord )
    return coord

cli_coords_input()
