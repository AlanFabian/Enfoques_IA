#Alan de Jesus Fabian Garcia 
def unify(term1, term2, substitution):
    if substitution is None:
        return None
    elif term1 == term2:
        return substitution
    elif is_variable(term1):
        return unify_variable(term1, term2, substitution)
    elif is_variable(term2):
        return unify_variable(term2, term1, substitution)
    elif is_compound(term1) and is_compound(term2):
        return unify(term1.arguments, term2.arguments, unify(term1.functor, term2.functor, substitution))
    else:
        return None


def unify_variable(variable, term, substitution):
    if variable in substitution:
        return unify(substitution[variable], term, substitution)
    elif term in substitution:
        return unify(variable, substitution[term], substitution)
    else:
        new_substitution = substitution.copy()
        new_substitution[variable] = term
        return new_substitution


def is_variable(term):
    return isinstance(term, str) and term.islower()


def is_compound(term):
    return isinstance(term, Compound)


# Ejemplo de uso

# Definición de la clase Compound para representar términos compuestos
class Compound:
    def __init__(self, functor, arguments):
        self.functor = functor
        self.arguments = arguments

    def __eq__(self, other):
        return self.functor == other.functor and self.arguments == other.arguments


# Términos a unificar
term1 = Compound("f", ["x", "y"])
term2 = Compound("f", ["a", "b"])

# Realizar unificación
substitution = unify(term1, term2, {})

# Imprimir el resultado de la unificación
print("Unificación:")
print(f"Término 1: {term1.functor}({', '.join(term1.arguments)})")
print(f"Término 2: {term2.functor}({', '.join(term2.arguments)})")
print("Substitución:")
for var, value in substitution.items():
    print(f"{var} = {value}")
