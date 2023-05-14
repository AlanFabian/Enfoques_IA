#Alan de Jesus Fabian Garcia 
def calcular_distribucion_probabilidad(conjunto_eventos):
    # Contar el número total de eventos en el conjunto
    total_eventos = len(conjunto_eventos)
    
    # Crear un diccionario para contar las ocurrencias de cada evento
    conteo_eventos = {}
    for evento in conjunto_eventos:
        if evento in conteo_eventos:
            conteo_eventos[evento] += 1
        else:
            conteo_eventos[evento] = 1
    
    # Calcular la probabilidad de cada evento
    distribucion_probabilidad = {}
    for evento, ocurrencias in conteo_eventos.items():
        probabilidad = ocurrencias / total_eventos
        distribucion_probabilidad[evento] = probabilidad
    
    # Devolver la distribución de probabilidad calculada
    return distribucion_probabilidad

# Ejemplo de uso
eventos = ['A', 'B', 'C', 'A', 'B', 'A', 'D']

# Calcular la distribución de probabilidad del conjunto de eventos utilizando la función
distribucion_probabilidad = calcular_distribucion_probabilidad(eventos)

# Imprimir la distribución de probabilidad
print("Distribución de probabilidad:")
for evento, probabilidad in distribucion_probabilidad.items():
    print(f'Evento: {evento}, Probabilidad: {probabilidad}')
