#Alan de Jesus Fabian Garcia 
import itertools

def generate_truth_table(variables):
    table = []
    n = len(variables)
    for values in itertools.product([False, True], repeat=n):
        row = dict(zip(variables, values))
        table.append(row)
    return table

def evaluate_expression(expression, variables):
    truth_table = generate_truth_table(variables)
    for row in truth_table:
        row['result'] = eval(expression, row)
    return truth_table

# Ejemplo de uso
variables = ['P', 'Q']
expression = 'P and Q'
table = evaluate_expression(expression, variables)

# Imprimir la tabla de verdad
header = variables + [expression]
print('|'.join(header))
print('-' * len(header))
for row in table:
    values = [str(row[var]) for var in variables] + [str(row['result'])]
    print('|'.join(values))
