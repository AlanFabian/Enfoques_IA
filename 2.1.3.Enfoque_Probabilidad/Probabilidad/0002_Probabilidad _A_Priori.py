#Alan de Jesus Fabian Garcia 
def calcular_probabilidad_a_priori(evento, conjunto_eventos):
    # Contar el número total de eventos en el conjunto
    total_eventos = len(conjunto_eventos)
    
    # Contar el número de ocurrencias del evento específico en el conjunto
    ocurrencias_evento = conjunto_eventos.count(evento)
    
    # Calcular la probabilidad a priori dividiendo las ocurrencias del evento entre el total de eventos
    probabilidad = ocurrencias_evento / total_eventos
    
    # Devolver la probabilidad calculada
    return probabilidad

# Ejemplo de uso
eventos = ['A', 'B', 'C', 'A', 'B', 'A', 'D']
evento_deseado = 'A'

# Calcular la probabilidad a priori del evento deseado utilizando la función
probabilidad = calcular_probabilidad_a_priori(evento_deseado, eventos)

# Imprimir la probabilidad a priori del evento deseado
print(f'La probabilidad a priori del evento "{evento_deseado}" es: {probabilidad}')
