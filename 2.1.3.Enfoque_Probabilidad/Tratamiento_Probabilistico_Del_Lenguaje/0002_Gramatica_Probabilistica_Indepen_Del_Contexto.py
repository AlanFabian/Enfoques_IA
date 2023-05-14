#Alan de Jesus Fabian Garcia 
import nltk
from nltk import PCFG
from nltk.corpus import treebank

# Obtener el corpus
corpus = treebank.parsed_sents()

# Construir el modelo de PCFG
productions = []
for tree in corpus:
    tree.collapse_unary(collapsePOS=True)  # Colapsar etiquetas de categorías gramaticales
    tree.chomsky_normal_form()  # Convertir el árbol a la forma normal de Chomsky
    productions += tree.productions()

pcfg = PCFG.from_productions(productions)

# Generar una oración aleatoria basada en el modelo de PCFG
sentence = pcfg.generate()

print(' '.join(sentence.leaves()))
