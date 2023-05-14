#Alan de Jesus Fabian Garcia 
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos de ejemplo (Iris dataset)
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador Naive Bayes
clf = GaussianNB()

# Entrenar el clasificador utilizando el conjunto de entrenamiento
clf.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión: {:.2f}".format(accuracy))
