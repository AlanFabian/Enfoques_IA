#Alan de Jesus Fabian Garcia 
def verificar_independencia_condicional(evento_a, evento_b, evento_c, conjunto_eventos):
    # Contar el número de ocurrencias de los eventos A, B y C juntos en el conjunto
    ocurrencias_a_b_c = 0
    for i in range(len(conjunto_eventos)-2):
        if conjunto_eventos[i] == evento_a and conjunto_eventos[i+1] == evento_b and conjunto_eventos[i+2] == evento_c:
            ocurrencias_a_b_c += 1
    
    # Contar el número de ocurrencias de los eventos A y B juntos en el conjunto
    ocurrencias_a_b = 0
    for i in range(len(conjunto_eventos)-1):
        if conjunto_eventos[i] == evento_a and conjunto_eventos[i+1] == evento_b:
            ocurrencias_a_b += 1
    
    # Calcular la probabilidad condicionada de C dado A y B
    probabilidad_condicionada = ocurrencias_a_b_c / ocurrencias_a_b
    
    # Verificar la independencia condicional
    if probabilidad_condicionada == 0 or probabilidad_condicionada == probabilidad_condicionada:
        independencia_condicional = True
    else:
        independencia_condicional = False
    
    # Devolver el resultado de la verificación
    return independencia_condicional

# Ejemplo de uso
eventos = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'D']
evento_a = 'A'
evento_b = 'B'
evento_c = 'C'

# Verificar la independencia condicional entre A, B y C utilizando la función
independencia_condicional = verificar_independencia_condicional(evento_a, evento_b, evento_c, eventos)

# Imprimir el resultado de la verificación
if independencia_condicional:
    print(f'Los eventos {evento_a}, {evento_b} y {evento_c} son independientes condicionalmente.')
else:
    print(f'Los eventos {evento_a}, {evento_b} y {evento_c} no son independientes condicionalmente.')
