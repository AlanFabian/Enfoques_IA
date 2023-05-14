#Alan de Jesus Fabian Garcia 
import random

# Definimos una lista de números de ejemplo
numeros_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creamos un diccionario para almacenar las transiciones
transiciones = {}

# Recorremos la lista de números para construir las transiciones
for i in range(len(numeros_ejemplo) - 1):
    numero_actual = numeros_ejemplo[i]
    numero_siguiente = numeros_ejemplo[i + 1]

    # Verificamos si el número actual ya existe en el diccionario
    if numero_actual in transiciones:
        transiciones[numero_actual].append(numero_siguiente)
    else:
        transiciones[numero_actual] = [numero_siguiente]

# Imprimimos las transiciones para verificar
for numero, siguientes in transiciones.items():
    print(numero, "->", siguientes)

# Función para generar una secuencia de números usando el modelo de Markov
def generar_secuencia(longitud):
    numero_inicial = random.choice(numeros_ejemplo)
    secuencia = [numero_inicial]

    for _ in range(longitud - 1):
        numero_actual = secuencia[-1]
        if numero_actual in transiciones:
            siguientes_posibles = transiciones[numero_actual]
            numero_siguiente = random.choice(siguientes_posibles)
            secuencia.append(numero_siguiente)
        else:
            break

    return secuencia

# Generamos una secuencia de longitud 10
secuencia_generada = generar_secuencia(10)
print("Secuencia generada:", secuencia_generada)
