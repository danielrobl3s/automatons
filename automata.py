class State():
    def __init__(self, number, stat =' ', transitions = []):
        self.number = number
        self.transitions = transitions
        self.stat = stat

def automataTransition(word):
    symbol = ''
    for i in word:
        for j in range(len(automata)):
            print(str(automata[j].stat))

word = ''
symbol = ''

automata = [
    State(0, 'initial', [0]),
    State(1, ' ', [0, 1]),
    State(2, 'final', [])
]



word = input('Put a word from this alphabet: 0 and 1: ')
automataTransition(word)