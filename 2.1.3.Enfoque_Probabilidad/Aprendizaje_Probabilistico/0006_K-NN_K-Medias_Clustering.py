#Alan de Jesus Fabian Garcia 
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# Generar datos de ejemplo
X, _ = make_blobs(n_samples=200, centers=4, random_state=0)

# Algoritmo k-NN
knn = NearestNeighbors(n_neighbors=2)
knn.fit(X)
distancias, indices = knn.kneighbors(X)

# Graficar el gráfico de codo para determinar el número óptimo de clusters en k-Means
distancias = np.sort(distancias, axis=0)
distancias = distancias[:, 1]
plt.plot(distancias)
plt.xlabel('Índice de muestra')
plt.ylabel('Distancia al k-ésimo vecino más cercano')
plt.show()

# Algoritmo k-Means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Algoritmo Clustering Espectral
clustering_espectral = SpectralClustering(n_clusters=4, assign_labels="discretize", random_state=0)
clustering_espectral.fit(X)

# Graficar los resultados
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# k-NN
axs[0].scatter(X[:, 0], X[:, 1], c=indices[:, 1])
axs[0].set_title('k-NN')

# k-Means
axs[1].scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
axs[1].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', color='red', s=100)
axs[1].set_title('k-Means')

# Clustering Espectral
axs[2].scatter(X[:, 0], X[:, 1], c=clustering_espectral.labels_)
axs[2].set_title('Clustering Espectral')

plt.tight_layout()
plt.show()
