#Alan de Jesus Fabian Garcia 
def apply_func(func, value):
    return func(value)

def square(x):
    return x * x

def cube(x):
    return x * x * x

# Ejemplo de uso

result = apply_func(square, 5)
print("Cuadrado de 5:", result)

result = apply_func(cube, 3)
print("Cubo de 3:", result)
