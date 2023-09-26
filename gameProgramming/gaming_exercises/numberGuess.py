# Select the sercet number from a given range. 
# Player must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong? 
    # Tell them the guess is wrong. 
    # Tell them the number of guess left. 
    # Tell if too high / too low. 
# What happens if the guess is right? 
    # Tell them guess is right. 
    # Award a point. 
# What happens if the player runs out of guesses? 
    # Tell player round has been lost. 
    # Award point to CPU. 
# Check to see if player or CPU has >= 3 points, if so they win. 
import random # import te random module to our code. 

# DECLARATIOINS 
sercetNumber = -1 # Range: 0 -- 20
playerName = "" # empty string 
playerScore = 0
cpuScore = 0
numGuesses = 0 
playerGuess = -1
difficulty = "" 
rangeMin = -1 
rangeMax = -1 
numAttempts = -1
print(""" 
        +====================+ 
        |                    |
        |   Guess a number   |
        |   Marcus Brunson   |
        |        2023        |
        +====================+
     """) 

# CPU SECRET NUBER GENERATION 
x = 0
while x < 50:
    sercetNumber = random.randint(0,20) 
print(sercetNumber) 
x += 1

# Game Loop 
print("You need to guess a number from 0 to 20 and you have four guesses. \n If you guess it right, you get a point, If you guess it wrong the CPU gets a point") 
print("Select between a difficulty of easy, hard, godTier") 
if difficulty = godTier
sercetNumber = random.randint(rangeMin,rangeMax) 
numAttempts = 2 
rangeMin = 0 
rangeMax = 100
# ADD CODE HERE TO CHANGE BETWEEN EACH MATCH 
# PRINT () an explanation of your three difficulty levels. 
# Use input () to store difficulty in difficulty variable. 
# assign values to numAttempts, rangeMin, and rangeMax based on choice
while playerScore != 3 and cpuScore != 3: # Start THE MATCH (GAME)
    # Difficulty code need to be BEFORE the round starts.
    # pass -- Tells PYTHON to skip this block of code 
    print(f"Player Score: {playerScore}");cpuScore: {cpuScore};\n 
    sercetNumber = random.randint(rangeMin,rangeMax) 
# Whenever you assign a specific value to something, it's called "hard coded".
    # print(sercetNumber)
     
    
    
    numGuesses = 0
for guesses in range(4): # START THE ROUND! 
    # Put Difficulty CODE 
    print(f"You have {4 - numGuesses} guesses remaining,\n")
    playerGuess = input("Type a number from 0 to 20 and press ENTER,\n") 
    # input() saves all data as a string by default. 
    # int() will covert to a INTEGER     
    # float() will convet to a FLOAT 
    print(f"You have chosen {playerGuess}, Let's see if your right!\n") 
    if playerGuess == sercetNumber: 
    print("Whoa dude, what a guess! You got it!\n") 
    playerScore += 1 
    break # IMMEDATELY EXIT ANY LOOP YOU ARE IN!
else: 
    print("You did not guess correctly,\n") 
    if playerGuess > sercetNumber: 
        print("Your guess is too high,\n") 
    else: 
        print("Your guess is too low,\n") 
    numGuesses += 1 
    if playerGuess != sercetNumber: 
        cpuScore += 1
        print("The cpu wins a point since you ran out of guesses")
if playerScore >= 3:
    print("Winner, Winner, chicken dinner! You scored 3 points first!\n") 
else:
    print("Yo, you lost to a computer, ") 
