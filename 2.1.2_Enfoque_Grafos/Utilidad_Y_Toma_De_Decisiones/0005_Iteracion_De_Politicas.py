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

# Definimos una función para realizar la iteración de políticas
def iteracion_politicas(grafo):
    # Inicializamos las políticas de los nodos
    politicas = {nodo: None for nodo in grafo.nodes}
    
    # Realizamos la iteración de políticas
    while True:
        nuevas_politicas = politicas.copy()
        for nodo in grafo.nodes:
            if nodo == "Final":
                nuevas_politicas[nodo] = None
            else:
                politica_maxima = max([(grafo[nodo][sucesor]['valor_informacion'] + politicas[sucesor], sucesor)
                                        for sucesor in grafo.successors(nodo)], key=lambda x: x[0])[1]
                nuevas_politicas[nodo] = politica_maxima
        if nuevas_politicas == politicas:
            break
        politicas = nuevas_politicas
    
    return politicas

# Ejecutamos la iteración de políticas
politicas = iteracion_politicas(grafo)

# Mostramos las políticas de cada nodo
for nodo, politica in politicas.items():
    print(f"Política de {nodo}: {politica}")

# Dibujamos el grafo con las políticas de los nodos
pos = nx.spring_layout(grafo)
node_labels = {nodo: f"{nodo}\nPolítica: {politicas[nodo]}" for nodo in grafo.nodes}
nx.draw_networkx(grafo, pos, with_labels=True, node_size=1000)
nx.draw_networkx_labels(grafo, pos, labels=node_labels)

# Mostramos el grafo
plt.axis('off')
plt.show()
