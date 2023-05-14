#Alan de Jesus fabian Garcia 
def generar_espacio_versiones(datos_entrenamiento):
    espacio_versiones = []
    atributos = list(datos_entrenamiento[0].keys())[:-1]

    for instancia in datos_entrenamiento:
        x = instancia.copy()
        if x['Play'] == 'Yes':
            h = ['+', '+', '+', '+', '+']
            for i, atributo in enumerate(atributos):
                if h[i] == '+':
                    if x[atributo] != h[i]:
                        h[i] = '?'
            espacio_versiones.append(h)
        else:
            h = ['-', '-', '-', '-', '-']
            for i, atributo in enumerate(atributos):
                if h[i] == '-':
                    if x[atributo] != h[i]:
                        h[i] = '?'
            espacio_versiones.append(h)

    return espacio_versiones

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
    {'Outlook': 'Rain', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'Yes'},
    {'Outlook': 'Sunny', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'True', 'Play': 'Yes'}
]

espacio_versiones = generar_espacio_versiones(datos_entrenamiento)

# Imprimir el espacio de versiones
for h in espacio_versiones:
    print(h)
