import pytest
import components

#makes board for initialise_board() test
board_8x8 = [
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "Light", "-Dark", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-Dark", "Light", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
    ["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"]
    ]

board_2x2 = [["Light", "-Dark"],
            ["-Dark", "Light"]]

board_3x3 = [["Light", "-Dark","-None"],
            ["-Dark", "Light","-None"],
            ["-None","-None","-None"]]

board_15x15 = [
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "Light", "-Dark", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-Dark", "Light", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"],
["-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None", "-None"]
]

#initialise_board() testing
#NORMAL TESTS
def test_board_8x8():
    assert components.initialise_board() == board_8x8 #Normal test

#EDGE CASES
def test_board_2x2():
    assert components.initialise_board(size=2) == board_2x2 #edge case with small even size

def test_board_3x3():
    assert components.initialise_board(size=3) == board_3x3 #edge case with small odd size 

def test_board_15x15():
    assert components.initialise_board(size=15) == board_15x15 #edge case with large size

#ERRONEOUS
def test_board_0x0():
    assert components.initialise_board(size=0) == None #erroneous test with zero error

def test_board_string():
    assert components.initialise_board(size="abcd") == None #erroneous test with type error

#boards for legal_move() testing

board_one_valid_black = [
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

#NORMAL TESTS
def test_normal_move_dark():
    assert components.legal_move("-Dark",(3,2),board_8x8) == (True, [(0,1)]) #normal valid test for dark

def test_normal_move_light():
    assert components.legal_move("Light",(3,5),board_8x8) == (True, [(0,-1)]) #normal valid test for light

def test_invalid_dark():
    assert components.legal_move("-Dark",(0,0),board_8x8) == (False, None) #normal invalid test for dark

def test_invalid_light():
    assert components.legal_move("Light",(0,0),board_8x8) == (False, None) #normal invalid test for light

#EDGE CASES FOR VALID MOVES
def test_one_valid_black():
    assert components.legal_move("-Dark",(7,0),board_one_valid_black) == (True, [(-1,0)]) #edge case for valid black - only one legal move

def test_one_valid_light():
    assert components.legal_move("Light",(7,0),board_one_valid_light) == (True, [(-1,0)]) #edge case for valid light - only one legal move

#EDGE CASES FOR INVALID MOVES
def test_board_full_dark():
    assert components.legal_move("-Dark",(0,0),board_full) == (False, None) #edge case for invalid dark - no empty tiles

def test_board_full_light():
    assert components.legal_move("Light",(0,0),board_full) == (False, None) #edge case for invalid light - no empty tiles