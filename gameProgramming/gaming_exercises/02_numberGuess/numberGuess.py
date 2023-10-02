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
playerName = "Marcus"
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
# REMOVE THIS LOOP, IT WAS ONLY USED TO TEST THE SECRET NUMBER GENERATION. 
# x = 0
# while x < 50:
#     sercetNumber = random.randint(0,20) 
#     print(sercetNumber) 
#     x += 1 # This line of code is not in the scope of the while loop.  This creates an infinite loop. 
# The fact that you have an infinite loop at the start of your program indicates it was not tested.

# Game Loop 
print("Select between a difficulty of Easy, Medium, Hard")  
# NO CODE TO ALLOW PLAYER TO SELECT DIFFICULTY. 
difficulty = input("Blah blah blah.\n") # Add code here to get difficulty.  
Easy = 1
Medium = 2 
Hard = 3
if difficulty == Easy:
    print("You have selected Easy as your difficulty") 
    print("You need to guess a number from 0 to 10 and you have three guesses. \n If you guess it right, you get a point, If you guess it wrong the CPU gets a point")     
    numAttempts = 3
    rangeMin = 0 
    rangeMax = 10
    sercetNumber = random.randint(rangeMin,rangeMax) 
elif difficulty == Medium:
    sercetNumber = random.randint(rangeMin,rangeMax) 
    numAttempts = 2
    rangeMin = 0 
    rangeMax = 30 
elif difficulty == Hard:
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
    print(f"Player Score: {playerScore} cpuScore: {cpuScore};\n") 
    sercetNumber = random.randint(rangeMin,rangeMax) # THIS LINE OVERRIDES THE THE secretNumber = random.randint(rangeMin, rangeMax) CODE EARLIER.  REMOVE THE EARLIER CODE.
# Whenever you assign a specific value to something, it's called "hard coded".
    # print(sercetNumber)
     
    
    
    numGuesses = 0
    for guesses in range(4): # START THE ROUND! UPDATE TO USE THE NUM. ATTEMPTS VARIABLE. 
    # Put Difficulty CODE 
        print(f"You have {4 - numGuesses} guesses remaining,\n") # UPDATE TO USE THE NUM. ATTEMPTS VARIABLE. 
        playerGuess = int(input("Type a number from 0 to 20 and press ENTER,\n")) # YOU NEED TO USE THE int() CODE.  
    # input() saves all data as a string by default. 
    # int() will covert to a INTEGER     
    # float() will convet to a FLOAT 
        print(f"You have chosen {playerGuess}, Let's see if your right!\n") 
        if playerGuess == sercetNumber: 
            print("Whoa dude, what a guess! You got it!\n") 
            playerScore += 1 
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
    print("Yo, you lost to a computer")  
