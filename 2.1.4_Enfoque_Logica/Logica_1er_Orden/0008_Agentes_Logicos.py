#Alan de Jesus Fabian Garcia 
class LogicalAgent:
    def __init__(self, kb):
        self.kb = kb

    def ask(self, query):
        return self.kb.query(query)

    def tell(self, sentence):
        self.kb.add_sentence(sentence)


class KnowledgeBase:
    def __init__(self):
        self.sentences = []

    def add_sentence(self, sentence):
        self.sentences.append(sentence)

    def query(self, query):
        return self.evaluate(query, {})

    def evaluate(self, expression, bindings):
        if isinstance(expression, str):
            if expression in bindings:
                return bindings[expression]
            else:
                return None
        elif isinstance(expression, tuple):
            operator = expression[0]
            if operator == 'not':
                arg = expression[1]
                return not self.evaluate(arg, bindings)
            elif operator == 'and':
                arg1 = expression[1]
                arg2 = expression[2]
                return self.evaluate(arg1, bindings) and self.evaluate(arg2, bindings)
            elif operator == 'or':
                arg1 = expression[1]
                arg2 = expression[2]
                return self.evaluate(arg1, bindings) or self.evaluate(arg2, bindings)
            elif operator == 'implies':
                antecedent = expression[1]
                consequent = expression[2]
                return (not self.evaluate(antecedent, bindings)) or self.evaluate(consequent, bindings)
            elif operator == 'forall':
                variable = expression[1]
                domain = expression[2]
                body = expression[3]
                for value in domain:
                    new_bindings = dict(bindings)
                    new_bindings[variable] = value
                    if not self.evaluate(body, new_bindings):
                        return False
                return True
            elif operator == 'exists':
                variable = expression[1]
                domain = expression[2]
                body = expression[3]
                for value in domain:
                    new_bindings = dict(bindings)
                    new_bindings[variable] = value
                    if self.evaluate(body, new_bindings):
                        return True
                return False


# Ejemplo de uso

# Crear base de conocimiento
kb = KnowledgeBase()

# Agregar conocimiento a la base de conocimiento
kb.add_sentence(('implies', ('and', 'A', 'B'), 'C'))  # (A ∧ B) ⇒ C
kb.add_sentence(('or', 'A', 'B'))  # A ∨ B

# Crear agente lógico
agent = LogicalAgent(kb)

# Consultar al agente
result = agent.ask('C')
print("¿C es verdadero?:", result)

result = agent.ask('A')
print("¿A es verdadero?:", result)

result = agent.ask('B')
print("¿B es verdadero?:", result)
