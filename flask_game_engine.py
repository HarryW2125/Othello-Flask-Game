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

        is_valid, direction = components.legal_move(current_player, (x,y), board)
        if is_valid == True:
                flip_arr = []
                #flank count initially set to 1 as initial tile is already flipped before entering the loop
                flank_count =1
                #changes initial tile to current player
                board[y][x] = current_player  
                #moves x and y one step in the right direction
                x += direction[0]
                y += direction[1]

                #runs whilst the tile is on the board
                while 0<= x <=7 and 0<= y <=7:
                    #if current tile is empty breaks out of the loop
                    if board[y][x] == "-None":
                        break
                    
                    # if the tile is the colour of the current player, flip all of the tiles in flip_arr to current players colour
                    elif board[y][x] == current_player:
                        
                        for x,y in flip_arr:
                            flank_count+=1
                            board[y][x] = current_player
                        break
                    
                    # if the tile is the opposite colour, increment replace count and add the coord to the flip arr
                    else:
                        flip_arr.append((x,y))
                        #moves x and y one step in the right direction
                        x += direction[0]
                        y += direction[1]

                current_player = player_swap(current_player)
                
                #valid moves updates session
                session["current_player"] = current_player
                session["board"] = board
                session["move_counter"] = move_counter -1

                return jsonify( { "status": "success", "player": current_player, "board":board})
        else:
              return jsonify( { "status": "fail", "player": current_player, "message":"Move is not valid"})

if __name__ == "__main__":
    app.run(debug=True)