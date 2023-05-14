#Alan de Jesus Fabian Garcia 
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos


class Situacion:
    def __init__(self, nombre, acciones):
        self.nombre = nombre
        self.acciones = acciones


class Evento:
    def __init__(self, nombre, situaciones):
        self.nombre = nombre
        self.situaciones = situaciones


# Definición de acciones
accion1 = Accion("AbrirPuerta", ["PuertaCerrada"], ["PuertaAbierta"])
accion2 = Accion("CerrarPuerta", ["PuertaAbierta"], ["PuertaCerrada"])

# Definición de situaciones
situacion1 = Situacion("Inicio", [])
situacion2 = Situacion("Situacion1", [accion1])
situacion3 = Situacion("Situacion2", [accion2])

# Definición de eventos
evento1 = Evento("Evento1", [situacion1, situacion2])
evento2 = Evento("Evento2", [situacion1, situacion3])

# Imprimir información de acciones, situaciones y eventos
print("Acciones:")
print(accion1.nombre)
print(accion1.precondiciones)
print(accion1.efectos)
print()

print("Situaciones:")
print(situacion1.nombre)
print([accion.nombre for accion in situacion1.acciones])
print()

print("Eventos:")
print(evento1.nombre)
print([situacion.nombre for situacion in evento1.situaciones])
