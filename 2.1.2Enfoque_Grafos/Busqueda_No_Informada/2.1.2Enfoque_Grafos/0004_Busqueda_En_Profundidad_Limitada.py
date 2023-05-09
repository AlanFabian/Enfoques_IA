#Alan de Jesus Fabian Garcia 20/04/2023
# Definir la estructura del grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#Funcion de busqeuda en profundidad limitada
def dlfs(grafo,nodo_inicial,profundidad_limite):
    #Inicializo el conjunto de nodos visitados y la pila 
    visitados = set ()
    pila = [(nodo_inicial,0)]
    
    while pila:
        #Sacar un nodo y su profundidad de la pila 
        nodo_actual,profundidad_actual = pila.pop()
        
        #Si el nodo no ha sido visitado y no excede la profundidad
        #Marcarlo como visitado para procesarlo 
        if nodo_actual not in visitados and profundidad_actual <= profundidad_limite:
            visitados.add(nodo_actual)
            print(nodo_actual)
            
            #Agrego los vecinos del nodo actual con una profundidad
            #Menor o igual a la profundiad limite a la pila 
            vecinos = grafo [nodo_actual]
            for vecino in vecinos:
                if vecino not in visitados and profundidad_actual < profundidad_limite:
                    pila.append((vecino,profundidad_actual+1))

dlfs(grafo,'A',2)
