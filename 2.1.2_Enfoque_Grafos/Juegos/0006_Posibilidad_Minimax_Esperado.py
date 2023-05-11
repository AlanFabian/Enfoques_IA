#Alan de Jesus Fabian Garcia 
import pygame
import random

# Definición del tablero
board = [' '] * 9
player = 'X'
computer = 'O'
game_over = False

# Definición de las combinaciones ganadoras
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
    [0, 4, 8], [2, 4, 6]  # Diagonales
]

# Inicialización de Pygame
pygame.init()
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gato (Tic-Tac-Toe)")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Función para dibujar el tablero
def draw_board():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (width / 3, 0), (width / 3, height), 2)
    pygame.draw.line(screen, WHITE, (width / 3 * 2, 0), (width / 3 * 2, height), 2)
    pygame.draw.line(screen, WHITE, (0, height / 3), (width, height / 3), 2)
    pygame.draw.line(screen, WHITE, (0, height / 3 * 2), (width, height / 3 * 2), 2)

    for i in range(len(board)):
        row = i // 3
        col = i % 3
        xpos = col * (width / 3) + (width / 3 / 2)
        ypos = row * (height / 3) + (height / 3 / 2)
        if board[i] == 'X':
            pygame.draw.line(screen, WHITE, (xpos - 20, ypos - 20), (xpos + 20, ypos + 20), 2)
            pygame.draw.line(screen, WHITE, (xpos + 20, ypos - 20), (xpos - 20, ypos + 20), 2)
        elif board[i] == 'O':
            pygame.draw.circle(screen, WHITE, (int(xpos), int(ypos)), 20, 2)

# Función para verificar si el juego ha terminado
def is_game_over():
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return True
    return ' ' not in board

# Función Minimax para determinar la mejor jugada
def minimax(board, depth, maximizing_player):
    # Definir los valores de evaluación para el jugador y la computadora
    player_score = 1
    computer_score = -1

    # Verificar si el juego ha terminado o si se alcanzó la profundidad máxima
    if is_game_over() or depth == 0:
        if is_game_over():
            if maximizing_player:
                return -1  # El jugador perdió
            else:
                return 1  # El jugador ganó
        else:
            return 0  # Empate

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = computer
                eval = minimax(board, depth - 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = player
                eval = minimax(board, depth - 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Función para realizar la jugada de la computadora utilizando el algoritmo Minimax
def make_computer_move():
    best_score = float('-inf')
    best_move = None
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = computer
            score = minimax(board, 5, False)  # Profundidad máxima de búsqueda
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = computer

# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and player == 'X':
            if pygame.mouse.get_pressed()[0]:
                xpos, ypos = pygame.mouse.get_pos()
                row = ypos // (height / 3)
                col = xpos // (width / 3)
                index = int(row * 3 + col)
                if board[index] == ' ':
                    board[index] = player
                    player = 'O'
                    if not is_game_over():
                        make_computer_move()
                        player = 'X'
                else:
                    print("Movimiento inválido. Inténtalo de nuevo.")

    draw_board()
    pygame.display.flip()

# Salir del juego
pygame.quit()
