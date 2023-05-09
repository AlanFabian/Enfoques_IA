import time

# Función que simula el entorno
def simulate_environment(action):
    # Simula el resultado de una acción en el entorno
    time.sleep(0.5)
    if action == "up":
        return (1, 0)
    elif action == "down":
        return (-1, 0)
    elif action == "left":
        return (0, -1)
    elif action == "right":
        return (0, 1)
    else:
        return (0, 0)

# Función de búsqueda en línea
def online_search():
    # Estado inicial
    state = (0, 0)
    print("Estado inicial:", state)
    # Bucle de búsqueda
    while True:
        # Pide una acción al usuario
        action = input("Introduzca una acción (up/down/left/right): ")
        # Realiza la acción en el entorno y actualiza el estado
        movement = simulate_environment(action)
        state = (state[0] + movement[0], state[1] + movement[1])
        print("Nuevo estado:", state)
