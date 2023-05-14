#Alan de Jesus Fabian Garcia 
from pyDatalog import pyDatalog

# Definición de hechos y reglas
pyDatalog.create_terms('padre, abuelo, X, Y')

+padre('Juan', 'Pedro')
+padre('Pedro', 'Diego')

# Reglas de razonamiento por defecto
abuelo(X, Y) <= padre(X, Z) & padre(Z, Y)
abuelo(X, Y) <= padre(X, Z) & abuelo(Z, Y)

# Consultas
print(abuelo('Juan', Y))  # Y = Pedro, Diego
