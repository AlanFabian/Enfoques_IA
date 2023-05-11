#Alan de Jesus Fabian Garcia 
class Variable:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        self.value = None
        
    def assign(self, value):
        self.value = value
        
    def unassign(self):
        self.value = None
        
class Constraint:
    def __init__(self, variables, constraint_function):
        self.variables = variables
        self.constraint_function = constraint_function
        
    def satisfied(self):
        return self.constraint_function([variable.value for variable in self.variables])

class CSP:
    def __init__(self, variables, constraints):
        self.variables = variables
        self.constraints = constraints
        
    def backtrack(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        
        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in first.domain:
            if self.check_consistency(first, value, assignment):
                first.assign(value)
                inferences = self.forward_checking(first, assignment)
                if inferences != "failure":
                    assignment[first] = value
                    result = self.backtrack(assignment)
                    if result != "failure":
                        return result
                    del assignment[first]
                first.unassign()
                self.reverse_inferences(inferences)
        return "failure"
    
    def check_consistency(self, variable, value, assignment):
        temp = variable.value
        variable.assign(value)
        consistent = all(constraint.satisfied() for constraint in self.constraints)
        variable.assign(temp)
        return consistent
    
    def forward_checking(self, variable, assignment):
        inferences = {}
        for constraint in self.constraints:
            if variable in constraint.variables and any(v not in assignment for v in constraint.variables):
                for v in constraint.variables:
                    if v not in assignment and v != variable:
                        for value in v.domain:
                            if constraint.satisfied():
                                if v not in inferences:
                                    inferences[v] = set(value)
                                else:
                                    inferences[v].add(value)
                            v.domain.discard(value)
                if not constraint.satisfied():
                    return "failure"
        return inferences
    
    def reverse_inferences(self, inferences):
        for variable in inferences:
            for value in inferences[variable]:
                variable.domain.add(value)
    
if __name__ == '__main__':
    variables = [Variable('A', {1, 2, 3}),
                 Variable('B', {1, 2, 3}),
                 Variable('C', {1, 2, 3})]
    
    constraints = [Constraint([variables[0], variables[1]], lambda values: values[0] != values[1]),
                   Constraint([variables[1], variables[2]], lambda values: values[1] != values[2])]
    
    csp = CSP(variables, constraints)
    result = csp.backtrack()
    
    if result == "failure":
        print("No solution found.")
    else:
        print(result)
