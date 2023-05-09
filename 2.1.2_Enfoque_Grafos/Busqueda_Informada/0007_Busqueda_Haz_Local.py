import random

# Función objetivo (aquí usamos la función de Rosenbrock)
def objective_function(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

# Función de búsqueda de haz local
def local_beam_search(beam_width, x_min, x_max, y_min, y_max, max_iter):
    # Generamos un conjunto de estados iniciales aleatorios
    states = [(random.uniform(x_min, x_max), random.uniform(y_min, y_max)) for _ in range(beam_width)]
    for i in range(max_iter):
        # Evaluamos la función objetivo para cada estado
        values = [(s, objective_function(s[0], s[1])) for s in states]
        # Ordenamos los estados por su valor de la función objetivo (de menor a mayor)
        values.sort(key=lambda x: x[1])
        # Tomamos los primeros estados (los de menor valor de la función objetivo)
        states = [v[0] for v in values[:beam_width]]
        # Si todos los estados tienen el mismo valor de la función objetivo, terminamos
        if len(set([v[1] for v in values])) == 1:
            break
    # Devolvemos el estado con menor valor de la función objetivo
    return min(states, key=lambda x: objective_function(x[0], x[1]))

# Ejemplo de uso
best_state = local_beam_search(beam_width=10, x_min=-5, x_max=5, y_min=-5, y_max=5, max_iter=100)
print(f"El estado con menor valor de la función objetivo es ({best_state[0]}, {best_state[1]}) con un valor de {objective_function(best_state[0], best_state[1])}.")
