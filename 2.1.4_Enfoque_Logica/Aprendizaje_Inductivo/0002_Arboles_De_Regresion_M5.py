#Alan de Jesus Fabian Garcia 
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import StackingRegressor

# Cargar el conjunto de datos de ejemplo (Boston Housing)
datos = load_boston()
X = datos.data
y = datos.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión lineal
regresor_lineal = LinearRegression()

# Crear un modelo de árbol de decisión para regresión
regresor_arbol = DecisionTreeRegressor()

# Combinar los modelos en un ensamblaje
modelo_ensamblado = StackingRegressor(
    estimators=[('regresor_lineal', regresor_lineal), ('regresor_arbol', regresor_arbol)]
)

# Entrenar el modelo ensamblado
modelo_ensamblado.fit(X_entrenamiento, y_entrenamiento)

# Evaluar el modelo en el conjunto de prueba
puntuacion = modelo_ensamblado.score(X_prueba, y_prueba)

# Imprimir la puntuación de precisión del modelo
print("Puntuación del modelo ensamblado:", puntuacion)
