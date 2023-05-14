#Alan de Jesus Fabian Garcia 
from sympy import symbols, Or, Not, to_cnf, satisfiable

# Variables simbólicas
P, Q, R = symbols('P Q R')

# Resolución
formula1 = (P | Q) & (~P | R) & (~Q | ~R)
resolution = formula1.resolve()
print(resolution)  # Devuelve (Q | R)

# Forma Normal Conjuntiva (FNC)
formula2 = (P & Q) | (~R & P) | (Not(P) & Not(Q) & R)
fnc = to_cnf(formula2)
print(fnc)  # Devuelve (P | ~Q | ~R) & (P | R)

# Verificar satisfacibilidad de la FNC
satisfiable_fnc = satisfiable(fnc)
print(satisfiable_fnc)  # Devuelve un modelo de asignación de variables que satisface la fórmula
