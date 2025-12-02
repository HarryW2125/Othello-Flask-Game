import pytest
import flask_game_engine_ai

#boards for tests
board_starting = [
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "Light", "-Dark", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-Dark", "Light", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"]
    ]

board_diff_flips_light= [
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "Light", "-Dark", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-Dark", "Light", "-None", "-None", "-None"],
    ["-None", "-None", "-Dark", "-Dark", "-Dark", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"]
    ]
  
board_half_full = [
    ["-None", "-None", "-None", "Light", "-Dark", "-None", "Light", "-None"],
    ["Light", "-None", "-None", "-Dark", "Light", "-None", "-Dark", "-None"],
    ["-None", "-Dark", "-None", "-None", "-None", "Light", "-Dark", "Light"],
    ["Light", "-None", "-Dark", "-None", "-None", "-Dark", "Light", "-None"],
    ["-None", "Light", "-None", "-Dark", "-None", "-None", "Light", "-Dark"],
    ["-Dark", "-None", "-Dark", "-None", "Light", "-None", "-None", "-Dark"],
    ["-None", "Light", "-None", "-Dark", "-None", "Light", "-None", "-None"],
    ["Light", "-Dark", "-None", "-None", "-Dark", "-None", "Light", "-None"]
]

board_empty = [
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"]
    ]

board_full = [
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"]
]

board_one_valid_dark = [
    ["-Dark",  "Light", "Light", "Light", "Light", "Light", "Light", "-None"],
    ["Light", "Light",  "Light", "Light", "Light", "Light", "Light", "Light"],
    ["Light", "Light", "Light",  "Light", "Light", "Light", "Light", "Light"],
    ["Light", "Light", "Light", "Light",  "Light", "Light", "Light", "Light"],
    ["Light", "Light", "Light", "Light", "Light",  "Light", "Light", "Light"],
    ["Light", "Light", "Light", "Light", "Light", "Light",  "Light", "Light"],
    ["Light", "Light", "Light", "Light", "Light", "Light", "Light",  "Light"],
    ["Light", "Light", "Light", "Light", "Light", "Light", "Light", "Light"]
]

board_one_valid_light = [
    ["Light", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-None"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"],
    ["-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark", "-Dark"]
]

board_no_valid_dark = [
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "Light", "Light", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "Light", "Light", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"]
    ]

board_no_valid_light = [
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-Dark", "-Dark", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-Dark", "-Dark", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"]
    ]

#player_swap() testing

def test_player_swap_dark():
    assert flask_game_engine_ai.player_swap("-Dark") == "Light" #normal test from light -> dark

def test_player_swap_light():
    assert flask_game_engine_ai.player_swap("Light") == "-Dark" #normal test from dark -> light

#check_all_moves() testing

#NORMAL CASES
def test_check_valid_dark():
    assert flask_game_engine_ai.check_all_moves("-Dark",board_starting) == True #normal test for valid moves present

def test_check_valid_light():
    assert flask_game_engine_ai.check_all_moves("Light",board_starting) == True #normal test for valid moves present

def test_check_invalid_dark():
    assert flask_game_engine_ai.check_all_moves("-Dark",board_no_valid_dark) == False #normal test for no valid moves

def test_check_invalid_light():
    assert flask_game_engine_ai.check_all_moves("Light",board_no_valid_light) == False #normal test for no valid moves


#VALID EDGE CASES
def test_check_one_dark():
    assert flask_game_engine_ai.check_all_moves("-Dark",board_one_valid_dark) == True #one valid move

def test_check_one_light():
    assert flask_game_engine_ai.check_all_moves("Light",board_one_valid_light) == True #one valid move

#INVALID EDGE CASES
def test_check_moves_full():
    assert flask_game_engine_ai.check_all_moves("Dark",board_full) == False #case where board is full

def test_check_moves_empty():
    assert flask_game_engine_ai.check_all_moves("Light",board_empty) == False #case where board is empty

#tile_counts() testing

#NORMAL CASES
def test_tile_count_start_board():
    assert flask_game_engine_ai.tile_counts(board_starting) == (2,2) #normal case for relatively empty board

def test_tile_count_normal_board():
    assert flask_game_engine_ai.tile_counts(board_half_full) == (15,15) # normal case for board with 30 nonempty tiles

#EDGE CASES
def test_tile_count_empty_board():
    assert flask_game_engine_ai.tile_counts(board_empty) == (0,0) #edge case with empty board

def test_tile_count_full_board():
    assert flask_game_engine_ai.tile_counts(board_full) == (0,64) #edge case where board is full of dark values

#ai_move() testing

#NORMAL CASES
def test_ai_move_small_board():
    assert flask_game_engine_ai.ai_move(board_starting) == (4,2) #normal case for starting board

def test_ai_move_normal_board():
    assert flask_game_engine_ai.ai_move(board_diff_flips_light) == (5,5) #normal case with multiple valid moves for light that flip different numbers of tiles

#EDGE CASES
def test_ai_move_empty():
    assert flask_game_engine_ai.ai_move(board_empty) == None #edge case with empty board

def test_ai_move_full():
    assert flask_game_engine_ai.ai_move(board_full) == None #edge case with full board

def test_ai_one_move():
    assert flask_game_engine_ai.ai_move(board_one_valid_light) == (7,0) #edge case with one valid move
