
#Alan de Jesus Fabian Garcia 20/04/2023
import heapq

def bfs_cost(grafo,inicio,final):
    visitados= set()
    queue = [(0,inicio,[])]
    heapq.heapify(queue)
    while queue:
        (costo,nodo,path) = heapq.heappop(queue)
        if nodo not in visitados:
            visitados.add(nodo)
            path = path + [nodo]
            if nodo == final:
                return path
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    heapq.heappush(queue,(costo+grafo[nodo][vecino],vecino,path))
                    
    return None

def find_shortest_path_bfs_cost(grafo,inicio,final):
    path = bfs_cost(grafo,inicio,final)
    if path:
        return f"El camino mas corto de {inicio} a {final} es : {path} "
    else:
        return f"No se encontro ningun camino de {inicio} a {final}. "
    

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 3},
    'D': {'E': 1},
    'E': {}
}

# Encuentra el camino mas corto de A,E
inicio = 'A'
final  = 'E'
result = find_shortest_path_bfs_cost(grafo,inicio,final)

print(result)
