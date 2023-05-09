grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 6)],
    'E': []
}

def busqueda_direccional(grafo,inicio,objetivo):
    #Inicializo el conjunto de nodos visitados desde el inicio y desde el objetivo 
    visitado_inicio = set()
    visitado_objetivo = set()
    #Inicializo las colas de busqueda desde el inicio hasta el objetivo 
    cola_inicio = [(inicio,0)]
    cola_objetivo =[(objetivo,0)]
    #Inicializo los diccionarios encargados de la distancia desde el inicio y desde el objetivo 
    distancia_inicio = {inicio:0}
    distancia_objetivo = {objetivo:0}
    #Inicializo el nodo actual y la distancia minima 
    nodo_actual = None
    distancia_minima= float('inf')
    
    #Funcion para reconstruir el camino minimo desde el inicio hasta el objetivo
    def camino_minimo(nodo,distancia_inicio,distancia_objetivo):
        ruta_inicio = []
        ruta_objetivo = []
        while nodo != inicio:
            for adyacente ,costo in grafo [nodo]:
                if adyacente in distancia_inicio and distancia_inicio[adyacente]==distancia_inicio[nodo]-costo:
                    ruta_inicio.append(adyacente)
                    nodo = adyacente
                    break
        ruta_inicio.reverse()
        nodo = objetivo
        while nodo != inicio:
            for adyacente, costo in grafo[nodo]:
                if adyacente in distancia_objetivo and distancia_objetivo[adyacente] == distancia_objetivo[nodo] - costo:
                    ruta_objetivo.append(adyacente)
                    nodo = adyacente
                    break
        return ruta_inicio + ruta_objetivo[::-1]
    
    # Buscar desde el inicio y desde el objetivo al mismo tiempo
    while cola_inicio and cola_objetivo:
        # Expandir el nodo con la menor distancia desde el inicio
        distancia, (nodo_actual,i) = min((distancia_inicio[nodo], (nodo, i)) for i, (nodo, _) in enumerate(cola_inicio))
        cola_inicio.pop(i)
        visitado_inicio.add(nodo_actual)
        # Comprobar si el nodo actual ha sido visitado desde el objetivo
        if nodo_actual in visitado_objetivo:
            # Calcular la distancia total y la ruta
            distancia_total = distancia + distancia_objetivo[nodo_actual]
            ruta = [nodo_actual] + camino_minimo(nodo_actual, distancia_inicio, distancia_objetivo)
            print("La distancia entre", inicio, "y", objetivo, "es:", distancia_total)
            return ruta, distancia_total
        # Expandir los nodos adyacentes desde el nodo actual
        for adyacente, costo in grafo[nodo_actual]:
            if adyacente not in visitado_inicio:
                nueva_distancia = distancia + costo
                cola_inicio.append((adyacente, nueva_distancia))
                # Actualizar la distancia desde el inicio
                if adyacente not in distancia_inicio or nueva_distancia < distancia_inicio[adyacente]:
                    distancia_inicio[adyacente] = nueva_distancia
        # Expandir el nodo con la menor distancia desde el objetivo
        distancia, (nodo_actual, i) = min((distancia_objetivo[nodo], (nodo,i)) for i,(nodo, _) in enumerate(cola_objetivo))
        cola_objetivo.pop(i)
        visitado_objetivo.add(nodo_actual)
