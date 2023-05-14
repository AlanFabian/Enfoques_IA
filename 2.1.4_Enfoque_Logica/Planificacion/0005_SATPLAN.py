#Alan de Jesus Fabian Garcia 
from pysat.solvers import Glucose3

def satplan(conditions_iniciales, conditions_objetivo, acciones):
    # Crear un solver SAT
    solver = Glucose3()

    # Crear variables proposicionales para las condiciones iniciales y objetivo
    variables = {}
    for condition in conditions_iniciales | conditions_objetivo:
        variables[condition] = solver.new_var()

    # Agregar cláusulas para las condiciones iniciales
    for condition in conditions_iniciales:
        solver.add_clause([variables[condition]])

    # Agregar cláusulas para las acciones y efectos
    for accion in acciones:
        for precondicion in accion['precondiciones']:
            solver.add_clause([-variables[precondicion], variables[accion['nombre']]])

        for efecto in accion['efectos']:
            solver.add_clause([-variables[accion['nombre']], variables[efecto]])

    # Agregar cláusulas para las condiciones objetivo
    objetivo_satisfecho = [variables[condition] for condition in conditions_objetivo]
    solver.add_clause(objetivo_satisfecho)

    # Resolver el problema de satisfacción booleana
    if solver.solve():
        plan = []
        for accion in acciones:
            if solver.model[variables[accion['nombre']]] > 0:
                plan.append(accion['nombre'])
        return plan
    else:
        return None

# Definición de las acciones y sus precondiciones y efectos
acciones = [
    {
        'nombre': 'A',
        'precondiciones': ['estado1'],
        'efectos': ['estado2']
    },
    {
        'nombre': 'B',
        'precondiciones': ['estado2'],
        'efectos': ['estado3']
    },
    {
        'nombre': 'C',
        'precondiciones': ['estado3'],
        'efectos': ['estado4']
    }
]

# Definición de las condiciones iniciales y objetivo
conditions_iniciales = {'estado1'}
conditions_objetivo = {'estado4'}

# Ejecutar el algoritmo SATPLAN
plan = satplan(conditions_iniciales, conditions_objetivo, acciones)

# Imprimir el plan generado
if plan is not None:
    print("Plan:", plan)
else:
    print("No se pudo encontrar un plan para alcanzar las condiciones objetivo.")
