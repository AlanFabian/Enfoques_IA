#Alan de Jesus Fabian Garcia 
import tensorflow as tf
import numpy as np

class MultilayerPerceptron:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(self.hidden_dim, activation='sigmoid', input_shape=(self.input_dim,)),
            tf.keras.layers.Dense(self.output_dim, activation='sigmoid')
        ])

        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
        return model

    def fit(self, X, y, epochs=100, batch_size=32):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def predict(self, X):
        predictions = self.model.predict(X)
        return np.round(predictions)
