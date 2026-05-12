from random import randrange

def display_board(board):
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")


def enter_move(board):
    ok = False
    while not ok:
        move = input("Enter your move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Bad move - repeat your input!")
            continue

        move = int(move) - 1
        row = move // 3
        col = move % 3

        if board[row][col] in ['O','X']:
            print("Field already occupied - repeat your input!")
            continue

        ok = True

    board[row][col] = 'O'


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O','X']:
                free.append((row,col))
    return free


def victory_for(board, sgn):
    if sgn == "X":
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        who = None

    cross1 = cross2 = True

    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn:
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:
            cross2 = False

    if cross1 or cross2:
        return who

    return None



def minimax(board, is_max):
    if victory_for(board, 'X') == 'me':
        return 1
    if victory_for(board, 'O') == 'you':
        return -1

    free = make_list_of_free_fields(board)
    if not free:
        return 0

    if is_max:
        best = -100
        for row, col in free:
            temp = board[row][col]
            board[row][col] = 'X'

            score = minimax(board, False)

            board[row][col] = temp
            best = max(best, score)
        return best
    else:
        best = 100
        for row, col in free:
            temp = board[row][col]
            board[row][col] = 'O'

            score = minimax(board, True)

            board[row][col] = temp
            best = min(best, score)
        return best



def draw_move(board):
    best_score = -100
    best_move = None

    for row, col in make_list_of_free_fields(board):
        temp = board[row][col]
        board[row][col] = 'X'

        score = minimax(board, False)

        board[row][col] = temp

        if score > best_score:
            best_score = score
            best_move = (row, col)

    row, col = best_move
    board[row][col] = 'X'



board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'  

human_turn = True

while True:
    display_board(board)

    free = make_list_of_free_fields(board)
    if not free:
        break

    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')

    if victor is not None:
        break

    human_turn = not human_turn


display_board(board)

if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won!")
else:
    print("Tie!")
