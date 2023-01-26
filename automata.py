state1 = 0
state2 = 0
state3 = 0
tState = 0
firstState = 1
finalState = 3
symbol1 = ''
symbol2 = ''

automata={
    state1: 1,
    symbol1: '0',
    tState: 2,

    state2: 2,
    symbol2: '0',
    tState: [2,3]
}

def automataTransition(word):
    for i in word:
        if i == automata.state1:
            pass

word = input('ingresa una palabra')
