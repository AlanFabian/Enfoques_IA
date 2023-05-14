#Alan de Jesus Fabian Garcia 
# Definición de la clase Factor
class Factor:
    def __init__(self, variables, table):
        self.variables = variables  # Lista de variables en el factor
        self.table = table  # Tabla de valores del factor

    def __str__(self):
        return f"Variables: {self.variables}, Table: {self.table}"

# Definición de la función de eliminación de variables
def eliminar_variables(factor, variables_a_eliminar):
    nuevas_variables = list(set(factor.variables) - set(variables_a_eliminar))

    if len(nuevas_variables) == 0:
        # Si no quedan variables en el factor, devolvemos un factor con una tabla constante de 1
        return Factor([], [1])

    # Filtramos las filas de la tabla que corresponden a las variables a eliminar
    tabla_filtrada = []
    for fila in factor.table:
        fila_filtrada = [valor for idx, valor in enumerate(fila) if factor.variables[idx] not in variables_a_eliminar]
        tabla_filtrada.append(fila_filtrada)

    return Factor(nuevas_variables, tabla_filtrada)

# Creación de un factor de ejemplo
variables = ['A', 'B', 'C']
tabla = [
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6]
]
factor_ejemplo = Factor(variables, tabla)

print("Factor original:")
print(factor_ejemplo)

# Eliminamos la variable 'B'
variables_a_eliminar = ['B']
factor_eliminado = eliminar_variables(factor_ejemplo, variables_a_eliminar)

print("\nFactor eliminado:")
print(factor_eliminado)
