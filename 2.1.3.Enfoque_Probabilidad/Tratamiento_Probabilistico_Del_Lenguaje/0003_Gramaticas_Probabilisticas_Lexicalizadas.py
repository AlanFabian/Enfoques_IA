#Alan de Jesus Fabian Garcia 
import nltk
from nltk import treetransforms
from nltk.parse import pchart
from nltk.corpus import treebank

# Obtener el corpus
corpus = treebank.parsed_sents()

# Preprocesar el corpus
transformed_corpus = []
for tree in corpus:
    tree.collapse_unary(collapsePOS=True)  # Colapsar etiquetas de categorías gramaticales
    tree.chomsky_normal_form()  # Convertir el árbol a la forma normal de Chomsky
    transformed_corpus.append(tree)

# Construir el modelo de LFG
lfg = nltk.grammar.induced_lfg.InducedLexicalizedGrammar.from_trees(transformed_corpus)

# Crear un parser basado en el modelo de LFG
parser = pchart.InsideChartParser(lfg)

# Parsear una oración
sentence = "I saw the man with a telescope"
tokens = sentence.split()
parsed_trees = list(parser.parse(tokens))

# Imprimir el árbol parseado
for tree in parsed_trees:
    print(tree)
