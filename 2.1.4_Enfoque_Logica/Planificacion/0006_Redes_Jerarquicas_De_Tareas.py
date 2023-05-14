#Alan de Jesus Fabian Garcia 
class Tarea:
    def __init__(self, nombre, sub_tareas=None):
        self.nombre = nombre
        self.sub_tareas = sub_tareas if sub_tareas else []

    def agregar_sub_tarea(self, sub_tarea):
        self.sub_tareas.append(sub_tarea)

    def ejecutar(self):
        print(f"Ejecutando tarea: {self.nombre}")

        for sub_tarea in self.sub_tareas:
            sub_tarea.ejecutar()


# Creación de la red jerárquica de tareas
tarea_principal = Tarea("Tarea Principal")

sub_tarea1 = Tarea("Sub Tarea 1")
sub_tarea2 = Tarea("Sub Tarea 2")
sub_tarea3 = Tarea("Sub Tarea 3")

sub_sub_tarea1 = Tarea("Sub Sub Tarea 1")
sub_sub_tarea2 = Tarea("Sub Sub Tarea 2")

sub_tarea1.agregar_sub_tarea(sub_sub_tarea1)
sub_tarea1.agregar_sub_tarea(sub_sub_tarea2)

tarea_principal.agregar_sub_tarea(sub_tarea1)
tarea_principal.agregar_sub_tarea(sub_tarea2)
tarea_principal.agregar_sub_tarea(sub_tarea3)

# Ejecución de la red jerárquica de tareas
tarea_principal.ejecutar()
