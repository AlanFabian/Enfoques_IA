import pygame

# Tamaño del tablero y casillas
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

# Definir los valores de las piezas (puedes ajustarlos según tus preferencias)
piece_values = {
    'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0,
    'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': 0
}

# Función de evaluación del estado del tablero
def evaluate_board(board):
    player_score = 0
    opponent_score = 0

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '.':
                if piece.isupper():
                    player_score += piece_values[piece]
                else:
                    opponent_score += piece_values[piece]

    return player_score - opponent_score

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Tablero de ajedrez
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

# Función para dibujar el tablero
def draw_board():
    for row in range(8):
        for col in range(8):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            piece = board[row][col]
            if piece != '.':
                font = pygame.font.Font(None, 50)
                text = font.render(piece, True, (0, 0, 0))
                text_rect = text.get_rect(center=(x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2))
                screen.blit(text, text_rect)

# ...

# Función principal del juego
def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        draw_board()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Ejecutar el juego
if __name__ == '__main__':
    main()
