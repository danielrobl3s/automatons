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
}
]

def automataTransition(word):
    c = 0
    for i in word:
        for j in automata:
            c += 1
            if i == automata[c].state:
                result += i
                print('letter' + word[i] + ' accepted, state: ' + c)
            else:
                print('word not accepted')
                exit()


word = input('tell me a word')
automataTransition(word)
print('your word is: ' + word)