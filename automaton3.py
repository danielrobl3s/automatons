class Automaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q1', 'a'): 'q2',
            ('q1', 'b'): 'q3',
            ('q2', 'a'): 'q2',
            ('q2', 'b'): 'q3',
            ('q3', 'a'): 'q1'
        }
        self.initial_state = 'q0'
        self.final_states = {'q0', 'q3'}  # including the initial state as a final state

    def run(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.final_states

if __name__ == '__main__':
    a = Automaton()
    input_string = ''
    result = a.run(input_string)
    print(result) 