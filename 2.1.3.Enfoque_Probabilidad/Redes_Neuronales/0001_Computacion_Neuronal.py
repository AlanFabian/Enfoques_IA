
#Alan de Jesus Fabian Garcia 
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar los datos de entrenamiento y prueba
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesamiento de datos
x_train = x_train.reshape(60000, 784) / 255.0
x_test = x_test.reshape(10000, 784) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Crear el modelo de la red neuronal
model = Sequential()
model.add(Dense(128, activation='sigmoid', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=1)

# Evaluar el modelo
loss, accuracy = model.evaluate(x_test, y_test, verbose=1)
print(f"Loss: {loss}")
print(f"Accuracy: {accuracy}")
