import math
import random

lives = 6
words = [
    'owoc: ananas',
    'mebel: komoda',
    'zwierzę: koń',
    'broń: karabin',
    'sport: krykiet',
    'kraj: Albania',
    'stolica: Oslo'
]

nick = input('Podaj swój nick: ')
print(f'\nWitaj {nick}!')

randIndex = math.floor(random.random() * 7)
word = words[randIndex]
wordSplit = word.split(' ')
wordFinal = wordSplit[1]

wordEncoded = []
for i in range(len(wordSplit[1])):
    wordEncoded.append(wordSplit[1].replace(wordSplit[1], '_'))

while(True):
    print(f'\nŻycia:' + (' + ' * lives))
    print(f'Podaj hasło - {wordSplit[0]}')
    print(*wordEncoded, sep=" ")
    guess = input('')

    if(guess not in wordFinal):
        print('Błędny wyraz')
        lives -= 1
    else:
        for i in range(len(wordFinal)):
            if (guess in wordFinal[i]):
                wordEncoded[i] = guess
    if(lives == 0):
        print(f'\nPoprawne hasło to: {wordFinal}')
        print('Przegrałeś 🤷‍')
        exit()
    elif(guess == wordFinal or ''.join(wordEncoded) == wordFinal):
        print(f'\n{wordFinal}')
        print('Wygrałeś! 🎉')
        exit()