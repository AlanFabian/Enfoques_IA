#Alan de Jesus Fabian Garcia 
class AccionCondicional:
    def __init__(self, condiciones, acciones):
        self.condiciones = condiciones
        self.acciones = acciones

    def es_aplicable(self, estado):
        return all(estado[condicion] for condicion in self.condiciones)

    def ejecutar(self):
        for accion in self.acciones:
            accion.ejecutar()


class Accion:
    def __init__(self, nombre):
        self.nombre = nombre

    def ejecutar(self):
        print(f"Ejecutando acción: {self.nombre}")


# Definición de las acciones condicionales
accion_condicional1 = AccionCondicional(['condicion1', 'condicion2'], [
    Accion('Acción 1.1'),
    Accion('Acción 1.2')
])

accion_condicional2 = AccionCondicional(['condicion3'], [
    Accion('Acción 2.1')
])

# Definición del estado inicial
estado_inicial = {
    'condicion1': True,
    'condicion2': True,
    'condicion3': False
}

# Ejecución de la planificación condicional
if accion_condicional1.es_aplicable(estado_inicial):
    accion_condicional1.ejecutar()

if accion_condicional2.es_aplicable(estado_inicial):
    accion_condicional2.ejecutar()
