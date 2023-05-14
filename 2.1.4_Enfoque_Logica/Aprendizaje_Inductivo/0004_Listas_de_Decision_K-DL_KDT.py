#Alan de Jesus Fabian Garcia 
class Decision:
    def __init__(self, condicion, decision):
        self.condicion = condicion
        self.decision = decision


def construir_lista_decision(datos_entrenamiento, atributos, clase_objetivo):
    lista_decision = []

    for atributo in atributos:
        decision = datos_entrenamiento[atributo].mode()[0]
        lista_decision.append(Decision(atributo, decision))

    lista_decision.append(Decision(None, datos_entrenamiento[clase_objetivo].mode()[0]))

    return lista_decision


def tomar_decision(instancia, lista_decision):
    for decision in lista_decision:
        if decision.condicion is None or instancia[decision.condicion] == decision.decision:
            return decision.decision

    return None


# Ejemplo de datos de entrenamiento
datos_entrenamiento = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'False', 'Play': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'True', 'Play': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'No'},
    {'Outlook': 'Overcast', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'False', 'Play': 'No'},
    {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'Yes'},
    {'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'True', 'Play': 'Yes'},
    {'Outlook': 'Overcast', 'Temperature': 'Hot', 'Humidity': 'Normal', 'Windy': 'False', 'Play': 'Yes'},
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'True', 'Play': 'No'}
]


