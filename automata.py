state = 0
transition = 0
symbol = ''
word = ''
result = ''

automata=[{
    state: 1,
    symbol: '0',
    transition: 2
},
{
    state: 2,
    symbol: '0',
    transition: 2
},
{
    state: 2,
    symbol: '1',
    transition: 3
}]

def automataTransition(word):
    result = ''
    for i in word:
        for j in range(len(automata)):
            if i == str(automata[j][symbol]) and str(automata[j][transition]) != j:
                result += i
                print('letter' + word[j] + ' accepted, state: ' + str(j))
            else:
                print('word not accepted')
                exit()
    

word = input('tell me a word')
automataTransition(word)
print('your word ' + result + ' is able to being made by the automata')