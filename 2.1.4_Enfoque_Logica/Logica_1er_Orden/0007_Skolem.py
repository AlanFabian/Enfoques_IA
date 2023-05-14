#Alan de Jesus Fabian Garcia 
class Clause:
    def __init__(self, literals):
        self.literals = literals

    def __repr__(self):
        return ' ∨ '.join(str(literal) for literal in self.literals)


class Literal:
    def __init__(self, predicate, arguments):
        self.predicate = predicate
        self.arguments = arguments

    def __repr__(self):
        return f'{self.predicate}({", ".join(str(arg) for arg in self.arguments)})'


class Skolem:
    def __init__(self, function_name, arity):
        self.function_name = function_name
        self.arity = arity

    def __repr__(self):
        return f'{self.function_name}/{self.arity}'


def skolemize(clause):
    skolem_constants = {}
    skolemized_literals = []

    for literal in clause.literals:
        skolemized_args = []
        for arg in literal.arguments:
            if isinstance(arg, str) and arg[0].isupper():
                if arg not in skolem_constants:
                    skolem_constants[arg] = Skolem('sk_' + arg, 0)
                skolemized_args.append(skolem_constants[arg])
            else:
                skolemized_args.append(arg)
        skolemized_literal = Literal(literal.predicate, skolemized_args)
        skolemized_literals.append(skolemized_literal)

    return Clause(skolemized_literals)


def resolve(clause1, clause2):
    resolved_clauses = []
    for literal1 in clause1.literals:
        for literal2 in clause2.literals:
            if literal1.predicate == literal2.predicate and literal1.arguments != literal2.arguments:
                resolved_literals = clause1.literals + clause2.literals
                resolved_literals.remove(literal1)
                resolved_literals.remove(literal2)
                resolved_clause = Clause(resolved_literals)
                resolved_clauses.append(resolved_clause)
    return resolved_clauses


# Ejemplo de uso

# Cláusulas
clause1 = Clause([Literal('P', ['x']), Literal('Q', ['x', 'y'])])
clause2 = Clause([Literal('P', ['a']), Literal('Q', ['a', 'b'])])

# Skolemización
skolemized_clause1 = skolemize(clause1)
skolemized_clause2 = skolemize(clause2)

# Resolución
resolved_clauses = resolve(skolemized_clause1, skolemized_clause2)

# Imprimir resultado
print("Cláusula 1:", clause1)
print("Cláusula 2:", clause2)
print("Skolemización de la cláusula 1:", skolemized_clause1)
print("Skolemización de la cláusula 2:", skolemized_clause2)
print("Resolución:", resolved_clauses)
