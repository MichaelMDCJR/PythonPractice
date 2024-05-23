import random

# Hangman pictures
def hangman_state(statevalue):
    if statevalue == 0:
        return """
         ______
         |
         | 
         |
        ___
        """
    elif statevalue == 1:
        return """
         ______
         |    O
         | 
         |
        ___
        """
    elif statevalue == 2:
        return """
         ______
         |    O
         |    |
         |
        ___
        """
    elif statevalue == 3:
        return """
         ______
         |    O
         |   /|
         |
        ___
        """
    elif statevalue == 4:
        return r"""
         ______
         |    O
         |   /|\
         |
        ___
        """
    elif statevalue == 5:
        return r"""
         ______
         |    O
         |   /|\
         |    /
        ___
        """
    elif statevalue == 6:
        return r"""
         ______
         |    O
         |   /|\
         |    /\
        ___
        """

words = ['cat', 'random', 'window', 'python', 'remind', 'computer', 'tree', 'monster', 'mouse', 'printer', 'diving', 'execute', 'lists', 'doors', 'happy']
state = 0
guessed = False

randomVar = random.randrange(0, len(words))

wordLength = len(words[randomVar])
myWord = words[randomVar]
lettersGuessed = 0
changed = False

array = []
for i in range(wordLength):
    array.append('_ ')

while not guessed:
    # prints hangman
    print(hangman_state(state))

    # prints array
    for i in range(len(array)):
        if array[i] == '_ ':
            print('_ ', end='')
        else:
            print(array[i] + ' ', end='')

    letter = input("\nWhat letter do you guess: ")

    for i in range(wordLength):
        if myWord[i] == letter:
            array[i] = letter
            lettersGuessed += 1
            changed = True

    if not changed:
        state += 1
    changed = False

    if lettersGuessed == wordLength:
        guessed = True
        print("The word was: " + myWord)
        print("You win!")
        break

    if state == 6:
        print("You lose!")
        print("The word was: " + myWord)
        break
