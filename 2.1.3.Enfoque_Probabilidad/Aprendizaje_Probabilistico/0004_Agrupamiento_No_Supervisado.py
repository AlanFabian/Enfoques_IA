#Alan de Jesus Fabian Garcia 
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generar datos de ejemplo
X, _ = make_blobs(n_samples=200, centers=4, random_state=0)

# Crear un objeto KMeans
kmeans = KMeans(n_clusters=4)

# Ajustar el modelo a los datos
kmeans.fit(X)

# Obtener las etiquetas de los clusters asignados a cada muestra
labels = kmeans.labels_

# Obtener las coordenadas de los centroides de los clusters
centroids = kmeans.cluster_centers_

# Visualizar los clusters y los centroides
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', color='red', s=100)
plt.show()
