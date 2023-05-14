#Alan de Jesus Fabian Garcia 
class Rule:
    def __init__(self, symptoms, cause):
        self.symptoms = symptoms
        self.cause = cause

    def match(self, observed_symptoms):
        return all(symptom in observed_symptoms for symptom in self.symptoms)


class DiagnosticSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def diagnose(self, observed_symptoms):
        for rule in self.rules:
            if rule.match(observed_symptoms):
                return rule.cause

        return "Unknown"


# Ejemplo de uso

# Crear reglas de diagnóstico y causales
rule1 = Rule(["Fiebre", "Dolor de cabeza"], "Gripe")
rule2 = Rule(["Dolor de garganta", "Congestión nasal"], "Resfriado")
rule3 = Rule(["Dolor de cabeza", "Visión borrosa"], "Migraña")

# Crear sistema de diagnóstico
diagnostic_system = DiagnosticSystem()

# Agregar reglas al sistema de diagnóstico
diagnostic_system.add_rule(rule1)
diagnostic_system.add_rule(rule2)
diagnostic_system.add_rule(rule3)

# Observar síntomas y obtener el diagnóstico
observed_symptoms = ["Fiebre", "Dolor de cabeza"]
diagnosis = diagnostic_system.diagnose(observed_symptoms)

# Imprimir el resultado del diagnóstico
print("Diagnóstico:")
print(f"Síntomas observados: {observed_symptoms}")
print(f"Diagnóstico: {diagnosis}")
