#Alan de Jesus Fabian Garcia 
# Gramática de ejemplo para expresiones aritméticas
# E -> T E'
# E' -> + T E' | ε
# T -> F T'
# T' -> * F T' | ε
# F -> ( E ) | ID

# Función para realizar el análisis sintáctico
def analisis_sintactico(tokens):
    # Inicializar el índice de tokens
    indice = 0

    # Función para analizar la no-terminal E
    def E():
        nonlocal indice
        T()
        E_()

    # Función para analizar la no-terminal E'
    def E_():
        nonlocal indice
        if indice < len(tokens) and tokens[indice] == '+':
            indice += 1
            T()
            E_()

    # Función para analizar la no-terminal T
    def T():
        nonlocal indice
        F()
        T_()

    # Función para analizar la no-terminal T'
    def T_():
        nonlocal indice
        if indice < len(tokens) and tokens[indice] == '*':
            indice += 1
            F()
            T_()

    # Función para analizar la no-terminal F
    def F():
        nonlocal indice
        if indice < len(tokens) and tokens[indice] == '(':
            indice += 1
            E()
            if indice < len(tokens) and tokens[indice] == ')':
                indice += 1
            else:
                raise SyntaxError("Error de sintaxis: Se esperaba ')' después de '('")
        elif indice < len(tokens) and tokens[indice] == 'ID':
            indice += 1
        else:
            raise SyntaxError("Error de sintaxis: Se esperaba '(' o 'ID'")

    # Llamar a la función inicial
    E()

    # Verificar si se ha analizado todos los tokens
    if indice < len(tokens):
        raise SyntaxError("Error de sintaxis: Tokens no esperados")

    print("Análisis sintáctico exitoso")

# Ejemplo de tokens a analizar
tokens = ['ID', '+', 'ID', '*', 'ID']

# Realizar el análisis sintáctico
try:
    analisis_sintactico(tokens)
except SyntaxError as e:
    print(e)
