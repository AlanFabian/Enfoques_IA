#Alan de Jesus Fabian Garcia 
class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent


class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def forward_chaining(self, facts):
        inferred_facts = set(facts)
        while True:
            new_facts = set()
            for rule in self.rules:
                if all(antecedent in inferred_facts for antecedent in rule.antecedents) and rule.consequent not in inferred_facts:
                    new_facts.add(rule.consequent)
            if not new_facts:
                break
            inferred_facts.update(new_facts)
        return inferred_facts

    def backward_chaining(self, goal, known_facts):
        if goal in known_facts:
            return True
        for rule in self.rules:
            if rule.consequent == goal:
                if all(self.backward_chaining(antecedent, known_facts) for antecedent in rule.antecedents):
                    return True
        return False


# Ejemplo de uso

# Crear reglas
rule1 = Rule(["A"], "B")
rule2 = Rule(["B"], "C")
rule3 = Rule(["C"], "D")

# Crear base de conocimiento
knowledge_base = KnowledgeBase()

# Agregar reglas a la base de conocimiento
knowledge_base.add_rule(rule1)
knowledge_base.add_rule(rule2)
knowledge_base.add_rule(rule3)

# Ejemplo de encadenamiento hacia adelante
facts = ["A"]
inferred_facts = knowledge_base.forward_chaining(facts)
print("Encadenamiento hacia adelante:")
print("Hechos iniciales:", facts)
print("Hechos inferidos:", inferred_facts)

# Ejemplo de encadenamiento hacia atrás
goal = "D"
known_facts = set(facts)
result = knowledge_base.backward_chaining(goal, known_facts)
print("\nEncadenamiento hacia atrás:")
print("Meta:", goal)
print("Hechos conocidos:", known_facts)
print("Resultado:", result)
