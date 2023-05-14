#Alan de Jesus Fabian Garcia 
# Ejemplo de gramática para expresiones aritméticas
# E -> E + T | T
# T -> T * F | F
# F -> ( E ) | NUM

# Función para realizar el análisis semántico
def analisis_semantico(arbol):
    if arbol['tipo'] == 'expresion':
        tipo_izquierda = analisis_semantico(arbol['izquierda'])
        tipo_derecha = analisis_semantico(arbol['derecha'])
        if tipo_izquierda != 'num' or tipo_derecha != 'num':
            raise Exception('Error semántico: Se esperaban operandos numéricos')
        return 'num'
    elif arbol['tipo'] == 'termino':
        tipo_izquierda = analisis_semantico(arbol['izquierda'])
        tipo_derecha = analisis_semantico(arbol['derecha'])
        if tipo_izquierda != 'num' or tipo_derecha != 'num':
            raise Exception('Error semántico: Se esperaban operandos numéricos')
        return 'num'
    elif arbol['tipo'] == 'factor':
        if arbol['valor'].isdigit():
            return 'num'
        else:
            raise Exception('Error semántico: Se esperaba un número')
    else:
        raise Exception('Error semántico: Tipo de nodo desconocido')

# Ejemplo de árbol de análisis sintáctico
arbol = {
    'tipo': 'expresion',
    'izquierda': {
        'tipo': 'termino',
        'izquierda': {
            'tipo': 'factor',
            'valor': '5'
        },
        'derecha': {
            'tipo': 'factor',
            'valor': '3'
        }
    },
    'derecha': {
        'tipo': 'factor',
        'valor': '2'
    }
}

# Realizar el análisis semántico
try:
    tipo_resultado = analisis_semantico(arbol)
    print('El tipo de resultado es:', tipo_resultado)
except Exception as e:
    print(e)
