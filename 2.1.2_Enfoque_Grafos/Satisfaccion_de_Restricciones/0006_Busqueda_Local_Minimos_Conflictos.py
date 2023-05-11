#Alan de Jesus Fabian Garcia 
import random

def calcular_conflictos(estado, grafo):
    conflictos = 0
    for nodo in estado:
        for vecino in grafo[nodo]:
            if estado[nodo] == estado[vecino]:
                conflictos += 1
    return conflictos

def minimos_conflictos(estado_inicial, grafo, max_iteraciones):
    estado_actual = estado_inicial.copy()

    for _ in range(max_iteraciones):
        if calcular_conflictos(estado_actual, grafo) == 0:
            return estado_actual

        nodo_conflicto = random.choice(list(estado_actual.keys()))
        vecinos = grafo[nodo_conflicto]

        mejores_estados = []
        min_conflictos = float('inf')

        for valor in vecinos:
            estado_actual[nodo_conflicto] = valor
            conflictos = calcular_conflictos(estado_actual, grafo)

            if conflictos < min_conflictos:
                mejores_estados = [valor]
                min_conflictos = conflictos
            elif conflictos == min_conflictos:
                mejores_estados.append(valor)

        estado_actual[nodo_conflicto] = random.choice(mejores_estados)

    return None

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

estado_inicial = {
    'A': 'Rojo',
    'B': 'Azul',
    'C': 'Verde',
    'D': 'Rojo'
}

max_iteraciones = 100

estado_final = minimos_conflictos(estado_inicial, grafo, max_iteraciones)

if estado_final is None:
    print("No se encontró una solución en el número máximo de iteraciones.")
else:
    print("Estado final:")
    print(estado_final)
