#Alan de Jesus Fabian Garcia 
from sympy import symbols, Equivalent, Implies, satisfiable

# Variables simbólicas
P, Q = symbols('P Q')

# Verificar equivalencia
formula1 = Equivalent(P, Q)
formula2 = Equivalent(~P, ~Q)
print(formula1.equals(formula2))  # Devuelve True (fórmulas equivalentes)

# Verificar validez
formula3 = Implies(P, Q)
print(formula3.is_valid())  # Devuelve True (fórmula válida en todos los casos)

# Verificar satisfacibilidad
formula4 = P & Q
print(satisfiable(formula4))  # Devuelve True (fórmula satisfacible)
