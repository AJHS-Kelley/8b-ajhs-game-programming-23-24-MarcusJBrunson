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
    ======''',] 

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

# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1

