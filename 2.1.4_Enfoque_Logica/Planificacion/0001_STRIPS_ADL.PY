#Alan de Jesus Fabian Garcia 
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def is_applicable(self, state):
        return all(condition in state for condition in self.preconditions)

    def apply(self, state):
        if self.is_applicable(state):
            state.update(self.effects)
            return state
        else:
            raise Exception("Action cannot be applied to the current state.")

def strips(initial_state, goal_state, actions):
    plan = []

    while goal_state.items() - initial_state.items():
        applicable_actions = [action for action in actions if action.is_applicable(initial_state)]

        if not applicable_actions:
            raise Exception("Goal state is not reachable from the initial state.")

        action = applicable_actions[0]
        plan.append(action.name)
        initial_state = action.apply(initial_state)

    return plan

# Definición de las acciones
actions = [
    Action('Action1', {'condition1'}, {'effect1'}),
    Action('Action2', {'effect1'}, {'effect2'}),
    Action('Action3', {'condition2'}, {'effect1', 'effect3'})
]

# Definición del estado inicial y el estado objetivo
initial_state = {'condition1', 'condition2'}
goal_state = {'effect2', 'effect3'}

# Ejecutar el algoritmo STRIPS
plan = strips(initial_state, goal_state, actions)

# Imprimir el plan generado
print("Plan:", plan)
