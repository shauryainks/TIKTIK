# Tic-Tac-Toe with Minimax Algorithm

This Python program implements a simple console-based Tic-Tac-Toe game using the minimax algorithm for artificial intelligence (AI) player moves. The game is played on a 3x3 board, and the players take turns to make a move until the game is won, lost, or drawn.

## Table of Contents

- [Requirements](#requirements)
- [How to Play](#how-to-play)
- [Minimax Algorithm](#minimax-algorithm)
- [Implementation Details](#implementation-details)
- [Run the Game](#run-the-game)

## Requirements

- Python 3.x

## How to Play

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-minimax.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tic-tac-toe-minimax
   ```

3. Run the game:

   ```bash
   python tictactoe.py
   ```

4. Follow the on-screen instructions to choose your player and make moves.

## Minimax Algorithm

The minimax algorithm is a decision-making algorithm commonly used in two-player turn-based games to find the optimal move for a player. It evaluates all possible moves and their outcomes to determine the best move that maximizes the player's chances of winning or minimizes the opponent's chances.

In the context of Tic-Tac-Toe, the minimax algorithm is employed for the AI player (computer) to make intelligent moves. It explores all possible future game states, assigns a score to each state, and chooses the move that leads to the highest score for the AI player or the lowest score for the opponent.

## Implementation Details

- The game uses the console for interaction.
- The players are represented as 'X' and 'O'.
- The AI player ('O') employs the minimax algorithm to determine the optimal move.
- The program ensures that the user inputs valid moves and prevents illegal moves.
- The game displays the current state of the board after each move.

## Run the Game

To run the Tic-Tac-Toe game with the minimax algorithm:

```bash
python tictactoe.py
```

Follow the on-screen instructions to choose your player ('X' or 'O') and make moves. The AI player will use the minimax algorithm to determine its moves, providing a challenging opponent for the player. The game continues until there is a winner, a draw, or the user decides to exit.

Enjoy playing Tic-Tac-Toe with a smart AI opponent!
