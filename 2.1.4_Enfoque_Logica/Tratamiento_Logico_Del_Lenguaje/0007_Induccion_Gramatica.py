#Alan de Jesus Fabian Garcia 
import nltk

# Conjunto de ejemplos de lenguaje
ejemplos = [
    ('I love cats', 'SVO'),
    ('The cat is sleeping', 'Det N V'),
    ('Dogs bark', 'N V'),
    ('Birds can fly', 'N MD V')
]

# Extracción de reglas gramaticales
gramatica = nltk.induce_pcfg(nltk.Nonterminal('S'), ejemplos)

# Imprimir las reglas gramaticales
for produccion in gramatica.productions():
    print(produccion)
