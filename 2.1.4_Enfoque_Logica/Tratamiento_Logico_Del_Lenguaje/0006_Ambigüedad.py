#Alan de Jesus Fabian Garcia 
import nltk

# Definición de la gramática ambigua
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det Adj N
    VP -> V NP
    Det -> 'the' | 'a'
    Adj -> 'big' | 'small'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Creación de un analizador sintáctico basado en la gramática
parser = nltk.ChartParser(grammar)

# Oración ambigua de ejemplo
sentence = 'the big dog chased the small cat'

# Análisis sintáctico de la oración
for tree in parser.parse(sentence.split()):
    tree.pretty_print()
