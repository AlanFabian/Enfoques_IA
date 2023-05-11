#Alan de Jesus Fabian Garcia 
import pygame

# Tamaño del tablero y casillas
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

# Definir los valores de las piezas (puedes ajustarlos según tus preferencias)
piece_values = {
    'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0,
    'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': 0
}

# Profundidad máxima para el efecto horizonte
MAX_DEPTH = 3

# Función de evaluación del estado del tablero con corte por efecto horizonte
def evaluate_board(board, depth):
    # Verificar si se alcanzó la profundidad máxima
    if depth >= MAX_DEPTH:
        return 0

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

# Función de búsqueda con corte por efecto horizonte (Alfa-Beta)
def alpha_beta_search(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return evaluate_board(node.state, depth)

    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, alpha_beta_search(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alpha_beta_search(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

# Clase que representa un nodo del juego de ajedrez
class ChessNode:
    def __init__(self, state):
        self.state = state
        self.children = self.generate_children()

    def generate_children(self):
        children = []
        # Generar posibles movimientos y crear nuevos nodos para cada movimiento
        # Agregar los nuevos nodos a la lista de children
        # ...

    def is_terminal(self):
        # Verificar si el nodo es un estado terminal (fin del juego)
        # ...

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

        # Clase que representa un nodo del juego de ajedrez
        class ChessNode:
            def __init__(self, state):
                self.state = state
                self.children = self.generate_children()

            def generate_children(self):
                children = []
                # Generar posibles movimientos y crear nuevos nodos para cada movimiento
                # Agregar los nuevos nodos a la lista de children
                # ...

            def is_terminal(self):
                # Verificar si el nodo es un estado terminal (fin del juego)
                # ...

        # Inicializar Pygame
                pygame.init()
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
                clock = pygame.time.Clock()

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
                        # Dibujar texto en lugar de imágenes de las piezas
                        font = pygame.font.Font(None, 100)
                        if piece.isupper():
                            text_color = (255, 255, 255)  # Color para las piezas blancas
                        else:
                            text_color = (0, 0, 0)  # Color para las piezas negras

                        text = font.render(piece, True, text_color)
                        text_rect = text.get_rect(center=(x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2))
                        screen.blit(text, text_rect)

            # Dibujar etiquetas de las filas y columnas
            font = pygame.font.Font(None, 36)
            for i in range(8):
                x = i * SQUARE_SIZE + SQUARE_SIZE // 2 - 10
                y = HEIGHT - SQUARE_SIZE // 2 - 10
                text = font.render(chr(ord('a') + i), True, (255, 255, 255))
                screen.blit(text, (x, y))
                text = font.render(str(8 - i), True, (255, 255, 255))
                screen.blit(text, (10, i * SQUARE_SIZE + SQUARE_SIZE // 2 - 10))

        # Función principal del juego
        def main():
            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                screen.fill((0, 0, 0))
                draw_board()

                # Ejemplo de uso de la función de evaluación con corte por efecto horizonte
                score = alpha_beta_search(ChessNode(board), MAX_DEPTH, float('-inf'), float('inf'), True)
                print("Puntaje del tablero:", score)

                pygame.display.flip()
                clock.tick(60)

            pygame.quit()

        # Ejecutar el juego
        if __name__ == '__main__':
            main()


