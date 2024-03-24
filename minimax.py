from func import *

def evaluate(gamestate):
    win = asess_turn(gamestate)
    if win == 1:
        return 10
    elif win == -1:
        return -10
    else:
        return True

def value(gamestate):
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
    
gamestate = [1, -1, 0, 1, 0, -1, 1, 0, 0]

acts = actions(gamestate)

for i in acts:
    print(result(gamestate, i, player(gamestate)))