#Alan de Jesus Fabian Garcia 
import nltk
from nltk import ngrams
from collections import defaultdict

# Obtener el corpus
corpus = ["Este es un ejemplo de texto", "Otro ejemplo de texto"]

# Preprocesar el corpus
tokenized_corpus = [nltk.word_tokenize(sentence.lower()) for sentence in corpus]

# Construir el modelo de trigramas
model = defaultdict(lambda: defaultdict(lambda: 0))
for sentence in tokenized_corpus:
    trigrams = list(ngrams(sentence, 3, pad_left=True, pad_right=True))
    for w1, w2, w3 in trigrams:
        model[(w1, w2)][w3] += 1

# Estimar probabilidades
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count

# Ejemplo de generación de texto
seed = ("este", "es")
for _ in range(5):
    print(seed[0], seed[1])
    next_word = max(model[seed[0], seed[1]], key=model[seed[0], seed[1]].get)
    seed = (seed[1], next_word)
