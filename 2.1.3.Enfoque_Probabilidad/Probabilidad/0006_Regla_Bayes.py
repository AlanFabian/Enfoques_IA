#Alan de Jesus Fabian Garcia 
def calcular_probabilidad_condicional_inversa(evento_a, evento_b, conjunto_eventos):
    # Contar el número de ocurrencias de evento A en el conjunto
    ocurrencias_evento_a = conjunto_eventos.count(evento_a)
    
    # Contar el número de ocurrencias de evento A y B juntos en el conjunto
    ocurrencias_evento_a_b = 0
    for i in range(len(conjunto_eventos)-1):
        if conjunto_eventos[i] == evento_a and conjunto_eventos[i+1] == evento_b:
            ocurrencias_evento_a_b += 1
    
    # Calcular la probabilidad condicional de B dado A
    probabilidad_condicional_a_b = ocurrencias_evento_a_b / ocurrencias_evento_a
    
    # Calcular la probabilidad de evento A
    probabilidad_evento_a = ocurrencias_evento_a / len(conjunto_eventos)
    
    # Calcular la probabilidad de evento B
    probabilidad_evento_b = conjunto_eventos.count(evento_b) / len(conjunto_eventos)
    
    # Aplicar la regla de Bayes para calcular la probabilidad condicional inversa
    probabilidad_condicional_inversa = (probabilidad_condicional_a_b * probabilidad_evento_b) / probabilidad_evento_a
    
    # Devolver la probabilidad condicional inversa calculada
    return probabilidad_condicional_inversa

# Ejemplo de uso
eventos = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'D']
evento_a = 'A'
evento_b = 'B'

# Calcular la probabilidad condicional inversa de A dado B utilizando la función
probabilidad_condicional_inversa = calcular_probabilidad_condicional_inversa(evento_a, evento_b, eventos)

# Imprimir la probabilidad condicional inversa
print(f'La probabilidad condicional inversa de {evento_a} dado {evento_b} es: {probabilidad_condicional_inversa}')
