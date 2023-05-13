#Alan de Jesus Fabian Garcia 
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x)**2

# Ejemplo de uso
x = np.array([-1, 0, 1])
print(sigmoid(x))             # Salida: [0.26894142, 0.5, 0.73105858]
print(sigmoid_derivative(x))  # Salida: [0.19661193, 0.25, 0.19661193]
print(relu(x))                # Salida: [0, 0, 1]
print(relu_derivative(x))     # Salida: [0, 0, 1]
print(tanh(x))                # Salida: [-0.76159416, 0., 0.76159416]
print(tanh_derivative(x))     # Salida: [0.41997434, 1., 0.41997434]
