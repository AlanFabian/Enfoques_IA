
#Alan de Jesus Fabian Garcia 20/04/2023

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Funcion de busqueda en profundidad
def dfs(grafo,nodo_inicial):
    # Inicializar el conjunto de nodos visitados y la pila
    visitados = set()
    pila = [nodo_inicial]
    
    while pila:
        #sacar un nodo de la pila 
        nodo_actual = pila.pop()
        
        #Si el nodo no ha sido visitado aun,marcarlo como visitado  y lo imprimo
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            print(nodo_actual)
            
            #Agregar los vecinos del nodo actual a la pila 
            vecinos = grafo[nodo_actual]
            print(nodo_actual)
            
            #Agregar los vecinos del nodo actual a la pila 
            vecinos = grafo [nodo_actual]
            for vecino in vecinos:
                if vecino not in visitados:
                    pila.append(vecino)
                    
#Ejecutar la funcion de busqueda en profundidad 
dfs(grafo,'A')
#El grafo lo represento como un diccionario donde cada clave es un nodo y su valor es una lista de los nodos vecinos 
#La funcion dfs basicamente realizar una busqueda en profundidad a partir del nodo inicial que se le pasa como argumento.
#La busqueda en profundidad se realiza mediante  el uso de una pila y conjunto de nodos visitados
#Lo que hace que el algoritmo saque un nodo de la pila y lo marque como visitado , luego agrega todos los vecinos no visitados del nodo a la pila
#Se repite hasta que este vacia y al final imprimo los nodos visitados en orden de visita
