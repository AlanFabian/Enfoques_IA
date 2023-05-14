#Alan de Jesus Fabian Garcia 
def calcular_probabilidad_condicionada(evento_a, evento_b, conjunto_eventos):
    # Contar el número de ocurrencias de evento A en el conjunto
    ocurrencias_evento_a = conjunto_eventos.count(evento_a)
    
    # Contar el número de ocurrencias de evento A y B juntos en el conjunto
    ocurrencias_evento_a_b = 0
    for i in range(len(conjunto_eventos)-1):
        if conjunto_eventos[i] == evento_a and conjunto_eventos[i+1] == evento_b:
            ocurrencias_evento_a_b += 1
    
    # Calcular la probabilidad condicionada de evento A dado evento B
    probabilidad_condicionada = ocurrencias_evento_a_b / ocurrencias_evento_a
    
    # Devolver la probabilidad condicionada calculada
    return probabilidad_condicionada


def normalizar_probabilidades(probabilidades):
    # Calcular la suma de todas las probabilidades
    suma_probabilidades = sum(probabilidades)
    
    # Normalizar las probabilidades dividiéndolas por la suma
    probabilidades_normalizadas = [p / suma_probabilidades for p in probabilidades]
    
    # Devolver las probabilidades normalizadas
    return probabilidades_normalizadas

# Ejemplo de uso
eventos = ['A', 'B', 'A', 'B', 'C', 'A', 'B', 'A', 'D']
evento_a = 'A'
evento_b = 'B'

# Calcular la probabilidad condicionada de A dado B utilizando la función
probabilidad_condicionada = calcular_probabilidad_condicionada(evento_a, evento_b, eventos)

# Imprimir la probabilidad condicionada
print(f'La probabilidad condicionada de {evento_a} dado {evento_b} es: {probabilidad_condicionada}')

# Calcular las probabilidades normalizadas de cada evento en el conjunto
probabilidades = [eventos.count(evento) for evento in set(eventos)]
probabilidades_normalizadas = normalizar_probabilidades(probabilidades)

# Imprimir las probabilidades normalizadas
print(f'Las probabilidades normalizadas son: {probabilidades_normalizadas}')
