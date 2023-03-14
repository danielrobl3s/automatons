class Automaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qf'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            ('q0', '0'): 'q1',
            ('q1', '0'): 'q2',
            ('q1', '1'): 'q3',
            ('q2', '0'): 'q2',
            ('q2', '1'): 'q3',
            ('q3', '0'): 'q4',
            ('q3', '1'): 'q5',
            ('q4', '0'): 'q4',
            ('q4', '1'): 'q5',
            ('q5', '0'): 'q6',
            ('q6', '0'): 'q7',
            ('q6', '1'): 'qf',
            ('q7', '0'): 'q7',
            ('q7', '1'): 'qf'
        }
        self.initial_state = 'q0'
        self.final_state = 'qf'

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
    input_string = '0001010001'
    result = a.run(input_string)
    print(result)  # should print True
