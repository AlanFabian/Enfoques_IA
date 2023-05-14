#Alan de Jesus Fabian Garcia 
class Agente:
    def __init__(self, nombre, planificador):
        self.nombre = nombre
        self.planificador = planificador

    def ejecutar_accion(self):
        accion = self.planificador.obtener_siguiente_accion(self.nombre)
        print(f"{self.nombre} ejecuta acción: {accion}")

    def actualizar_estado(self, nuevo_estado):
        self.planificador.actualizar_estado(self.nombre, nuevo_estado)


class PlanificadorContinuo:
    def __init__(self, acciones_iniciales):
        self.acciones = acciones_iniciales.copy()

    def obtener_siguiente_accion(self, agente):
        return self.acciones[agente].pop(0)

    def actualizar_estado(self, agente, nuevo_estado):
        print(f"Actualizando estado del agente {agente}: {nuevo_estado}")
        # Aquí iría la lógica para actualizar el estado del agente en el planificador


# Acciones iniciales
acciones_iniciales = {
    'agente1': ['A1', 'B1', 'C1'],
    'agente2': ['A2', 'B2', 'C2']
}

# Creación del planificador continuo
planificador = PlanificadorContinuo(acciones_iniciales)

# Creación de los agentes
agente1 = Agente('Agente 1', planificador)
agente2 = Agente('Agente 2', planificador)

# Ejecución continua de acciones
while True:
    agente1.ejecutar_accion()
    agente2.ejecutar_accion()

    # Aquí se realizarían las actualizaciones del estado de los agentes según las percepciones del entorno

    # Si se cumplen ciertas condiciones, se podría agregar más acciones al planificador o modificar las existentes
    if some_condition:
        planificador.acciones['agente1'].append('D1')

    if other_condition:
        planificador.acciones['agente2'].insert(0, 'Z2')

 

