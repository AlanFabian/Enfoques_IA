#Alan de Jesus Fabian Garcia 
import math
from collections import Counter

def calcular_entropia(datos):
    etiquetas = [dato[-1] for dato in datos]
    contador_etiquetas = Counter(etiquetas)
    entropia = 0

    for etiqueta in contador_etiquetas:
        probabilidad = contador_etiquetas[etiqueta] / len(etiquetas)
        entropia -= probabilidad * math.log2(probabilidad)

    return entropia

def calcular_ganancia(datos, atributo):
    entropia_inicial = calcular_entropia(datos)
    valores_atributo = set([dato[atributo] for dato in datos])
    ganancia = entropia_inicial

    for valor in valores_atributo:
        datos_subconjunto = [dato for dato in datos if dato[atributo] == valor]
        probabilidad_subconjunto = len(datos_subconjunto) / len(datos)
        ganancia -= probabilidad_subconjunto * calcular_entropia(datos_subconjunto)

    return ganancia

def obtener_atributo_seleccionado(datos, atributos):
    ganancias = []

    for atributo in atributos:
        ganancia = calcular_ganancia(datos, atributo)
        ganancias.append((atributo, ganancia))

    atributo_seleccionado = max(ganancias, key=lambda x: x[1])[0]
    return atributo_seleccionado

def construir_arbol_id3(datos, atributos):
    etiquetas = [dato[-1] for dato in datos]

    # Caso base: todos los datos tienen la misma etiqueta
    if len(set(etiquetas)) == 1:
        return etiquetas[0]

    # Caso base: no hay más atributos para dividir
    if len(atributos) == 0:
        contador_etiquetas = Counter(etiquetas)
        etiqueta_mayor_frecuencia = max(contador_etiquetas, key=lambda x: contador_etiquetas[x])
        return etiqueta_mayor_frecuencia

    atributo_seleccionado = obtener_atributo_seleccionado(datos, atributos)
    arbol = {atributo_seleccionado: {}}

    valores_atributo = set([dato[atributo_seleccionado] for dato in datos])

    for valor in valores_atributo:
        datos_subconjunto = [dato for dato in datos if dato[atributo_seleccionado] == valor]
        nuevos_atributos = atributos.copy()
        nuevos_atributos.remove(atributo_seleccionado)
        arbol[atributo_seleccionado][valor] = construir_arbol_id3(datos_subconjunto, nuevos_atributos)

    return arbol

# Ejemplo de datos de entrenamiento
datos_entrenamiento = [
    ['Soleado', 'Caliente', 'Alta', 'Débil', 'No'],
    ['Soleado', 'Caliente', 'Alta', 'Fuerte', 'No'],
    ['Nublado', 'Caliente', 'Alta', 'Débil', 'Sí'],
    ['Lluvioso', 'Templado', 'Alta', 'Débil', 'Sí'],
    ['Lluvioso', 'Frío', 'Normal', 'Débil', 'Sí'],
    ['Lluvioso', 'Frío', 'Normal', 'Fuerte', 'No'],
    ['Nublado', 'Frío', 'Normal', 'Fuerte', 'Sí']
]

# Aquí puedes llamar a la función para construir el árbol de decisión
arbol_decision = construir_arbol_id3(datos_entrenamiento, atributos)
print(arbol_decision)
