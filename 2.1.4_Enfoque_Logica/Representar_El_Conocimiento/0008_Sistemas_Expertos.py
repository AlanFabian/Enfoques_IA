#Alan de Jesus Fabian Garcia 
from pyknow import *

class Enfermedad(Fact):
    """Clase que representa los hechos (enfermedad) en el sistema experto."""
    pass

class Sintoma(Fact):
    """Clase que representa los hechos (síntomas) en el sistema experto."""
    pass

class Diagnostico(KnowledgeEngine):
    @Rule(Enfermedad('resfriado') & Sintoma('fiebre'))
    def regla1(self):
        self.declare(Enfermedad('resfriado'))

    @Rule(Enfermedad('gripe') & Sintoma('dolor_garganta'))
    def regla2(self):
        self.declare(Enfermedad('gripe'))

    @Rule(Enfermedad('gripe') & Sintoma('fiebre'))
    def regla3(self):
        self.declare(Enfermedad('gripe'))

    @Rule(Enfermedad('resfriado') & NOT(Sintoma('fiebre')))
    def regla4(self):
        self.declare(Enfermedad('resfriado'))

# Crear el motor de inferencia
motor_inferencia = Diagnostico()

# Establecer los hechos iniciales
motor_inferencia.reset()
motor_inferencia.declare(Sintoma('fiebre'))

# Ejecutar el motor de inferencia
motor_inferencia.run()

# Obtener los resultados
resultado = motor_inferencia.facts

# Imprimir el diagnóstico
for fact in resultado:
    if isinstance(fact, Enfermedad):
        print("El paciente tiene:", fact)


