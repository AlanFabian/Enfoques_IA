# Definir la estructura del grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Función de búsqueda de profundidad iterativa
def iddfs(grafo, nodo_inicial):
    # Definir una función auxiliar que realiza la búsqueda en profundidad limitada
    def dfs_limitada(nodo_actual, profundidad_limite, profundidad_actual):
        # Si el nodo no ha sido visitado y no excede la profundidad límite,
        # marcarlo como visitado y procesarlo
        if nodo_actual not in visitados and profundidad_actual <= profundidad_limite:
            visitados.add(nodo_actual)
            print(nodo_actual)

            # Si la profundidad límite no ha sido alcanzada,
            # agregar los vecinos del nodo actual con una profundidad
            # menor o igual a la profundidad límite a la pila
            if profundidad_actual < profundidad_limite:
                vecinos = grafo[nodo_actual]
                for vecino in vecinos:
                    dfs_limitada(vecino, profundidad_limite, profundidad_actual+1)

    # Inicializar el conjunto de nodos visitados
    visitados = set()

    # Ejecutar la búsqueda en profundidad iterativa
    profundidad_limite = 0
    while True:
        # Reiniciar el conjunto de nodos visitados
        visitados = set()

        # Ejecutar la búsqueda en profundidad limitada con la profundidad límite actual
        dfs_limitada(nodo_inicial, profundidad_limite, 0)

        # Incrementar la profundidad límite
        profundidad_limite += 1

        # Si todos los nodos han sido visitados, salir del bucle
        if len(visitados) == len(grafo):
            break

# Ejecutar la función de búsqueda de profundidad iterativa
iddfs(grafo, 'A')
