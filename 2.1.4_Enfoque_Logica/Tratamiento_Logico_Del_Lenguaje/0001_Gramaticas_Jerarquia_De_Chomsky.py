#Alan de Jesus Fabian Garcia 
import nltk

# Tipo 3: Gramática Regular
gramatica_regular = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Tipo 2: Gramática Libre de Contexto
gramatica_libre_de_contexto = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Tipo 1: Gramática Sensible al Contexto
gramatica_sensible_al_contexto = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Tipo 0: Gramática Irrestricta
gramatica_irrestricta = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Ejemplo de frase a analizar
frase = "the dog chased the cat"

# Crear el analizador sintáctico
analizador = nltk.ChartParser(gramatica_libre_de_contexto)

# Analizar la frase
for arbol in analizador.parse(frase.split()):
    print(arbol)
