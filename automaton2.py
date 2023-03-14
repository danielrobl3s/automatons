class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, string):
        current_state = self.start_state
        for char in string:
            if char not in self.alphabet:
                return False
            current_state = self.transition_function[current_state][char]
        return current_state in self.accept_states


# Define the alphabet
alphabet = {'0', '1'}

# Define the states
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}

# Define the initial state
start_state = 'q0'

# Define the final states
accept_states = {'q5'}

# Define the transition function
transition_function = {
    'q0': {'0': 'q1', '1': 'q2'},
    'q1': {'0': 'q1', '1': 'q2'},
    'q2': {'0': 'q3', '1': 'q4'},
    'q3': {'0': 'q3', '1': 'q4'},
    'q4': {'0': 'q5', '1': 'q4'},
    'q5': {'0': 'q6', '1': 'q4'},
    'q6': {'0': 'q6', '1': 'q4'}
}

# Construct the DFA
dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# Test the DFA
print(dfa.accepts('00000110'))
