#Alan de Jesus Fabian Garcia 
# Reglas
relationships = {
    'juan': ['pepe', 'maria'],
    'pepe': ['ana', 'luis']
}

# Consulta
def abuelo(x, y):
    for child in relationships.get(x, []):
        if y in relationships.get(child, []):
            return True
    return False

# Ejemplo de consulta
print(abuelo('juan', 'ana'))
