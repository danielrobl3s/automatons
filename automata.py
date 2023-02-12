istate = 0
state = 0
fstate = 0
transition = 0
word = ''
symbol = ''

automata = [{
    istate: 0,
    transition: 0,
}, 
{
    state: 1,
    transition: 0,

}, 
{
    state: 2,
    transition: 0,
    transition: 1,
}, 
{
    fstate: 3,
}]

def automataTransition(word):
    for i in word:
        for j in len(automata):
            if str(automata[j][transition]) == i:
                symbol += i
                print('symbol: ' + i)
            else: 
                exit()

word = input('Put a word from this alphabet: 0 and 1: ')
automataTransition(word)