#Alan de Jesus Fabian Garcia 
import math

def calcular_incertidumbre(conjunto_eventos):
    # Contar el número total de eventos en el conjunto
    total_eventos = len(conjunto_eventos)
    
    # Crear un diccionario para contar las ocurrencias de cada evento
    conteo_eventos = {}
    for evento in conjunto_eventos:
        if evento in conteo_eventos:
            conteo_eventos[evento] += 1
        else:
            conteo_eventos[evento] = 1
    
    # Calcular la incertidumbre (entropía) del conjunto de eventos
    incertidumbre = 0
    for evento, ocurrencias in conteo_eventos.items():
        probabilidad = ocurrencias / total_eventos
        incertidumbre -= probabilidad * math.log2(probabilidad)
    
    # Devolver la incertidumbre calculada
    return incertidumbre

# Ejemplo de uso
eventos = ['A', 'B', 'C', 'A', 'B', 'A', 'D']

# Calcular la incertidumbre del conjunto de eventos utilizando la función
incertidumbre = calcular_incertidumbre(eventos)

# Imprimir la incertidumbre
print(f'La incertidumbre del conjunto de eventos es: {incertidumbre}')
