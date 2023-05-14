#Alan De Jesus Fabian Garcia 
import re

# Texto de entrada
texto = "Mi nombre es Juan y mi número de teléfono es 555-1234. Vivo en Ciudad ABC."

# Expresiones regulares para extraer nombre y número de teléfono
regex_nombre = r"Mi nombre es (\w+)"
regex_telefono = r"mi número de teléfono es (\d{3}-\d{4})"

# Extraer información utilizando expresiones regulares
nombre = re.search(regex_nombre, texto).group(1)
telefono = re.search(regex_telefono, texto).group(1)

# Imprimir la información extraída
print("Nombre:", nombre)
print("Teléfono:", telefono)
