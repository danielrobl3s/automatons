def transition(state, symbol):
    transitions = {
        's0': [('a', 's1'), ('b', 's2'), ('c', 's3')],
        's1': [('a', 's2'), ('b', 's3'), ('c', 's1')],
        's2': [('a', 's3'), ('b', 's1'), ('c', 's3')],
        's3': [('a', 's3'), ('b', 's3'), ('c', 's3')],
    }
    for (input_symbol, next_state) in transitions[state]:
        if input_symbol == symbol:
            return next_state
    return None

def is_accepting(state):
    return state == 's3'

def run_automaton(input_string):
    state = 's0'
    for symbol in input_string:
        state = transition(state, symbol)
        if state is None:
            return False
    return is_accepting(state)

input_string = input('Introduce a word from the alphabet: a,b,c: ')
result = run_automaton(input_string)
if result:
    print(f'{input_string} is accepted')
else:
    print(f'{input_string} is not accepted')
