#Alan de Jesus Fabian Garcia 
class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self, expression):
        if expression in self.facts:
            return True

        for rule in self.rules:
            if rule.implies(expression):
                return self.evaluate(rule.result)

        return False


class Rule:
    def __init__(self, conditions, result):
        self.conditions = conditions
        self.result = result

    def implies(self, expression):
        return expression == self.result


# Ejemplo de uso
kb = KnowledgeBase()

# Agregar hechos
kb.add_fact("P")
kb.add_fact("Q")

# Agregar reglas
rule1 = Rule(["P", "Q"], "R")
rule2 = Rule(["R"], "S")
kb.add_rule(rule1)
kb.add_rule(rule2)

# Realizar inferencia
print(kb.evaluate("P"))  # Devuelve True
print(kb.evaluate("R"))  # Devuelve True
print(kb.evaluate("S"))  # Devuelve True
print(kb.evaluate("Q"))  # Devuelve False
