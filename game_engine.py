def cli_coords_input():
    valid = False
    while valid == False:
        try:
            x_coord=int(input("Enter the x co-ordinate"))
            y_coord=int(input("Enter the y co-ordinate"))

        except ValueError:
            continue



cli_coords_input()
