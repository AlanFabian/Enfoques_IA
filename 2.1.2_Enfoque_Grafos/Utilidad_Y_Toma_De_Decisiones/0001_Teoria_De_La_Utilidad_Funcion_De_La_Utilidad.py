#Alan de Jesus Fabian Garcia 
import random

def calcular_conflictos(estado, grafo):
    conflictos = 0
    for nodo in estado:
        for vecino in grafo[nodo]:
            if estado[nodo] == estado[vecino]:
                conflictos += 1
    return conflictos

def calcular_utilidad(nodo, valor, estado_actual, grafo):
    utilidad = 0
    for vecino in grafo[nodo]:
        if estado_actual[vecino] == valor:
            utilidad += 1
    return utilidad

def minimos_conflictos(estado_inicial, grafo, max_iteraciones):
    estado_actual = estado_inicial.copy()

    for _ in range(max_iteraciones):
        if calcular_conflictos(estado_actual, grafo) == 0:
            return estado_actual

        nodos_con_conflicto = []
        for nodo in estado_actual:
            for vecino in grafo[nodo]:
                if estado_actual[nodo] == estado_actual[vecino]:
                    nodos_con_conflicto.append(nodo)
                    break

        if len(nodos_con_conflicto) > 0:
            nodo_conflicto = random.choice(nodos_con_conflicto)
            vecinos = grafo[nodo_conflicto]

            mejores_estados = []
            max_utilidad = float('-inf')

            for valor in vecinos:
                utilidad = calcular_utilidad(nodo_conflicto, valor, estado_actual, grafo)

                if utilidad > max_utilidad:
                    mejores_estados = [valor]
                    max_utilidad = utilidad
                elif utilidad == max_utilidad:
                    mejores_estados.append(valor)

            estado_actual[nodo_conflicto] = random.choice(mejores_estados)
        else:
            nodo = random.choice(list(grafo.keys()))
            valor = random.choice(grafo[nodo])
            estado_actual[nodo] = valor

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
