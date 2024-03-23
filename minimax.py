from func import *

def terminal(gamestate):
    for i in range(0, 9, 3):
        if gamestate[i] == gamestate[i+1] == gamestate[i+2] != 0:
            return True

    # Vertical
    for i in range(3):
        if gamestate[i] == gamestate[i+3] == gamestate[i+6] != 0:
            return True

    # Diagonals
    if gamestate[0] == gamestate[4] == gamestate[8] != 0:
        return True
    if gamestate[2] == gamestate[4] == gamestate[6] != 0:
        return True
    
    if 0 in gamestate:
        return False
    else:
        return True

def values(gamestate):
    for i in range(0, 9, 3):
        if gamestate[i] == gamestate[i+1] == gamestate[i+2] != 0:
            return -gamestate[i]

    # Vertical
    for i in range(3):
        if gamestate[i] == gamestate[i+3] == gamestate[i+6] != 0:
            return -gamestate[i]

    # Diagonals
    if gamestate[0] == gamestate[4] == gamestate[8] != 0:
            return -gamestate[0]
    if gamestate[2] == gamestate[4] == gamestate[6] != 0:
            return -gamestate[2]
    
    if 0 in gamestate:
        return None
    else:
        return 0  # No winners and no empty cells left, so the game is a tie

def player(gamestate):
    X_Count = sum(1 for move in gamestate if move == 1)
    O_Count = sum(1 for move in gamestate if move == -1)

    if X_Count == O_Count:
        if 0 in gamestate:
            return 'MIN'  # If the board is empty, it's O's turn to move
        return 'MAX'
    elif X_Count - O_Count == 1:
        return 'MAX'
    else:
        return 'NIL'

def actions(gamestate):
    available_actions = []
    for i in range(len(gamestate)):
        if gamestate[i] == 0:
            available_actions.append(i)
    return available_actions

def result(gamestate, action, turn):
    new_state = gamestate.copy()  # Create a copy of the gamestate
    new_state[action] = 1 if turn == 'MIN' else -1 if turn == 'MAX' else 0
    return new_state

import random

def minimax(gamestate, turn):
    print("Current gamestate:", gamestate)
    print("Current player:", turn)
    
    if terminal(gamestate):
        actions_list = actions(gamestate)
        if actions_list:
            return values(gamestate), actions_list[0]  # Return any available move in terminal states
        else:
            return values(gamestate), None
    
    if turn == 'MAX':
        best_value = float('-inf')
        best_move = None
        for a in actions(gamestate):
            value, _ = minimax(result(gamestate, a, 'MIN'), 'MIN')  # Ensure that the next turn is for MIN player
            if value > best_value:
                best_value = value
                best_move = a
        return best_value, best_move
    
    if turn == 'MIN':
        best_value = float('inf')
        best_move = None
        for a in actions(gamestate):
            value, _ = minimax(result(gamestate, a, 'MAX'), 'MAX')  # Ensure that the next turn is for MAX player
            if value < best_value:
                best_value = value
                best_move = a
        return best_value, best_move

gamestate = [1, 0, 0, 0, 0, 0, 0, 0, 0]
best_value, best_move = minimax(gamestate, player(gamestate))
print("Best Move:", best_move)
print("Value of Best Move:", best_value)