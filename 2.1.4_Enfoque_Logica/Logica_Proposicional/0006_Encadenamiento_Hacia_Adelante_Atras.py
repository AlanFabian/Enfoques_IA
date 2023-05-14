#Alan de Jesus Fabian Garcia 
class Rule:
    def __init__(self, conditions, result):
        self.conditions = conditions
        self.result = result

    def applies(self, facts):
        return all(condition in facts for condition in self.conditions)


class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def add_fact(self, fact):
        self.facts.append(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def forward_chaining(self):
        new_facts = True
        while new_facts:
            new_facts = False
            for rule in self.rules:
                if rule.applies(self.facts) and rule.result not in self.facts:
                    self.facts.append(rule.result)
                    new_facts = True

    def backward_chaining(self, goal):
        if goal in self.facts:
            return True
        for rule in self.rules:
            if goal == rule.result:
                satisfied = True
                for condition in rule.conditions:
                    if not self.backward_chaining(condition):
                        satisfied = False
                        break
                if satisfied:
                    return True
        return False


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

# Realizar encadenamiento hacia adelante
kb.forward_chaining()

# Imprimir hechos
print("Hechos en la base de conocimiento:")
print(kb.facts)

# Realizar encadenamiento hacia atrás
goal = "S"
result = kb.backward_chaining(goal)

# Imprimir resultado
if result:
    print(f"El objetivo '{goal}' es alcanzable.")
else:
    print(f"El objetivo '{goal}' no es alcanzable.")
