#Alan de Jesus Fabian Garcia 
class FOIL:
    def __init__(self):
        self.reglas = []

    def generar_reglas(self, ejemplos_positivos, ejemplos_negativos):
        for ejemplo_positivo in ejemplos_positivos:
            regla = self.inducir_regla(ejemplo_positivo, ejemplos_negativos)
            self.reglas.append(regla)

    def inducir_regla(self, ejemplo_positivo, ejemplos_negativos):
        atributos = list(ejemplo_positivo.keys())[:-1]
        regla = []

        for atributo in atributos:
            valor = ejemplo_positivo[atributo]
            if self.es_consistente(valor, ejemplos_negativos):
                regla.append((atributo, valor))

        return regla

    def es_consistente(self, valor, ejemplos_negativos):
        for ejemplo_negativo in ejemplos_negativos:
            if valor == ejemplo_negativo[atributo]:
                return False
        return True

# Ejemplo de datos de entrenamiento
ejemplos_positivos = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'False', 'Play': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'False', 'Play': 'No'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'Yes'}
]

ejemplos_negativos = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'True', 'Play': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'False', 'Play': 'No'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'True', 'Play': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'False', 'Play': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'No'}
]

# Crear instancia de FOIL
foil = FOIL()

# Generar las reglas
foil.generar_reglas(ejemplos_positivos, ejemplos_negativos)

# Imprimir las reglas generadas
for regla in foil.reglas:
    print(regla)

