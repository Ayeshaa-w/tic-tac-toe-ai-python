import tkinter as tk
from tkinter import messagebox

board = [""] * 9
current_player = "O"

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    return None

def on_click(i):
    global current_player
    if board[i] == "":
        board[i] = current_player
        buttons[i].config(text=current_player)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            reset()
            return

        if "" not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset()
            return

        current_player = "X" if current_player == "O" else "O"

def reset():
    global board, current_player
    board = [""] * 9
    current_player = "O"
    for btn in buttons:
        btn.config(text="")

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
