#Alan de Jesus Fabian Garcia 
from sympy import symbols, ForAll, Not, satisfiable

# Variables simbólicas
x, y = symbols('x y')

# Fórmula lógica
formula = ForAll(x, Not(ForAll(y, x != y)))

# Verificar satisfacibilidad
satisfiable_formula = satisfiable(formula)
print(satisfiable_formula)  # Devuelve un modelo de asignación de variables que satisface la fórmula
