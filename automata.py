class State():
    def __init__(self, number, stat =' ', transitions = []):
        self.number = number
        self.transitions = transitions
        self.stat = stat

def automataTransition(word):
    symbol = ''
    for i in word:
        for j in range(len(automata)):
            if str(automata[j][transition]) == i:
                symbol += i
                print('symbol: ' + symbol)
            else: 
                exit()

istate = 0
state = 0
fstate = 0
transition = 0
word = ''
symbol = ''

st0 = any
st1 = any
st2 = any

automata = {
    st0: State(0, 'initial', [0]),
    st1: State(1, ' ', [0,1]),
    st2: State(2, 'final', [])
}



word = input('Put a word from this alphabet: 0 and 1: ')
automataTransition(word)