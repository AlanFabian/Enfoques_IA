#Alan de Jesus Fabian Garcia 
class DefaultLogicAgent:
    def __init__(self, kb):
        self.kb = kb

    def ask(self, query):
        return self.kb.query(query)

    def tell(self, sentence):
        self.kb.add_sentence(sentence)


class DefaultLogicKnowledgeBase:
    def __init__(self):
        self.sentences = []
        self.defaults = []

    def add_sentence(self, sentence):
        self.sentences.append(sentence)

    def add_default(self, default):
        self.defaults.append(default)

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
                if self.evaluate(antecedent, bindings):
                    return self.evaluate(consequent, bindings)
                else:
                    return self.evaluate_default(consequent, bindings)

    def evaluate_default(self, expression, bindings):
        for default in self.defaults:
            if default[0] == expression:
                antecedent = default[1]
                consequent = default[2]
                if self.evaluate(antecedent, bindings):
                    return self.evaluate(consequent, bindings)
        return None


# Ejemplo de uso

# Crear base de conocimiento por defecto
kb = DefaultLogicKnowledgeBase()

# Agregar conocimiento a la base de conocimiento
kb.add_sentence(('implies', 'A', 'B'))  # A ⇒ B

# Agregar reglas por defecto a la base de conocimiento
kb.add_default(('B', 'not C', 'D'))  # Si B es verdadero, pero no C, entonces D es verdadero

# Crear agente de lógica por defecto
agent = DefaultLogicAgent(kb)

# Consultar al agente
result = agent.ask('B')
print("¿B es verdadero?:", result)

result = agent.ask('C')
print("¿C es verdadero?:", result)

result = agent.ask('D')
print("¿D es verdadero?:", result)
