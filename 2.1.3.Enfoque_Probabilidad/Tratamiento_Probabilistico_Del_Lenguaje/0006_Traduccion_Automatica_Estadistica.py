#Alan de Jesus Fabian Garcia 
import nltk
from nltk.translate import IBMModel1
from nltk.translate.ibm_model import Alignment

# Corpus paralelo (pares de frases en dos idiomas)
corpus = [
    (("I", "am", "happy"), ("Ich", "bin", "glücklich")),
    (("He", "is", "sad"), ("Er", "ist", "traurig")),
    (("They", "are", "sleeping"), ("Sie", "schlafen")),
]

# Preprocesamiento del corpus
source_sentences = [src for src, _ in corpus]
target_sentences = [tgt for _, tgt in corpus]

# Entrenamiento del modelo IBM Model 1
ibm1 = IBMModel1(source_sentences, target_sentences, iterations=10)

# Frase de origen a traducir
source_sentence = ["I", "am", "happy"]

# Traducción utilizando el modelo entrenado
translation = ibm1.best_translation(source_sentence)

print("Frase de origen:", " ".join(source_sentence))
print("Traducción:", " ".join(translation))
