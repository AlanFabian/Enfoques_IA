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
grafo.add_edge("Inicio", "A", decision="Decisión 1")
grafo.add_edge("Inicio", "B", decision="Decisión 2")
grafo.add_edge("A", "C", decision="Decisión 3")
grafo.add_edge("B", "C", decision="Decisión 4")
grafo.add_edge("C", "Final", decision="Decisión 5")

# Dibujamos el grafo
pos = nx.spring_layout(grafo)
edge_labels = nx.get_edge_attributes(grafo, 'decision')
nx.draw_networkx(grafo, pos, with_labels=True, node_size=1000)
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)

# Mostramos el grafo
plt.axis('off')
plt.show()
