#Alan de Jesus Fabian Garcia 
import nltk

# Definición de la gramática causal definida
grammar = nltk.CFG.fromstring("""
    S -> NP VP | NP VP Causal
    NP -> Det Noun
    VP -> Verb NP | Verb
    Det -> 'the' | 'a'
    Noun -> 'dog' | 'cat' | 'ball'
    Verb -> 'chased' | 'ate' | 'played'
    Causal -> 'because' S
""")

# Creación de un analizador sintáctico basado en la gramática
parser = nltk.ChartParser(grammar)

# Oración de ejemplo para analizar
sentence = 'the dog chased the cat because the cat ate the ball'

# Análisis sintáctico de la oración
for tree in parser.parse(sentence.split()):
    tree.pretty_print()
