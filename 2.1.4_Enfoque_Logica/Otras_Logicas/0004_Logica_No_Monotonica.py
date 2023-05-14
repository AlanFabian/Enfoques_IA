#Alan de Jesus Fabian Garcia 
class MonotonicLogicAgent:
    def __init__(self, kb):
        self.kb = kb

    def ask(self, query):
        return self.kb.query(query)

    def tell(self, sentence):
        self.kb.add_sentence(sentence)


class MonotonicKnowledgeBase:
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


# Ejemplo de uso

# Crear base de conocimiento monótona
kb = MonotonicKnowledgeBase()

# Agregar conocimiento a la base de conocimiento
kb.add_sentence(('implies', 'A', 'B'))  # A ⇒ B

# Crear agente de lógica monótona
agent = MonotonicLogicAgent(kb)

# Consultar al agente
result = agent.ask('B')
print("¿B es verdadero?:", result)

# Agregar nueva información
kb.add_sentence('C')  # Agregar nueva información C

# Consultar nuevamente al agente
result = agent.ask('B')
print("¿B sigue siendo verdadero?:", result)
