# Tic-Tac-Toe with Minimax AI 🎮

A command-line Tic-Tac-Toe game in Python where you play against an unbeatable AI powered by the **Minimax algorithm**.

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Gameplay](#gameplay)
- [Project Structure](#project-structure)
- [Algorithm Details](#algorithm-details)
- [License](#license)

---

## About

This is a classic Tic-Tac-Toe game played in the terminal. The computer opponent uses the **Minimax algorithm** to evaluate every possible future game state and always make the optimal move — meaning it will never lose. The best outcome you can achieve is a draw!

---

## Features

- ♟️ Play against an AI that never loses
- 🧠 Minimax algorithm for perfect decision-making
- 🖥️ Clean, visual board displayed in the terminal
- ✅ Input validation (detects bad moves and occupied cells)
- ⚡ No external dependencies — pure Python

---

## How It Works

- **You** play as `O`
- **The computer** plays as `X` and always goes first (taking the center)
- The board is numbered 1–9, left-to-right, top-to-bottom:

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

---

## Getting Started

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/your-username/tic-tac-toe-minimax.gitl;km
cd tic-tac-toe-minimax
```

### Run the Game

```bash
python tictactoe.py
```

---

## Gameplay

1. The computer (`X`) starts in the center.
2. Enter a number (1–9) to place your `O` on the board.
3. The game ends when someone wins or the board is full (draw).

**Example turn:**

```
Enter your move: 1
```

**Example result:**

```
You won!
```
or
```
I won!
```
or
```
Tie!
```

---

## Project Structure

```
tic-tac-toe-minimax/
│
├── tictactoe.py       # Main game file
└── README.md          # Project documentation
```

### Key Functions

| Function | Description |
|---|---|
| `display_board(board)` | Renders the current board state in the terminal |
| `enter_move(board)` | Handles and validates the human player's input |
| `make_list_of_free_fields(board)` | Returns a list of all unoccupied cells |
| `victory_for(board, sgn)` | Checks if a given player has won |
| `minimax(board, is_max)` | Recursively evaluates all possible game states |
| `draw_move(board)` | Picks and plays the computer's best move |

---

## Algorithm Details

The AI uses the **Minimax algorithm**, a decision-making algorithm for two-player zero-sum games.

- The AI (`X`) is the **maximizing** player — it tries to get the highest score.
- The human (`O`) is the **minimizing** player — it tries to get the lowest score.
- Scores: `+1` if X wins, `-1` if O wins, `0` for a draw.

The algorithm explores every possible future board state recursively and selects the move that guarantees the best outcome, making it truly unbeatable.

```
Score:  +1 → Computer wins
         0 → Draw
        -1 → Human wins
```

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with Python 🐍 | Powered by Minimax 🧠
