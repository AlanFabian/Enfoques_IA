#Alan de Jesus Fabian Garcia 
class TemporalLogicAgent:
    def __init__(self, kb):
        self.kb = kb

    def ask(self, query):
        return self.kb.query(query)

    def tell(self, sentence):
        self.kb.add_sentence(sentence)


class TemporalKnowledgeBase:
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
            elif operator == 'always':
                arg = expression[1]
                return self.evaluate(arg, bindings)
            elif operator == 'eventually':
                arg = expression[1]
                return self.evaluate(arg, bindings)


# Ejemplo de uso

# Crear base de conocimiento temporal
kb = TemporalKnowledgeBase()

# Agregar conocimiento a la base de conocimiento
kb.add_sentence(('always', ('implies', 'A', 'B')))  # ◻(A ⇒ B)
kb.add_sentence(('eventually', 'A'))  # ◇A

# Crear agente de lógica temporal
agent = TemporalLogicAgent(kb)

# Consultar al agente
result = agent.ask(('always', 'B'))  # ◻B
print("¿B siempre es verdadero?:", result)

result = agent.ask(('eventually', 'B'))  # ◇B
print("¿B es eventualmente verdadero?:", result)

result = agent.ask(('always', 'A'))  # ◻A
print("¿A siempre es verdadero?:", result)
