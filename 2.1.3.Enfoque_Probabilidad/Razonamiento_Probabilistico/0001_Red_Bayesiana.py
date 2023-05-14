#Alan de Jesus Fabian Garcia 
class NodoRedBayesiana:
    def __init__(self, nombre, probabilidad):
        self.nombre = nombre
        self.probabilidad = probabilidad
        self.padres = []
    
    def agregar_padre(self, padre):
        self.padres.append(padre)


class RedBayesiana:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, nombre, probabilidad):
        nodo = NodoRedBayesiana(nombre, probabilidad)
        self.nodos[nombre] = nodo
    
    def agregar_relacion(self, nombre_hijo, nombre_padre):
        hijo = self.nodos[nombre_hijo]
        padre = self.nodos[nombre_padre]
        hijo.agregar_padre(padre)
    
    def propagacion_hacia_adelante(self, evidencia):
        # Inicializar las probabilidades posteriores
        probabilidades_posteriores = {}
        
        # Propagación hacia adelante
        for nombre, nodo in self.nodos.items():
            if nombre in evidencia:
                # Si el nodo está en la evidencia, la probabilidad posterior es 1 si se cumple y 0 si no
                probabilidades_posteriores[nombre] = 1 if evidencia[nombre] else 0
            else:
                # Si el nodo no está en la evidencia, se calcula la probabilidad posterior utilizando la regla de Bayes
                probabilidad_padres = 1
                for padre in nodo.padres:
                    probabilidad_padres *= probabilidades_posteriores[padre.nombre]
                
                probabilidad = nodo.probabilidad[evidencia[nombre]]
                probabilidad_posterior = probabilidad * probabilidad_padres
                probabilidades_posteriores[nombre] = probabilidad_posterior
        
        # Devolver las probabilidades posteriores
        return probabilidades_posteriores


# Crear una red bayesiana simple
red_bayesiana = RedBayesiana()

# Agregar los nodos de la red bayesiana con sus probabilidades
red_bayesiana.agregar_nodo('A', [0.3, 0.7])  # Probabilidad P(A)
red_bayesiana.agregar_nodo('B', [0.2, 0.8])  # Probabilidad P(B)
red_bayesiana.agregar_nodo('C', [0.4, 0.6, 0.5, 0.5])  # Probabilidad P(C|A,B)

# Agregar las relaciones entre los nodos
red_bayesiana.agregar_relacion('C', 'A')
red_bayesiana.agregar_relacion('C', 'B')

# Realizar razonamiento probabilístico propagando hacia adelante en la red
evidencia = {'A': True, 'B': False}  # Se conoce que A es verdadero y B es falso
probabilidades_posteriores = red_bayesiana.propagacion_hacia_adelante(evidencia)

# Imprimir las probabilidades posteriores
print("Probabilidades posteriores:")
for nombre, probabilidad in probabilidades_posteriores.items():
    print(f'P({nombre}) = {probabilidad}')
