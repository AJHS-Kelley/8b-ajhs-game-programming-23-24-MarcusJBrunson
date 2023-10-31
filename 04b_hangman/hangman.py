# Hangman Game by Marcus Brunson, v0.1

words = 'Horse Cat Lion Cow Goat Sheep Bear Cheetah Gorilla Camel aggressive futuristic diverse fraudulent dictionary mitochondrion chromosome endomembrane vacuole'.split()

# VARIABLE_NAMES IN ALL-CAPS ARE CONSTANTS ARE NOT MEANT TO CHANGE!
HANGMAN_BOARD =['''
    +---+
        |
        |
        |
    ======''','''
    +---+
    O       |
        |
        |
    ======''','''
    +---+
        |
        |
        |
    ======''','''
    +---+
    O       |
   /|       |
        |
    ======''','''
    +---+
        |
        |
        |
    ======''','''
    +---+
    O       |
   /|\   |
        |
    ======''','''
    +---+
        |
        |
        |
    ======''','''
    +---+
    O       |
   /|\    |
  /    |
    ======''',] 

i = 0 
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1