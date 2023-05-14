#Alan de Jesus Fabian Garcia 
import re

# Definir las expresiones regulares para cada token
patrones = [
    (r'[a-zA-Z][a-zA-Z0-9_]*', 'IDENTIFICADOR'),  # Identificadores
    (r'\d+', 'ENTERO'),  # Enteros
    (r'\+', 'SUMA'),  # Operador suma
    (r'-', 'RESTA'),  # Operador resta
    (r'\*', 'MULTIPLICACION'),  # Operador multiplicación
    (r'/', 'DIVISION'),  # Operador división
    (r'\(', 'PARENTESIS_IZQ'),  # Paréntesis izquierdo
    (r'\)', 'PARENTESIS_DER'),  # Paréntesis derecho
    (r'\s+', None),  # Espacios en blanco (ignorados)
]

# Función para realizar el análisis léxico
def analisis_lexico(codigo):
    tokens = []
    while codigo:
        encontrado = False
        for patron, etiqueta in patrones:
            coincidencia = re.match(patron, codigo)
            if coincidencia:
                valor = coincidencia.group(0)
                if etiqueta:
                    token = (valor, etiqueta)
                    tokens.append(token)
                codigo = codigo[len(valor):]
                encontrado = True
                break
        if not encontrado:
            print("Error: Token inválido en el código:", codigo[0])
            return []
    return tokens

# Ejemplo de código a analizar
codigo = "x = 5 + 3 * (a - b)"

# Realizar el análisis léxico
tokens = analisis_lexico(codigo)

# Imprimir los tokens encontrados
for token in tokens:
    print(token)
