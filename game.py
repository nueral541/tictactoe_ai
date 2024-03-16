from func import *
from minimax import find_winning_combos, evaluate, find_best_move, make_move

print("Let's play Tic Tac Toe!")
print("To play, type in a number based on the scoring guide below!")
print_guide()
print("X goes first!")

running = True
while running:
    # Player X's turn
    gamestate = play_turn('X', gamestate)
    result = asess_turn(gamestate)
    if result != 0:
        winner = 'X' if result == 1 else 'O'
        break  # Exit the loop if there's a winner
    elif 0 not in gamestate:  # Check if the board is full
        break  # Exit the loop if it's a tie

    # AI player O's turn
    print("AI (O) is thinking...")
    best_move = find_best_move(gamestate, depth=3)  # Adjust depth as needed
    gamestate = make_move(gamestate, best_move, is_x=False)

    print_board(gamestate)

    result = asess_turn(gamestate)
    if result != 0:
        winner = 'X' if result == 1 else 'O'
        break  # Exit the loop if there's a winner
    elif 0 not in gamestate:  # Check if the board is full
        break  # Exit the loop if it's a tie

if winner:
    print("Congratulations!")
    print(f"{winner} wins!")
else:
    print("It's a tie!")
