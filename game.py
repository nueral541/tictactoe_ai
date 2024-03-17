from func import *
from minimax import find_best_move, make_move

print("Let's play Tic Tac Toe!")
print("To play, type in a number based on the scoring guide below!")
print_guide()
print("X goes first!")
winner = None  # Initialize winner as None
running = True
while running:
    # Player X's turn
    gamestate = play_turn('X', gamestate)
    result = assess_turn(gamestate)
    if result != 0:
        winner = 'X' if result == 1 else 'O'
        break  # Exit the loop if there's a winner
    elif 0 not in gamestate:  # Check if the board is full
        break  # Exit the loop if it's a tie

    # AI player O's turn
    best_move = find_best_move(gamestate, depth=9, winner=winner)  # Pass winner to find_best_move
    gamestate = make_move(gamestate, best_move, is_x=False)

    result = assess_turn(gamestate)
    if result != 0:
        winner = 'X' if result == 1 else 'O'
        break  # Exit the loop if there's a winner
    elif 0 not in gamestate:  # Check if the board is full
        break  # Exit the loop if it's a tie

if winner:
    print_board(gamestate)
    print("Congratulations!")
    print(f"{winner} wins!")
else:
    print("It's a tie!")
