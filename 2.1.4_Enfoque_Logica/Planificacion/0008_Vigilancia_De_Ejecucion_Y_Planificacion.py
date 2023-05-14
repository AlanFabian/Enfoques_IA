#Alan de Jesus Fabian Garcia 
class Planificador:
    def __init__(self, acciones, estado_inicial):
        self.acciones = acciones
        self.estado_actual = estado_inicial

    def ejecutar_plan(self, plan):
        for accion in plan:
            if self.verificar_precondiciones(accion):
                self.ejecutar_accion(accion)
                self.actualizar_estado(accion)
            else:
                print(f"No se pueden cumplir las precondiciones de la acción: {accion}")
                self.replanificar(accion)

    def verificar_precondiciones(self, accion):
        return all(precondicion in self.estado_actual for precondicion in accion['precondiciones'])

    def ejecutar_accion(self, accion):
        print(f"Ejecutando acción: {accion['nombre']}")

    def actualizar_estado(self, accion):
        for efecto in accion['efectos']:
            self.estado_actual.add(efecto)

    def replanificar(self, accion):
        print("Replanificando...")

        # Aquí iría la lógica de replanificación para generar un nuevo plan


# Definición de las acciones y su estructura
acciones = [
    {
        'nombre': 'A',
        'precondiciones': {'estado1'},
        'efectos': {'estado2'}
    },
    {
        'nombre': 'B',
        'precondiciones': {'estado2'},
        'efectos': {'estado3'}
    },
    {
        'nombre': 'C',
        'precondiciones': {'estado3'},
        'efectos': {'estado4'}
    }
]

# Definición del estado inicial
estado_inicial = {'estado1'}

# Definición del plan a ejecutar
plan = ['A', 'B', 'C']

# Creación del planificador
planificador = Planificador(acciones, estado_inicial)

# Ejecución del plan con vigilancia de ejecución y replanificación
planificador.ejecutar_plan(plan)
