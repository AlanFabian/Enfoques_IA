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
    
    def calcular_probabilidad_conjunta(self, evidencia):
        # Inicializar la probabilidad conjunta
        probabilidad_conjunta = 1
        
        # Calcular la probabilidad conjunta utilizando la regla de la cadena
        for nombre, nodo in self.nodos.items():
            probabilidad = nodo.probabilidad[evidencia[nombre]]
            
            for padre in nodo.padres:
                probabilidad_padre = nodo.probabilidad[evidencia[padre.nombre]]
                probabilidad *= probabilidad_padre
            
            probabilidad_conjunta *= probabilidad
        
        # Devolver la probabilidad conjunta
        return probabilidad_conjunta


# Crear una red bayesiana simple
red_bayesiana = RedBayesiana()

# Agregar los nodos de la red bayesiana con sus probabilidades
red_bayesiana.agregar_nodo('A', [0.3, 0.7])  # Probabilidad P(A)
red_bayesiana.agregar_nodo('B', [0.2, 0.8])  # Probabilidad P(B)
red_bayesiana.agregar_nodo('C', [0.4, 0.6, 0.5, 0.5])  # Probabilidad P(C|A,B)

# Agregar las relaciones entre los nodos
red_bayesiana.agregar_relacion('C', 'A')
red_bayesiana.agregar_relacion('C', 'B')

# Calcular la probabilidad conjunta dada una evidencia específica
evidencia = {'A': True, 'B': False, 'C': True}  # Se conoce que A es verdadero, B es falso y C es verdadero
probabilidad_conjunta = red_bayesiana.calcular_probabilidad_conjunta(evidencia)

# Imprimir la probabilidad conjunta
print("Probabilidad Conjunta:")
print(f'P(A=True, B=False, C=True) = {probabilidad_conjunta}')
