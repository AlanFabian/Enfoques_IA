#Alan de Jesus Fabian Garcia
import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo vacío
grafo = nx.DiGraph()

# Agregamos los nodos a la red de decisión
grafo.add_node("Inicio")
grafo.add_node("A")
grafo.add_node("B")
grafo.add_node("C")
grafo.add_node("Final")

# Agregamos las aristas que representan las decisiones y resultados
grafo.add_edge("Inicio", "A", decision="Decisión 1", valor_informacion=0.6)
grafo.add_edge("Inicio", "B", decision="Decisión 2", valor_informacion=0.4)
grafo.add_edge("A", "C", decision="Decisión 3", valor_informacion=0.8)
grafo.add_edge("B", "C", decision="Decisión 4", valor_informacion=0.2)
grafo.add_edge("C", "Final", decision="Decisión 5", valor_informacion=1.0)

# Definimos una función para realizar la iteración de valores
def iteracion_valores(grafo):
    # Inicializamos los valores de los nodos a cero
    valores = {nodo: 0 for nodo in grafo.nodes}
    
    # Realizamos la iteración de valores
    while True:
        nuevos_valores = valores.copy()
        for nodo in grafo.nodes:
            if nodo == "Final":
                nuevos_valores[nodo] = 0
            else:
                valor_maximo = max([grafo[nodo][sucesor]['valor_informacion'] + valores[sucesor]
                                    for sucesor in grafo.successors(nodo)])
                nuevos_valores[nodo] = valor_maximo
        if nuevos_valores == valores:
            break
        valores = nuevos_valores
    
    return valores

# Ejecutamos la iteración de valores
valores = iteracion_valores(grafo)

# Mostramos los valores de cada nodo
for nodo, valor in valores.items():
    print(f"Valor de {nodo}: {valor}")

# Dibujamos el grafo con los valores de los nodos
pos = nx.spring_layout(grafo)
node_labels = {nodo: f"{nodo}\nValor: {valores[nodo]:.2f}" for nodo in grafo.nodes}
nx.draw_networkx(grafo, pos, with_labels=True, node_size=1000)
nx.draw_networkx_labels(grafo, pos, labels=node_labels)

# Mostramos el grafo
plt.axis('off')
plt.show()
