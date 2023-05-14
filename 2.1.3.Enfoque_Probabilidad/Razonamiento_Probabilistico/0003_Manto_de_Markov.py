#Alan de Jesus Fabian Garcia 
import random

def generar_transiciones(texto):
    """
    Genera las transiciones de palabras a partir de un texto dado.
    """
    palabras = texto.split()
    transiciones = {}
    
    for i in range(len(palabras)-1):
        palabra_actual = palabras[i]
        palabra_siguiente = palabras[i+1]
        
        if palabra_actual not in transiciones:
            transiciones[palabra_actual] = []
        
        transiciones[palabra_actual].append(palabra_siguiente)
    
    return transiciones

def generar_texto(transiciones, longitud):
    """
    Genera texto a partir de las transiciones y una longitud dada.
    """
    texto_generado = ""
    palabra_actual = random.choice(list(transiciones.keys()))
    
    for _ in range(longitud):
        texto_generado += palabra_actual + " "
        
        if palabra_actual not in transiciones:
            break
        
        palabra_siguiente = random.choice(transiciones[palabra_actual])
        palabra_actual = palabra_siguiente
    
    return texto_generado

# Ejemplo de uso
texto_ejemplo = "Hola, ¿cómo estás? Me llamo Markov y soy un modelo de lenguaje basado en cadenas de Markov."
transiciones_ejemplo = generar_transiciones(texto_ejemplo)
texto_generado_ejemplo = generar_texto(transiciones_ejemplo, 10)

print("Transiciones:")
print(transiciones_ejemplo)
print("\nTexto generado:")
print(texto_generado_ejemplo)
