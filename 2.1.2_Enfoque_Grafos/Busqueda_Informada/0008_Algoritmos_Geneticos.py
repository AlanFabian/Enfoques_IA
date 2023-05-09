import random 
# Función objetivo (aquí usamos la función de Rosenbrock)
def objective_function(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

# Parámetros del algoritmo genético
POPULATION_SIZE = 100  # Tamaño de la población
NUM_GENERATIONS = 50  # Número de generaciones
MUTATION_RATE = 0.1  # Tasa de mutación (probabilidad de que un gen sea mutado)
ELITE_PERCENTAGE = 0.2  # Porcentaje de la población considerado élite

# Funciones auxiliares para el algoritmo genético
def generate_individual():
    # Genera un individuo aleatorio (en este caso, un par de números entre -5 y 5)
    return (random.uniform(-5, 5), random.uniform(-5, 5))

def generate_population():
    # Genera una población inicial aleatoria
    return [generate_individual() for _ in range(POPULATION_SIZE)]

def evaluate_population(population):
    # Evalúa la función objetivo para cada individuo de la población
    return [(ind, objective_function(ind[0], ind[1])) for ind in population]

def select_parents(population):
    # Selecciona dos padres mediante selección de torneo (seleccionamos dos individuos aleatorios y tomamos el mejor)
    tournament_size = 2
    parents = []
    for i in range(2):
        tournament = random.sample(population, tournament_size)
        winner = min(tournament, key=lambda x: x[1])
        parents.append(winner[0])
    return parents

def crossover(parents):
    # Realiza el cruce (en este caso, un cruce de un punto)
    crossover_point = random.randint(1, len(parents[0]) - 1)
    child = parents[0][:crossover_point] + parents[1][crossover_point:]
    return child

def mutate(individual):
    # Realiza la mutación (en este caso, un cambio aleatorio en uno de los genes)
    mutated_index = random.randint(0, len(individual) - 1)
    mutated_value = random.uniform(-5, 5)
    return tuple(mutated_value if i == mutated_index else x for i, x in enumerate(individual))

# Función principal del algoritmo genético
def genetic_algorithm():
    # Genera la población inicial
    population = generate_population()
    for generation in range(NUM_GENERATIONS):
        # Evalúa la población actual
        evaluated_population = evaluate_population(population)
        # Selecciona la élite (los mejores individuos) y los padres para la siguiente generación
        elite_size = int(ELITE_PERCENTAGE * POPULATION_SIZE)
        elite = [x[0] for x in sorted(evaluated_population, key=lambda x: x[1])[:elite_size]]
        parents = [select_parents(evaluated_population) for _ in range(POPULATION_SIZE - elite_size)]
        # Realiza el cruce y la mutación para generar la siguiente generación
        next_generation = elite
        for pair in parents:
            child = crossover(pair)
            if random.random() < MUTATION_RATE:
                child = mutate(child)
            next_generation.append(child)
        # Actualiza la población actual con la siguiente generación
        population = next_generation
   
