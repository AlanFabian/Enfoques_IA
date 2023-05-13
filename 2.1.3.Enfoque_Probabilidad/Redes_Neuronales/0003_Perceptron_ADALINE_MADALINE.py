
#Alan de Jesus Fabian Garcia 
import numpy as np

class Adaline:
    def __init__(self, learning_rate=0.01, epochs=50):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Inicializar los pesos y el sesgo con valores aleatorios pequeños
        self.weights = np.random.randn(X.shape[1])
        self.bias = np.random.randn()

        for _ in range(self.epochs):
            # Calcular la salida del modelo
            y_pred = self.predict(X)

            # Actualizar los pesos y el sesgo mediante el descenso del gradiente
            self.weights += self.learning_rate * np.dot(X.T, (y - y_pred))
            self.bias += self.learning_rate * np.sum(y - y_pred)

    def predict(self, X):
        # Calcular la salida del modelo
        z = np.dot(X, self.weights) + self.bias
        y_pred = np.where(z >= 0, 1, -1)
        return y_pred
    
    
###########################################################
import numpy as np

class Madaline:
    def __init__(self, learning_rate=0.01, epochs=50):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Inicializar los pesos y el sesgo con valores aleatorios pequeños
        self.weights = np.random.randn(X.shape[1])
        self.bias = np.random.randn()

        for _ in range(self.epochs):
            # Calcular la salida del modelo
            y_pred = self.predict(X)

            # Actualizar los pesos y el sesgo mediante el descenso del gradiente
            self.weights += self.learning_rate * np.dot(X.T, (y - y_pred))
            self.bias += self.learning_rate * np.sum(y - y_pred)

    def predict(self, X):
        # Calcular la salida del modelo
        z = np.dot(X, self.weights) + self.bias
        y_pred = np.where(z >= 0, 1, 0)
        return y_pred
