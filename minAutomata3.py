def transition(state, symbol):
    transition_table = [
        ('s0', 'a', 's0'),
        ('s0', 'b', 's0'),
        ('s0', 'c', 's0')
    ]
    
    for t in transition_table:
        if t[0] == state and t[1] == symbol:
            return t[2]

def is_accepting(state):
    return state == 's0'

def run_automaton(input_string):
    state = 's0'
    for symbol in input_string:
        state = transition(state, symbol)
    return is_accepting(state)

input_string = input('Enter a word from this alphabet: a,b,c: ')
result = run_automaton(input_string)
if result:
    print(f'{input_string} is accepted')
else:
    print(f'{input_string} is not accepted')
