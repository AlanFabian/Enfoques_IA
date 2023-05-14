#Alan de Jesus Fabian Garcia 
import random

# Función objetivo
def funcion_objetivo(x):
    return 0.3 * x**2 + 0.5 * x + 2

# Rango de valores para x
x_min = -10
x_max = 10

# Rango de valores para y (máximo valor de la función objetivo)
y_max = funcion_objetivo(0)

# Función de muestreo directo
def muestreo_directo(n):
    muestras = []
    for _ in range(n):
        x = random.uniform(x_min, x_max)  # Generar un valor aleatorio de x en el rango
        y = random.uniform(0, y_max)  # Generar un valor aleatorio de y en el rango máximo
        if y <= funcion_objetivo(x):
            muestras.append(x)
    return muestras

# Función de muestreo por rechazo
def muestreo_rechazo(n):
    muestras = []
    while len(muestras) < n:
        x = random.uniform(x_min, x_max)  # Generar un valor aleatorio de x en el rango
        y = random.uniform(0, y_max)  # Generar un valor aleatorio de y en el rango máximo
        if y <= funcion_objetivo(x):
            muestras.append(x)
    return muestras

# Ejemplo de uso de muestreo directo
n_muestras = 1000
muestras_directo = muestreo_directo(n_muestras)
print("Muestras obtenidas por muestreo directo:")
print(muestras_directo)

# Ejemplo de uso de muestreo por rechazo
n_muestras = 1000
muestras_rechazo = muestreo_rechazo(n_muestras)
print("\nMuestras obtenidas por muestreo por rechazo:")
print(muestras_rechazo)
