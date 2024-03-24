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
    
def print_board(gamestate):
    for i in range(0, 9, 3):
        print(gamestate[i:i+3])

def main():
    gamestate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    while not terminal(gamestate):
        print("Current board:")
        print_board(gamestate)
        player_move = int(input("Enter your move (0-8): "))
        if gamestate[player_move] == 0:
            gamestate[player_move] = 1  # Assuming player is 'X'
        else:
            print("Invalid move, try again.")
            continue
        
        if terminal(gamestate):
            break
        
        # AI move
        print("AI's move:")
        best_move = None
        best_value = float('-inf')
        for action in actions(gamestate):
            value = minimax(result(gamestate, action, 'MAX'))
            if value > best_value:
                best_value = value
                best_move = action
        gamestate[best_move] = -1  # Assuming AI is 'O'
    
    print("Final board:")
    print_board(gamestate)
    if values(gamestate) == -1:
        print("You win!")
    elif values(gamestate) == 1:
        print("AI wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
