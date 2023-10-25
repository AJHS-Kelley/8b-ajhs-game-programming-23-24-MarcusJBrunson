import random
# FUNCTION -- a named piece of code that can be reused easily. 
# FUNCTION SIGNATURE -- Syntax for creating a new function.
def exampleFunctionA():
    count = 0
    num = int(input("How many times do you want to wish happy birthday?\n"))
    while count < num: 
        print("Happy Birthday!\n") 
        count +=1

def exampleFunctionB(num, count): # PARAMETERS 
    while count < num: 
        print("Happy Birthday!\n") 
        count +=1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM! 

# RUNNING A FUNCTION IS KNOWN AS CALLING THE FUNCTION! 
# exampleFunctionA()
# exampleFunctionB(5, 0)

def rollDice(numDice, sizeDice):
   numRolled = 0
   sum = 0
   while numRolled < numDice: 
        roll = random.randint(1, sizeDice)
        sum += roll
        print(f"Roll: {roll}\n")
        print(f"Sum: {sum}\n")
        numRolled += 1
        return sum # reutrn will IMMEDIATELY exit a loop, function, if/elif/else block.
rollDice(3, 6)
rollDice(1, 20) 


strengthPlayer = rollDice(3, 6)
dexterPlayer = rollDice(3, 6)
wisdomPlayer = rollDice(3, 6) 

print(strengthPlayer) 
print(dexterPlayer) 
print(wisdomPlayer) 

def genStats():
    playerStats = [ 0, 
        0, # STRENGTH
        0,  # DEXTERITY 
        0, # CONSTITUTION
        0,  # INTELLIGENCE
        0,  # WISDOM
        0  # DEXTERITY 
    ]
    i = 0 
    while i < len(playerStats):

        playerStats [i] = rollDice(3, 6) 
        i += 1
        
    
    print(playerStats) 

genStats() 
 