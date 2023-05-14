#Alan de Jesus Fabian Garcia 
from collections import Counter

def calcular_probabilidad_clase(datos_entrenamiento, clase_objetivo, clase):
    total_instancias = len(datos_entrenamiento)
    conteo_clase = sum(1 for instancia in datos_entrenamiento if instancia[clase_objetivo] == clase)
    return conteo_clase / total_instancias

def calcular_probabilidad_atributo(datos_entrenamiento, atributo, valor, clase_objetivo, clase):
    total_instancias_clase = sum(1 for instancia in datos_entrenamiento if instancia[clase_objetivo] == clase)
    conteo_valor = sum(1 for instancia in datos_entrenamiento if instancia[atributo] == valor and instancia[clase_objetivo] == clase)
    return conteo_valor / total_instancias_clase

def clasificar_instancia(instancia, datos_entrenamiento, atributos, clase_objetivo):
    clases_posibles = list(set(instancia[clase_objetivo] for instancia in datos_entrenamiento))
    mejor_hipotesis = None
    mejor_probabilidad = -1

    for clase in clases_posibles:
        probabilidad_clase = calcular_probabilidad_clase(datos_entrenamiento, clase_objetivo, clase)
        probabilidad_total = probabilidad_clase

        for atributo in atributos:
            valor = instancia[atributo]
            probabilidad_atributo = calcular_probabilidad_atributo(datos_entrenamiento, atributo, valor, clase_objetivo, clase)
            probabilidad_total *= probabilidad_atributo

        if probabilidad_total > mejor_probabilidad:
            mejor_hipotesis = clase
            mejor_probabilidad = probabilidad_total

    return mejor_hipotesis

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
   
