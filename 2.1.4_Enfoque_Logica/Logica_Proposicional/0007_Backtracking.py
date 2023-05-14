#Alan de Jesus Fabian Garcia 
def backtracking_search(assignment, constraints):
    if len(assignment) == len(constraints):
        return assignment
    
    var = select_unassigned_variable(assignment, constraints)
    for value in order_domain_values(var, assignment, constraints):
        if is_consistent(var, value, assignment, constraints):
            assignment[var] = value
            result = backtracking_search(assignment, constraints)
            if result is not None:
                return result
            assignment[var] = None

    return None


def select_unassigned_variable(assignment, constraints):
    unassigned_vars = [var for var in constraints if var not in assignment]
    return min(unassigned_vars, key=lambda var: len(constraints[var]))


def order_domain_values(var, assignment, constraints):
    return constraints[var]


def is_consistent(var, value, assignment, constraints):
    for constraint in constraints[var]:
        if constraint[0] == var:
            other_var = constraint[1]
            if other_var in assignment and assignment[other_var] == value:
                return False
    return True


# Ejemplo de uso

# Variables
variables = ['A', 'B', 'C']

# Dominios de variables
domains = {
    'A': [1, 2, 3],
    'B': [1, 2],
    'C': [3]
}

# Restricciones
constraints = {
    'A': [('A', 'B')],
    'B': [('B', 'A'), ('B', 'C')],
    'C': [('C', 'B')]
}

# Realizar búsqueda de backtracking
assignment = {}
result = backtracking_search(assignment, constraints)

# Imprimir resultado
if result is not None:
    print("Asignación encontrada:")
    for var, value in result.items():
        print(f"{var}: {value}")
else:
    print("No se encontró ninguna asignación válida.")
