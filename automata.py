#Class to create an object 'state' which will be added to our automata list down below
class State():
    def __init__(self, number, stat =' ', transitions = {}, symbols = {}):
        self.number = number
        self.transitions = transitions
        self.symbols = symbols
        self.stat = stat
#function to transition and store the symbols that make up the word

def automataTransition(word):
    symbol = ''
    j = 0
    for i in automata:
        keys = list(i.transitions.keys())
        print(keys)

        for w in word:
            if word[w] in str(keys):
                symbol += word[w]
            elif i.stat == 'final':
                print('done!')
                exit()
            else:
                print('not a valid word')
                exit()
        j += 1

word = ''
symbol = ''

#Automata variable is a list which stores a series of states objects
automata = [
    State(0, 'initial', {0: 1}, {1: 0}),
    State(1, ' ', {0: 1, 1: 2}, {2:1}),
    State(2, 'final', {}, {})
]

#Entry point
word = input('Put a word from this alphabet: 0 and 1:  ')
automataTransition(word)