#Alan de Jesus Fabian Garcia 
def conflict(q, p):
    # Función que verifica si hay conflicto entre dos reinas
    return q == p or abs(q - p) == abs(len(q) - len(p))
    
def backtrack(q, n):
    if len(q) == n:
        return q
    
    # Seleccionar la siguiente columna para colocar una reina
    c = len(q)
    
    # Lista de posibles filas para la columna seleccionada
    candidates = list(range(n))
    
    # Ordenar las filas de acuerdo al número de conflictos
    candidates.sort(key=lambda r: sum(conflict(r, q[c]) for c in range(len(q))))
    
    for r in candidates:
        if not conflict(r, q[c]):
            # Si no hay conflicto, colocar la reina y seguir buscando
            sol = backtrack(q + [r], n)
            if sol is not None:
                return sol
        else:
            # Si hay conflicto, retroceder a la posición anterior con más conflictos
            break
    
    # Si no se encontró solución, retroceder a la posición anterior con más conflictos
    if not q:
        return None
    else:
        return backtrack(q[:-1], n)

# Ejemplo de uso
n = 4
sol = backtrack([], n)
if sol is not None:
    # Imprimir la solución encontrada
    print("Solución encontrada:")
    for row in sol:
        print("".join("Q" if i == row else "." for i in range(n)))
else:
    print("No se encontró solución.")
