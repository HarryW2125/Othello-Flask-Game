from flask import Flask, request, render_template, jsonify, session
import components
import random

def player_swap(current_player):
    '''Function that swaps to the other player.'''

    if current_player =="-Dark":
                current_player = "Light"
    else:
            current_player = "-Dark"
    
    return str(current_player)

def check_all_moves(colour,board):
    valid_arr =[]
    #loops through every coord on the board
    for i in range (8):

        for j in range (8):
            #checks move for current coord
            is_valid,direction = components.legal_move( colour, (j,i), board )
                
            #if valid adds true to the valid array
            if is_valid == True:
                valid_arr.append(True)
                
            else:
                valid_arr.append(False)
                
    if True in valid_arr:
        return(True)
    else:
        return(False)

def tile_counts(board):
    light_count = 0
    dark_count = 0
    for i in range(8):

        for j in range(8):
                
                if board[i][j] == "Light":
                        light_count +=1
                if board[i][j] =="-Dark":
                        dark_count +=1
    return(light_count,dark_count)
     

app = Flask(__name__)

#creates secret key so sessions can be utilised
app.secret_key = bytearray (random.randint(1,1000000))

@app.route('/')
def start_game():
    board = components.initialise_board()
    current_player = "-Dark"
    session["current_player"] = current_player
    session["board"] = board
    session["move_counter"] =60
    return render_template('index.html', game_board = board, current_player = current_player)

@app.route('/move', methods=['GET','POST'])
def process_move():
    if request.method =='GET':
        #retrieves variables from session
        current_player = session.get("current_player")
        board = session.get("board")
        move_counter = session.get("move_counter")

        #gets x and y variables from html template
        x = int(request.args['x']) -1
        y = int(request.args['y']) -1

        # if space is taken move isn't valid
        if board[y][x] != "-None":
            return jsonify( { "status": "fail", "player": current_player, "message": "Tile already placed here"})
        
        is_valid, directions = components.legal_move(current_player, (x,y), board)
        if is_valid == True:
                #flank count initially set to 1 as initial tile is already flipped before entering the loop
                flank_count =1
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
                    
                        # if the tile is the colour of the current player, flip all of the tiles in flip_arr to current players colour
                        elif board[current_y][current_x] == current_player:
                        
                            for current_x,current_y in flip_arr:
                                flank_count+=1
                                board[current_y][current_x] = current_player
                            break
                    
                        # if the tile is the opposite colour, increment replace count and add the coord to the flip arr
                        else:
                            flip_arr.append((current_x,current_y))
                         #moves x and y one step in the right direction
                            current_x += direction[0]
                            current_y += direction[1]

                current_player = player_swap(current_player)
                moves_valid_light = check_all_moves("Light",board)
                moves_valid_dark = check_all_moves("-Dark",board)
                #valid moves updates session
                session["current_player"] = current_player
                session["board"] = board
                session["move_counter"] = move_counter -1

                if (moves_valid_dark == False and moves_valid_light == False) or ( move_counter == 0):
                    light_count,dark_count = tile_counts(board)

                    if dark_count > light_count:
                         winner = "Dark"
                    elif light_count > dark_count:
                         winner = "-Light"
                    else:
                         winner = "Draw"

                    return jsonify( {"finished":f"{winner} won, light tiles: {light_count}, dark tiles: {dark_count}","board":board})
                
                elif (moves_valid_dark == False and current_player=="Light") or (moves_valid_light == False and current_player=="-Dark"):
                    previous_player = player_swap(current_player)
                    return jsonify({"status":"success","player": current_player, "board":board,"message": f"no valid move for {previous_player}, {current_player} turn "})
                

                else:    
                    return jsonify( { "status": "success", "player": current_player, "board":board,"message":""})
        else:
            moves_valid_light = check_all_moves("Light",board)
            moves_valid_dark = check_all_moves("-Dark",board)
            if (moves_valid_dark == False and moves_valid_light == False) or ( move_counter == 0):
                light_count,dark_count = tile_counts(board)

                if dark_count > light_count:
                    winner = "-Dark"
                elif light_count > dark_count:
                    winner = "Light"
                else:
                    winner = "Draw"
                                    
                return jsonify( {"finished":f"{winner} won, light tiles: {light_count}, dark tiles: {dark_count}","board":board})
            
            elif (moves_valid_dark == False and current_player=="-Dark") or (moves_valid_light == False and current_player=="Light"):
                current_player = player_swap(current_player)
                previous_player = player_swap(current_player)
                #valid moves updates session
                session["current_player"] = current_player
                session["board"] = board
                return jsonify( { "status":"fail", "player": previous_player,"message":f"No valid move for current player, swapping to {current_player}"})

            else:
              return jsonify( { "status": "fail", "player": current_player, "message":"Move is not valid"})

if __name__ == "__main__":
    app.run(debug=True)