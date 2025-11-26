'''Implements Flask version of othello.'''
import random
import json
import time
from flask import Flask, request, render_template, jsonify, session
import components

def player_swap(current_player):
    '''Function that swaps to the other player.'''

    if current_player =="-Dark":
        current_player = "Light"
    else:
        current_player = "-Dark"

    return str(current_player)


def check_all_moves(colour,board):
    '''Function that checks if any moves are valid for a certain colour, returning True or False.'''
    valid_arr =[]
    #loops through every coord on the board
    for i in range (8):

        for j in range (8):
            #checks move for current coord
            is_valid,direction = components.legal_move( colour, (j,i), board )

            #if valid adds true to the valid array
            if is_valid is True:
                valid_arr.append(True)

    #returns true if at least one move is valid, otherwise false
    if True in valid_arr:
        return True

    return False


def tile_counts(board):
    '''Counts the number of light and dark tiles on the board, returning both counts.'''
    #initialses counts
    light_count = 0
    dark_count = 0

    #loops through board
    for i in range(8):

        for j in range(8):

            #updates light and dark tile counts when tiles of that colour are found
            if board[i][j] == "Light":
                light_count +=1
            if board[i][j] =="-Dark":
                dark_count +=1

    return(light_count,dark_count)


def ai_move(board):
    '''Calculates and returns coord for AI move.'''
    move_options_arr = []
    directions_arr = []

    #loops through every space on the board
    for i in range(8):

        for j in range(8):
            is_valid,directions = components.legal_move("Light",(j,i),board)

            if is_valid is True:
                #adds move to potential move pool for ai
                move_options_arr.append( (j,i))
                directions_arr.append(directions)

    best_coord = None
    best_tile_flip = 0
    
    #loops through ai move pool
    for i in range( len(move_options_arr) ):
        tile_flip = 0
        x = move_options_arr[i][0]
        y = move_options_arr[i][1]

        for direction in directions_arr[i]:
            #moves x and y one step in the right direction
            current_x = x + direction[0]
            current_y = y + direction[1]

            #runs whilst the tile is on the board
            while 0<= current_x <=7 and 0<= current_y <=7:
                #if current tile is empty or light breaks out of the loop
                if board[current_y][current_x] == "-None" or board[current_y][current_x] == "Light":
                    break

                if board[current_y][current_x] == "-Dark":
                    tile_flip +=1
                    #continues along direction
                    current_x += direction[0]
                    current_y += direction[1]
        
        #if the current move flips more tiles, reassign best_tile_flip
        if tile_flip > best_tile_flip:
            best_tile_flip = tile_flip
            best_coord = (x,y)

    return best_coord

#creates flask app
app = Flask(__name__)

#creates secret key so sessions can be used
app.secret_key = bytearray (random.randint(1,1000000))


@app.route('/')
def start_game():
    '''Starts game for flask implementation of othello'''
    #initialises board
    board = components.initialise_board()
    current_player = "-Dark"
    #saves variables to current session so they can be used between app routes
    session["current_player"] = current_player
    session["board"] = board
    #returns html template and variables
    return render_template('index_ai.html', game_board = board, current_player = current_player)


@app.route('/move')
def process_move():
    '''Processes actions when a tile is clicked in the front end.'''
    #retrieves variables from session
    current_player = session.get("current_player")
    board = session.get("board")

    # if player is ai
    if current_player == "Light":
        #creates time between player move appearing on board and ai move appearing
        time.sleep(1)
        #gets coord for ai move
        coord = ai_move(board)
        x = coord[0]
        y = coord[1]

    #if player is human
    if current_player == "-Dark":
        #gets x and y variables from html template if its the users turn, -1 needed as python backend uses 0-7 instead of 1-8
        x = int(request.args['x']) -1
        y = int(request.args['y']) -1

    # if space is taken move isn't valid
    if board[y][x] != "-None":
        return jsonify({ "status": "fail", "player": current_player, "message": "Tile already placed here"})

    #returns all valid directions for current coord
    is_valid, directions = components.legal_move(current_player, (x,y), board)

    if is_valid is True:
        #changes initial tile to current player
        board[y][x] = current_player

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

                #if the tile is the colour of the current player
                if board[current_y][current_x] == current_player:

                    #flip all of the tiles in flip_arr to current players colour
                    for current_x,current_y in flip_arr:
                        board[current_y][current_x] = current_player
                    break

                #add the coord to the flip arr
                flip_arr.append((current_x,current_y))
                #moves x and y one step in the right direction
                current_x += direction[0]
                current_y += direction[1]

        current_player = player_swap(current_player)
        #checks if there are any valid moves for both players
        moves_valid_light = check_all_moves("Light",board)
        moves_valid_dark = check_all_moves("-Dark",board)
        #updates session variables
        session["current_player"] = current_player
        session["board"] = board

        #if there are no valid moves for either player, counts up tiles and game ends
        if (moves_valid_dark is False and moves_valid_light is False):
            light_count,dark_count = tile_counts(board)

            if dark_count > light_count:
                winner = "Dark"
            elif light_count > dark_count:
                winner = "Light"
            else:
                winner = "Draw"

            return jsonify({"finished":f"{winner} won, light tiles: {light_count}, dark tiles: {dark_count}","board":board})

            #after swapping players, if the new player has no valid moves, swaps to other player
        if (moves_valid_dark is False and current_player=="-Dark") or (moves_valid_light is False and current_player=="Light"):
            previous_player = current_player
            current_player = player_swap(current_player)
            #updates session variable again as current player has changed
            session["current_player"] = current_player
            return jsonify({"status":"success","player": current_player, "board":board,"message": f"no valid move for {previous_player}, {current_player} turn "})

        #move is valid with no other conditions
        return jsonify( { "status": "success", "player": current_player, "board":board,"message":""} )

    #move is not valid
    else:
        return jsonify( { "status": "fail", "player": current_player, "message":""} )


@app.route('/save_game')
def save_game():
    '''Saves current game state to a json file.'''
    #gets variables from session
    current_player = session.get("current_player")
    board = session.get("board")
    #puts variables into a dictionary so they can be converted to json
    data = {
        "board": board,
        "current_player": current_player,
    }

    #opens json file and writes data dictionary to it
    with open("saved_game.json","w") as file:
        json.dump(data ,file)

    return jsonify()


@app.route('/load_game')
def load_game():
    '''Loads game state from a json file.'''

    #opens json file
    with open("saved_game.json","r") as file:
        json_data = json.load(file)

    #retrieves variables from json file
    current_player = json_data["current_player"]
    board = json_data["board"]
    #updates session variables
    session["current_player"] = current_player
    session["board"] = board
    return jsonify( {"game_board":board,"message":f"Its {current_player}'s turn."} )

if __name__ == "__main__":
    app.run(debug=True)
