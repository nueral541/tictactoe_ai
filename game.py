from func import *
from minimax import find_best_move

gamestate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
running = True
winner = None

print("Let's play tictactoe!")
print("To play, type in a number based on the scoring guide below!")
print_guide()
print("X goes first!")

while running:
    # Player X's turn
    gamestate = play_turn('X', gamestate)
    result = asess_turn(gamestate)
    if result != 0:
        winner = 'X' if result == 1 else 'O'
        break  # Exit the loop if there's a winner
    elif 0 not in gamestate:  # Check if the board is full
        break  # Exit the loop if it's a tie

    # AI Player O's turn
    best_move = find_best_move(gamestate)
    if best_move != -1 and gamestate[best_move] == 0:
        gamestate[best_move] = -1  # Place O's symbol at the best move position
    else:
        print("AI Player is f*cking stuupid")

    # Check for winner or full board after O's turn
    result = asess_turn(gamestate)
    if result != 0:
        winner = 'X' if result == 1 else 'O'
        break  # Exit the loop if there's a winner
    elif 0 not in gamestate:  # Check if the board is full
        break  # Exit the loop if it's a tie

print_board(gamestate)
if winner:
    print("Congratulations!")
    print(f"{winner} wins!")
else:
    print("It's a tie!")
