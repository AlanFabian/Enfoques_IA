import numpy as np
import matplotlib.pyplot as plt

# Definición de un conjunto difuso triangular
x = np.linspace(0, 10, 100)
membership = np.zeros_like(x)
membership[(x >= 2) & (x <= 8)] = (x[(x >= 2) & (x <= 8)] - 2) / 6
membership[(x > 8) & (x <= 10)] = (10 - x[(x > 8) & (x <= 10)]) / 2

# Gráfico del conjunto difuso triangular
plt.plot(x, membership)
plt.xlabel('Valor')
plt.ylabel('Grado de pertenencia')
plt.title('Conjunto difuso triangular')
plt.show()


################################################################
from pyclips import Environment, Symbol

# Crear un entorno de CLIPS
env = Environment()

# Cargar la extensión Fuzzy CLIPS
env.load('fuzzyclips')

# Definir un conjunto difuso triangular
env.eval('(deftemplate valor (slot x))')
env.eval('(fuzzy-triangle BAJO 0 0 5)')
env.assert_string('(valor (x 3))')

# Realizar inferencia difusa
env.eval('(defrule regla1 (valor (x BAJO)) => (printout t "El valor es bajo" crlf))')
env.run()

# Obtener el resultado difuso
result = env.eval('(fuzzy-match BAJO)')

# Imprimir el resultado difuso
print("Resultado difuso:", Symbol.string(result))
