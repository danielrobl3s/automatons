class Automaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q1', 'a'): 'q2',
            ('q2', 'a'): 'q3',
            ('q2', 'b'): 'q5',
            ('q3', 'a'): 'q4',
            ('q4', 'a'): 'q3',
            ('q4', 'b'): 'q5',
            ('q5', 'b'): 'q6',
            ('q6', 'b'): 'q7',
            ('q7', 'a'): 'q8',
            ('q7', 'b'): 'q9',
            ('q9', 'a'): 'q8',
            ('q9', 'b'): 'q10',
            ('q10', 'a'): 'q8',
            ('q10', 'b'): 'q9'
        }
        self.initial_state = 'q0'
        self.final_state = 'q8'

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
    input_string = 'aaaaaabbba'
    result = a.run(input_string)
    print(result)  