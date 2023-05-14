#Alan de Jesus Fabian Garcia 
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos de ejemplo (Iris)
datos = load_iris()
X = datos.data
y = datos.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador base (clasificador débil)
clasificador_base = DecisionTreeClassifier(max_depth=1)

# Crear el clasificador Boosting
boosting = AdaBoostClassifier(base_estimator=clasificador_base, n_estimators=50)

# Entrenar el modelo Boosting
boosting.fit(X_entrenamiento, y_entrenamiento)

# Realizar predicciones en el conjunto de prueba
predicciones = boosting.predict(X_prueba)

# Calcular la precisión del modelo
precision = accuracy_score(y_prueba, predicciones)

# Imprimir la precisión del modelo
print("Precisión del modelo Boosting:", precision)
