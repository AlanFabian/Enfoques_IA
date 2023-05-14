#Alan de Jesus Fabian Garcia 
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

    def es_aplicable(self, estado):
        return all(precondicion in estado for precondicion in self.precondiciones)

    def aplicar(self, estado):
        if self.es_aplicable(estado):
            estado.update(self.efectos)
            return estado
        else:
            raise Exception("La acción no se puede aplicar al estado actual.")

def graphplan(estados_iniciales, estados_objetivo, acciones):
    niveles = [[estados_iniciales]]
    nivel = 0

    while True:
        if estados_objetivo.issubset(niveles[nivel][-1]):
            return construir_plan(niveles, nivel, acciones)

        nuevos_estados = expandir_estados(niveles[nivel], acciones)
        if nuevos_estados.issubset(niveles[nivel][-1]):
            return None

        niveles.append(nuevos_estados)
        nivel += 1

def expandir_estados(estados, acciones):
    nuevos_estados = set()

    for accion in acciones:
        if accion.es_aplicable(estados[-1]):
            nuevos_estados.update(accion.aplicar(estados[-1]))

    return nuevos_estados

def construir_plan(niveles, nivel, acciones):
    plan = []

    for i in range(nivel, 0, -1):
        for accion in acciones:
            if accion.aplicar(niveles[i-1]) == niveles[i]:
                plan.insert(0, accion.nombre)
                break

    return plan

# Definición de las acciones
acciones = [
    Accion('A', {'estado1'}, {'estado2'}),
    Accion('B', {'estado2'}, {'estado3'}),
    Accion('C', {'estado3'}, {'estado4'})
]

# Definición del estado inicial y el estado objetivo
estado_inicial = {'estado1'}
estado_objetivo = {'estado4'}

# Ejecutar el algoritmo GRAPHPLAN
plan = graphplan(estado_inicial, estado_objetivo, acciones)

# Imprimir el plan generado
if plan is not None:
    print("Plan:", plan)
else:
    print("No se pudo encontrar un plan para alcanzar el estado objetivo.")
