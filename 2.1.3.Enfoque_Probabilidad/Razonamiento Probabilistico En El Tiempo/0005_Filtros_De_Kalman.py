#Alan de Jesus Fabian Garcia 
import numpy as np

# Parámetros del modelo del sistema
A = np.array([[1, 1], [0, 1]])  # Matriz de transición
B = np.array([[0.5], [1]])  # Matriz de control
H = np.array([[1, 0]])  # Matriz de observación
Q = np.array([[0.1, 0], [0, 0.1]])  # Covarianza del proceso
R = np.array([[1]])  # Covarianza de la medida

# Función para realizar la actualización del filtro de Kalman
def actualizar_filtro_kalman(x_prev, P_prev, u, z):
    # Predicción
    x_pred = A.dot(x_prev) + B.dot(u)
    P_pred = A.dot(P_prev).dot(A.T) + Q

    # Actualización
    y = z - H.dot(x_pred)
    S = H.dot(P_pred).dot(H.T) + R
    K = P_pred.dot(H.T).dot(np.linalg.inv(S))
    x_est = x_pred + K.dot(y)
    P_est = (np.eye(2) - K.dot(H)).dot(P_pred)

    return x_est, P_est

# Ejemplo de uso del filtro de Kalman
mediciones = [1.2, 1.8, 3.5, 4.2]  # Mediciones ruidosas

# Estado inicial y covarianza inicial
x_initial = np.array([[0], [0]])
P_initial = np.eye(2)

x_current = x_initial
P_current = P_initial

# Actualización del filtro de Kalman para cada medición
for z in mediciones:
    x_current, P_current = actualizar_filtro_kalman(x_current, P_current, np.array([[1]]), z)
    print("Estado estimado:", x_current.flatten())
