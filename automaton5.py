class Automaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            ('q0', '1'): 'q1',
            ('q1', '1'): 'q2',
            ('q2', '1'): 'q1'
        }
        self.initial_state = 'q0'
        self.final_state = 'q2'

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
    input_string = ''
    result = a.run(input_string)
    print(result)
