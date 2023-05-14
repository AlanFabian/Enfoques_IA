#Alan de Jesus Fabian Garcia 
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating


class KnowledgeBase:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movies_by_genre(self, genre):
        return [movie for movie in self.movies if movie.genre == genre]

    def get_top_rated_movies(self, n):
        sorted_movies = sorted(self.movies, key=lambda movie: movie.rating, reverse=True)
        return sorted_movies[:n]


# Ejemplo de uso

# Crear una base de conocimiento de películas
knowledge_base = KnowledgeBase()

# Agregar películas a la base de conocimiento
knowledge_base.add_movie(Movie("The Shawshank Redemption", "Drama", 9.3))
knowledge_base.add_movie(Movie("The Godfather", "Drama", 9.2))
knowledge_base.add_movie(Movie("Pulp Fiction", "Crime", 8.9))
knowledge_base.add_movie(Movie("The Dark Knight", "Action", 9.0))
knowledge_base.add_movie(Movie("Fight Club", "Drama", 8.8))

# Obtener las películas del género "Drama"
drama_movies = knowledge_base.get_movies_by_genre("Drama")
print("Películas de drama:")
for movie in drama_movies:
    print(movie.title)

# Obtener las 3 películas mejor valoradas
top_rated_movies = knowledge_base.get_top_rated_movies(3)
print("Las 3 películas mejor valoradas:")
for movie in top_rated_movies:
    print(movie.title, "- Rating:", movie.rating)
