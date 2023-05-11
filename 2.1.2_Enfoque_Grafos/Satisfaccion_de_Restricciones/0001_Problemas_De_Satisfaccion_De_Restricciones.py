#Alan de Jesus Fabian Garcia
from typing import Dict, List, Optional

class Variable:
    def __init__(self, name: str, domain: List[int]) -> None:
        self.name = name
        self.domain = domain
        self.value: Optional[int] = None

class Constraint:
    def __init__(self, variables: List[Variable], constraint_function) -> None:
        self.variables = variables
        self.constraint_function = constraint_function

    def satisfied(self) -> bool:
        return self.constraint_function([variable.value for variable in self.variables])

class CSP:
    def __init__(self, variables: List[Variable], constraints: List[Constraint]) -> None:
        self.variables = variables
        self.constraints = constraints

    def backtrack(self, assignment: Dict[Variable, int], graph: Dict[Variable, List[Variable]]) -> Optional[Dict[Variable, int]]:
        if len(assignment) == len(self.variables):
            return assignment
        
        unassigned = [variable for variable in self.variables if variable not in assignment]
        first = unassigned[0]
        ordered_domain = self.order_domain_values(first, assignment, graph)
        
        for value in ordered_domain:
            first.value = value
            if self.forward_checking(first, graph):
                assignment[first] = value
                result = self.backtrack(assignment, graph)
                if result is not None:
                    return result
                assignment.pop(first)
            first.value = None
            
        return None

    def forward_checking(self, variable: Variable, graph: Dict[Variable, List[Variable]]) -> bool:
        for neighbor in graph[variable]:
            constraint = [c for c in self.constraints if variable in c.variables and neighbor in c.variables]
            if neighbor.value is None:
                for value in neighbor.domain:
                    variable.value = value
                    if not any(constraint) or all(c.satisfied() for c in constraint):
                        break
                else:
                    return False
            variable.value = None
        return True

    def order_domain_values(self, variable: Variable, assignment: Dict[Variable, int], graph: Dict[Variable, List[Variable]]) -> List[int]:
        values = []
        for value in variable.domain:
            variable.value = value
            if self.forward_checking(variable, graph):
                values.append(value)
        variable.value = None
        return values

def main() -> None:
    variables = [Variable('A', [1, 2, 3]), Variable('B', [1, 2, 3]), Variable('C', [1, 2, 3])]
    constraints = [
        Constraint([variables[0], variables[1]], lambda values: values[0] != values[1]),
        Constraint([variables[1], variables[2]], lambda values: values[1] != values[2])
    ]
    graph = {
        variables[0]: [variables[1]],
        variables[1]: [variables[0], variables[2]],
        variables[2]: [variables[1]]
    }
    csp = CSP(variables, constraints)
    result = csp.backtrack({}, graph)
    if result is None:
        print('No se encontró una solución')
    else:
        print(result)

if __name__ == '__main__':
    main()
