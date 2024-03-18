from func import *

def evaluate(gamestate):
    win = asess_turn(gamestate)
    if win == 1:
        return 10
    elif win == -1:
        return -10
    else:
        return 0
    
def legal_moves(gamestate):
    """
    Returns a list of indices representing legal moves in the current gamestate.
    """
    return [i for i, cell in enumerate(gamestate) if cell == 0]

def minimax(gamestate, depth, is_maximizing):
    score = evaluate(gamestate)

    # Base case: if the game is over or reached maximum depth
    if abs(score) == 10 or depth == 0:
        return score

    # Get legal moves
    legal_moves_list = legal_moves(gamestate)

    # If it's the maximizing player's turn (AI)
    if is_maximizing:
        best_score = -float('inf')
        for move in legal_moves_list:
            gamestate[move] = 1
            score = minimax(gamestate, depth - 1, False)
            gamestate[move] = 0  # Reset the move
            best_score = max(best_score, score)
        return best_score

    # If it's the minimizing player's turn (opponent)
    else:
        best_score = float('inf')
        for move in legal_moves_list:
            gamestate[move] = -1
            score = minimax(gamestate, depth - 1, True)
            gamestate[move] = 0  # Reset the move
            best_score = min(best_score, score)
        return best_score
    
def find_best_move(gamestate):
    best_move = -1
    best_score = -float('inf')

    for i in range(9):
        if gamestate[i] == 0:
            gamestate[i] = -1  # Assume AI player's move (maximizing player)
            score = minimax(gamestate, depth=5, is_maximizing=False)  # Assuming opponent's turn
            gamestate[i] = 0  # Reset the move
            if score > best_score:
                best_score = score
                best_move = i + 1  # Convert index to position (1-9)
    
    return best_move