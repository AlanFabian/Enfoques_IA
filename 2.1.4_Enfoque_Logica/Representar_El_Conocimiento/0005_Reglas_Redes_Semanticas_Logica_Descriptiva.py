#Alan de Jesus Fabia Garcia 
from pyDatalog import pyDatalog

# Definición de reglas
pyDatalog.create_terms('padre, abuelo, bisabuelo, X, Y, Z')

+padre('Juan', 'Pedro')
+padre('Pedro', 'Diego')

# Regla para definir al abuelo
abuelo(X, Y) <= padre(X, Z) & padre(Z, Y)

# Regla para definir al bisabuelo
bisabuelo(X, Y) <= abuelo(X, Z) & padre(Z, Y)

# Consultas
print(abuelo('Juan', X))  # X = Diego
print(bisabuelo('Juan', X))  # X = Diego
