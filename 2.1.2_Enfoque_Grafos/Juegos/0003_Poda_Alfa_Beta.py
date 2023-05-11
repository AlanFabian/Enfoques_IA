#Alan de Jesus Fabian Garcia 
import math
import random

# Función para imprimir el tablero
def print_board(board):
    print("-------------")
    print("| " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + " |")
    print("-------------")
    print("| " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + " |")
    print("-------------")
    print("| " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + " |")
    print("-------------")

# Función para verificar si alguien ha ganado
def is_winner(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or \
        (board[0] == player and board[3] == player and board[6] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[0] == player and board[4] == player and board[8] == player) or \
        (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# Función para obtener la lista de movimientos disponibles
def get_available_moves(board):
    moves = []
    for i in range(9):
        if board[i] == " ":
            moves.append(i)
    return moves

# Función que implementa el algoritmo Minimax con poda alfa-beta
def alpha_beta_pruning(board, depth, alpha, beta, is_max_player):
    # Verificar si el juego ha terminado o se ha alcanzado la profundidad máxima
    if is_winner(board, "X"):
        return -10 + depth, None
    elif is_winner(board, "O"):
        return 10 - depth, None
    elif len(get_available_moves(board)) == 0:
        return 0, None
    elif depth == 0:
        return 0, None

    # Si es el turno del jugador maximizador (O)
    if is_max_player:
        best_move = None
        best_score = -math.inf
        for move in get_available_moves(board):
            new_board = list(board)
            new_board[move] = "O"
            score, _ = alpha_beta_pruning(new_board, depth - 1, alpha, beta, False)
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score, best_move
    # Si es el turno del jugador minimizador (X)
    else:
        best_move = None
        best_score = math.inf
        for move in get_available_moves(board):
            new_board = list(board)
            new_board[move] = "X"
            score, _ = alpha_beta_pruning(new_board, depth - 1,alpha, beta, True)
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return best_score, best_move

# Ejemplo de uso del algoritmo
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
print_board(board)

while True:
    # Turno del jugador
    move = int(input("Ingrese su movimiento (0-8): "))
    while board[move] != " ":
        move = int(input("Esa casilla ya está ocupada. Ingrese otro movimiento: "))
    board[move] = "X"
    print_board(board)
    if is_winner(board, "X"):
        print("¡Ganaste!")
        break
    elif len(get_available_moves(board)) == 0:
        print("¡Empate!")
        break

    # Turno de la computadora
    _, move = alpha_beta_pruning(board, 5, -math.inf, math.inf, True)
    board[move] = "O"
    print_board(board)
    if is_winner(board, "O"):
        print("¡Perdiste!")
        break
    elif len(get_available_moves(board)) == 0:
        print("¡Empate!")
        break

