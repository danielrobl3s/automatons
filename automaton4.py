class Automaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q1', 'a'): 'q2',
            ('q1', 'b'): 'q3',
            ('q2', 'a'): 'q2',
            ('q2', 'b'): 'q4',
            ('q3', 'a'): 'q1',
            ('q3', 'b'): 'q5',
            ('q4', 'a'): 'q1',
        }
        self.initial_state = 'q0'
        self.final_state = 'q5'

    def run(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state == self.final_state


if __name__ == '__main__':
    a = Automaton()
    input_string = 'aabbabb'
    result = a.run(input_string)
    print(result)
