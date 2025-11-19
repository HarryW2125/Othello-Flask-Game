from flask import Flask, request, render_template, jsonify, session
import components
import random



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
        is_valid, direction = components.legal_move(current_player, (x,y), board)
        if is_valid == False:
            return jsonify( { "status": "fail", "player": current_player})

if __name__ == "__main__":
    app.run(debug=True)