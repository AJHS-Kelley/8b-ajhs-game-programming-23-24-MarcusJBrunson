# Hangman Game by Marcus Brunson, v0.3
import random 
words = 'Horse Cat Lion Cow Goat Sheep Bear Cheetah Gorilla Camel aggressive futuristic diverse fraudulent dictionary mitochondrion chromosome endomembrane vacuole'.split()

# VARIABLE_NAMES IN ALL-CAPS ARE CONSTANTS ARE NOT MEANT TO CHANGE!
HANGMAN_BOARD =['''
    +---+
        |
        |
        |
    ======''','''
    +---+
    O   |
        |
        |
    ======''','''
    +---+
    O    |
    |   |
        |
    ======''','''
    +---+
    O       |
   /|       |
            |
    ======''','''
    +---+
    O    |
   /|\   |
        |
    ======''','''
    +---+
    O    |
   /|\   |
   /      |
    ======''','''
    +---+
        |
        |
        |
    ======''','''
    +---+
    O       |
   /|\    |
   / \ |
    ======''']

# Pick Word from List 
def getRandomWord(wordList): # Return a random word from the list
    wordIndex = random.randint(0, len(wordList)-1) 
    # len(listname) -1 is extremely common for working with lists.
    return wordList[wordIndex] 

def displayBoard(missedLetters, correctLetters, sercetWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blanks = '_' * len(sercetWord) 
    
    # Replace Blanks with Correct Letters 
    for i in range(len(sercetWord)): 
        if sercetWord[i] in correctLetters: 
            blanks = blanks[:i] + sercetWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter and press enter.') 
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please entera single letter.')
        elif guess in alreadyGuessed:
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the English alphabet.') 
        else:
            return guess

def playAgain(): 
    print('Do you want to play again? yes or no?')
    return input().lower().startswith('y')

# Introduce the Game 
print('Welcome to Hangman by Marcus B.')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main Game Loop
while True:
    displayBoard(missedLetters, correctLetters, secretWord) 

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess 

        # Check to See if Winner, Winner Chicken Dinner
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False 
                break
            if foundAllLetters:
                print('Much wow! Very win! Well done.')
                print('The secret word was' + secretWord)
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord) 
            print('You have run out of guesses and lost the game.')
            print('You made this number of correct guesses' + str(len(correctLetters)))
            print('The secret word was' + secretWord)
            gameIsDone = True
    
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break


# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1

