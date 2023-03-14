def transition(state, symbol):
    transitions = {
        's0': [('a', 's4'), ('b', 's5'), ('c', 's1')],
        's1': [('a', 's5'), ('b', 's5'), ('c', 's3')],
        's3': [('a', 's5'), ('b', 's5'), ('c', 's5')],
        's4': [('a', 's4'), ('b', 's3'), ('c', 's1')],
    }
    for (input_symbol, next_state) in transitions.get(state, []):
        if input_symbol == symbol:
            return next_state
    return None

def is_accepting(state):
    return state == 's3'

def run_automaton(input_string):
    state = 's0'
    for symbol in input_string:
        state = transition(state, symbol)
        if state is None or state == 's5':
            return False
    return is_accepting(state)

input_string = input('Enter a word from this alphabet: a,b,c: ')
result = run_automaton(input_string)
if result:
    print(f'{input_string} is accepted')
else:
    print(f'{input_string} is not accepted')
