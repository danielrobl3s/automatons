class State():
    def __init__(self, number, stat =' ', transitions = {}):
        self.number = number
        self.transitions = transitions
        self.stat = stat

def automataTransition(word):
    symbol = ''
    cstate = 0
    for i in automata:
        if '0' == word[0]:
            pass
        else:
            print('not a valid word')
            exit()

word = ''
symbol = ''
cstate = 0

automata = [
    State(0, 'initial', {0: 1}),
    State(1, ' ', {0: 1, 1: 2}),
    State(2, 'final', {})
]



word = input('Put a word from this alphabet: 0 and 1:  ')
automataTransition(word)