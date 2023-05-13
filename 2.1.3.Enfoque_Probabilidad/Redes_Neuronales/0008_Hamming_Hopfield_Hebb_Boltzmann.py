#Hamming
def hamming_similarity(pattern1, pattern2):
    if len(pattern1) != len(pattern2):
        raise ValueError("Los patrones deben tener la misma longitud")

    distance = 0
    for bit1, bit2 in zip(pattern1, pattern2):
        if bit1 != bit2:
            distance += 1

    similarity = 1 - (distance / len(pattern1))
    return similarity
  
  #Hopfield
import numpy as np

class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        for pattern in patterns:
            pattern = np.array(pattern)
            outer_product = np.outer(pattern, pattern)
            np.fill_diagonal(outer_product, 0)
            self.weights += outer_product

    def recall(self, input_pattern, max_iterations=100):
        input_pattern = np.array(input_pattern)
        for _ in range(max_iterations):
            output_pattern = np.sign(np.dot(self.weights, input_pattern))
            if np.array_equal(input_pattern, output_pattern):
                return output_pattern
            input_pattern = output_pattern

        raise ValueError("La red no pudo converger hacia un patrón estable")

class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        for pattern in patterns:
            pattern = np.array(pattern)
            outer_product = np.outer(pattern, pattern)
            np.fill_diagonal(outer_product, 0)
            self.weights += outer_product

    def recall(self, input_pattern, max_iterations=100):
        input_pattern = np.array(input_pattern)
        for _ in range(max_iterations):
          
          
     #Hebbian     
       import numpy as np

class HebbianNetwork:
    def __init__(self, input_dim, output_dim):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.weights = np.zeros((output_dim, input_dim))

    def train(self, inputs):
        for input_data in inputs:
            input_data = np.array(input_data)
            self.weights += np.outer(input_data, input_data)

    def recall(self, input_data):
        input_data = np.array(input_data)
        output_data = np.dot(self.weights, input_data)
        return np.sign(output_data)

            output_pattern = np.sign(np.dot(self.weights, input_pattern))
            if np.array_equal(input_pattern, output_pattern):
                return output_pattern
            input_pattern = output_pattern

        raise ValueError("La red no pudo converger hacia un patrón estable")
        
#Boltzmann
 import numpy as np

class BoltzmannMachine:
    def __init__(self, num_visible, num_hidden):
        self.num_visible = num_visible
        self.num_hidden = num_hidden
        self.weights = np.random.randn(num_visible, num_hidden)
        self.hidden_bias = np.zeros(num_hidden)
        self.visible_bias = np.zeros(num_visible)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def train(self, data, learning_rate=0.1, epochs=100):
        num_samples = data.shape[0]
        for _ in range(epochs):
            for sample in data:
                hidden_activations = np.dot(sample, self.weights) + self.hidden_bias
                hidden_probs = self.sigmoid(hidden_activations)
                hidden_states = np.random.binomial(1, hidden_probs)
                visible_activations = np.dot(hidden_states, self.weights.T) + self.visible_bias
                visible_probs = self.sigmoid(visible_activations)
                visible_states = np.random.binomial(1, visible_probs)

                positive_gradient = np.outer(sample, hidden_probs)
                negative_gradient = np.outer(visible_states, hidden_states)
                self.weights += learning_rate * (positive_gradient - negative_gradient)
                self.visible_bias += learning_rate * (sample - visible_states)
                self.hidden_bias += learning_rate * (hidden_probs - hidden_states)

    def generate_sample(self, num_samples):
        hidden_states = np.random.binomial(1, 0.5,


