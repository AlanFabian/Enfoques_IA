#Alan de Jesus Fabian Garcia 
from minisom import MiniSom
import numpy as np

class KohonenMap:
    def __init__(self, input_dim, output_shape):
        self.input_dim = input_dim
        self.output_shape = output_shape
        self.map = self.build_map()

    def build_map(self):
        map = MiniSom(self.output_shape[0], self.output_shape[1], self.input_dim, sigma=1.0, learning_rate=0.5)
        return map

    def fit(self, X, epochs=100):
        self.map.random_weights_init(X)
        self.map.train_random(X, epochs)

    def predict(self, X):
        predictions = self.map.predict(X)
        return predictions
