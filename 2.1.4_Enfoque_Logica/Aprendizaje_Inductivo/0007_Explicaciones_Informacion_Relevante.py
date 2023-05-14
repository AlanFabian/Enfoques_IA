#Alan de Jesus Fabian Garcia 
class SistemaExplicativo:
    def __init__(self, modelo):
        self.modelo = modelo

    def obtener_explicacion(self, instancia):
        # Obtener la predicción del modelo
        prediccion = self.modelo.predecir(instancia)

        # Obtener la importancia de cada atributo
        importancia_atributos = self.modelo.calcular_importancia_atributos()

        # Obtener los atributos relevantes para la predicción
        atributos_relevantes = self.modelo.obtener_atributos_relevantes(instancia)

        explicacion = {
            'prediccion': prediccion,
            'importancia_atributos': importancia_atributos,
            'atributos_relevantes': atributos_relevantes
        }

        return explicacion

# Ejemplo de modelo
class Modelo:
    def predecir(self, instancia):
        # Lógica de predicción del modelo
        pass

    def calcular_importancia_atributos(self):
        # Lógica para calcular la importancia de los atributos
        pass

    def obtener_atributos_relevantes(self, instancia):
        # Lógica para obtener los atributos relevantes para la predicción
        pass

# Crear una instancia del modelo
modelo = Modelo()

# Crear una instancia del sistema explicativo
sistema_explicativo = SistemaExplicativo(modelo)

# Ejemplo de instancia a explicar
instancia = {'atributo1': valor1, 'atributo2': valor2, ...}

# Obtener la explicación para la instancia
explicacion = sistema_explicativo.obtener_explicacion(instancia)

# Imprimir la explicación
print(explicacion)
