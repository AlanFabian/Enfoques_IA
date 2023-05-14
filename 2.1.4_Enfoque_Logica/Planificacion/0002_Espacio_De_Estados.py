#Alan de Jesus Fabian Garcia 
class Estado:
    def __init__(self, nombre, acciones_posibles):
        self.nombre = nombre
        self.acciones_posibles = acciones_posibles

    def aplicar_accion(self, accion):
        # Lógica para aplicar la acción y obtener el nuevo estado
        pass

# Definición de los estados y acciones posibles
estado_inicial = Estado("Estado Inicial", ["A", "B"])
estado_intermedio = Estado("Estado Intermedio", ["C"])
estado_final = Estado("Estado Final", [])

# Definición de las acciones y sus efectos
acciones = {
    "A": {"efecto": estado_intermedio},
    "B": {"efecto": estado_final},
    "C": {"efecto": estado_final}
}

# Ejemplo de transición de estados mediante una secuencia de acciones
estado_actual = estado_inicial

# Aplicar acción A
accion_seleccionada = "A"
if accion_seleccionada in estado_actual.acciones_posibles:
    estado_siguiente = acciones[accion_seleccionada]["efecto"]
    estado_actual = estado_siguiente
else:
    print("La acción seleccionada no es válida para el estado actual.")

# Aplicar acción B
accion_seleccionada = "B"
if accion_seleccionada in estado_actual.acciones_posibles:
    estado_siguiente = acciones[accion_seleccionada]["efecto"]
    estado_actual = estado_siguiente
else:
    print("La acción seleccionada no es válida para el estado actual.")

# Imprimir el estado actual
print("Estado actual:", estado_actual.nombre)
