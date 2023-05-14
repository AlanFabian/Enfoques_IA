#Alan de Jesus Fabian Garcia 
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Corpus de documentos
corpus = [
    "El perro ladra.",
    "El gato maulla.",
    "El perro y el gato se llevan bien."
]

# Preprocesamiento del corpus
tokenized_corpus = [nltk.word_tokenize(sentence.lower()) for sentence in corpus]

# Construir la matriz TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([" ".join(tokens) for tokens in tokenized_corpus])

# Consulta del usuario
query = "perro"

# Preprocesamiento de la consulta
query_tokens = nltk.word_tokenize(query.lower())

# Construir el vector TF-IDF de la consulta
query_vector = tfidf_vectorizer.transform([" ".join(query_tokens)])

# Calcular la similitud coseno entre la consulta y los documentos
cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

# Obtener el índice del documento más relevante
most_similar_doc_index = cosine_similarities.argmax()

# Obtener el documento más relevante
most_similar_doc = corpus[most_similar_doc_index]

print("Consulta:", query)
print("Documento más relevante:", most_similar_doc)
