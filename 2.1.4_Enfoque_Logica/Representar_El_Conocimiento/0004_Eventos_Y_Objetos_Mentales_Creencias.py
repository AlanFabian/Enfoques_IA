#Alan de Jesus Fabian Garcia 
class Evento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Creencia:
    def __init__(self, evento, certeza):
        self.evento = evento
        self.certeza = certeza


# Definición de eventos
evento1 = Evento("Llueve", "Está lloviendo.")
evento2 = Evento("Sol", "Hace sol.")

# Definición de creencias
creencia1 = Creencia(evento1, 0.8)
creencia2 = Creencia(evento2, 0.6)

# Imprimir información de creencias
print("Creencias:")
print("Evento:", creencia1.evento.nombre)
print("Descripción:", creencia1.evento.descripcion)
print("Certeza:", creencia1.certeza)
print()

print("Evento:", creencia2.evento.nombre)
print("Descripción:", creencia2.evento.descripcion)
print("Certeza:", creencia2.certeza)
