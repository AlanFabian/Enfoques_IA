#Alan de Jeus Fabian Garcia 
from sklearn.datasets import make_circles
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo con estructura circular
X, y = make_circles(n_samples=100, noise=0.1, factor=0.5, random_state=0)

# Crear un objeto SVM con un núcleo no lineal (RBF)
svm = SVC(kernel='rbf', C=1.0, gamma='scale')

# Ajustar el modelo a los datos
svm.fit(X, y)

# Crear una malla de puntos para visualizar la superficie de decisión
xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 100), np.linspace(-1.5, 1.5, 100))
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Graficar los puntos de datos y la superficie de decisión
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.Blues_r, alpha=0.5)
plt.contour(xx, yy, Z, levels=[0], colors='red')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Máquinas de Vectores Soporte (Núcleo)')
plt.show()
