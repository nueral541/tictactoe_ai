from func import *

def terminal(gamestate):
    # Check for winners
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

    # Check for a tie
    if 0 not in gamestate:
        return True  # No winners and no empty cells left, so the game is a tie
    
    return False

def values(gamestate):
    # Check for winners
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

    # Check for a tie
    if 0 not in gamestate:
        return 0  # No winners and no empty cells left, so the game is a tie

def player(gamestate):
    X_Count = 0
    O_Count = 0
    for move in gamestate:
        if move == 1:
            X_Count += 1
        elif move == -1:
            O_Count += 1

    if X_Count == O_Count:
        return 'MIN'
    elif X_Count - O_Count == 1:
        return 'MAX'
    else:
        return 'NIL'

def actions(gamestate):
    actions = []
    for i in range(len(gamestate)):
        if gamestate[i] == 0:
            actions.append(i)
    
    return actions

def result(gamestate, action, turn):
    new_state = gamestate.copy()  # Create a copy of the gamestate
    new_state[action] = 1 if turn == 'MIN' else -1 if turn == 'MAX' else 0
    return new_state

def minimax(gamestate):

    if terminal(gamestate):
        return values(gamestate)
    
    if player(gamestate) == 'MAX':
        value = float('-inf')
        for a in actions(gamestate):
            value = max(value, minimax(result(gamestate, a, 'MAX')))
        return value
    
    if player(gamestate) == 'MIN':
        value = float('inf')
        for a in actions(gamestate):
            value = min(value, minimax(result(gamestate, a, 'MIN')))
        return value
    
def find_best_move(gamestate):
    best_move = None
    best_value = float('-inf')
    
    for action in actions(gamestate):
        value = minimax(result(gamestate, action, player(gamestate)))
        if value > best_value:
            best_value = value
            best_move = action
    
    return best_move