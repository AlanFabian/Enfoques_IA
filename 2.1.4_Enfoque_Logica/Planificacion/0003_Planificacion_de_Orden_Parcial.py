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

def planificacion_orden_parcial(estados_iniciales, estados_objetivo, acciones):
    plan = []
    estados = estados_iniciales.copy()

    while estados_objetivo - estados:
        acciones_aplicables = [accion for accion in acciones if accion.es_aplicable(estados)]

        if not acciones_aplicables:
            raise Exception("No se puede alcanzar el estado objetivo desde el estado inicial.")

        for accion in acciones_aplicables:
            estados_siguientes = accion.aplicar(estados)
            if estados_siguientes - estados:
                estados = estados.union(estados_siguientes)
                plan.append(accion.nombre)
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

# Ejecutar la planificación de orden parcial
plan = planificacion_orden_parcial(estado_inicial, estado_objetivo, acciones)

# Imprimir el plan generado
print("Plan:", plan)
