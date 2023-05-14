#Alan de Jesus Fabian Garcia 
import random


def hill_climbing(initial_state, objective_function, neighbors_function):
    current_state = initial_state
    while True:
        neighbors = neighbors_function(current_state)
        if not neighbors:
            break
        neighbor = max(neighbors, key=lambda state: objective_function(state))
        if objective_function(neighbor) <= objective_function(current_state):
            break
        current_state = neighbor
    return current_state


# Ejemplo de uso

# Función objetivo: valor absoluto
def objective_function(x):
    return abs(x)

# Función para generar vecinos
def neighbors_function(x):
    return [x + random.choice([-1, 1])]

# Estado inicial
initial_state = random.randint(-10, 10)

# Ejecutar algoritmo de Hill Climbing
result = hill_climbing(initial_state, objective_function, neighbors_function)

# Imprimir resultado
print("Resultado:")
print(f"Estado inicial: {initial_state}")
print(f"Mejor estado encontrado: {result}")
print(f"Valor objetivo: {objective_function(result)}")
