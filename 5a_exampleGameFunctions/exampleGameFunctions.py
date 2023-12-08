# Example Game Functions Project, Marcus Brunson, v0.0
import random
# DECLARATIOINS
playerName = ""
opponentName = ""
playerHealth = 100
opponentHealth = 100
difficulty = ""
playerScore = 0
opponentScore = 0

def fight(difficulty):
    difficulty = input("Type Easy, Medium, or Hard as your difficiulty \n")
    playerHealth = 100 
    opponentHealth = 100 

    while playerHealth > 0 and opponentHealth > 0:
         # Player's turn
         playerattackDamage = random.randint(10,20) * difficulty    c
         opponentHealth -= playerattackDamage

         if opponentHealth <= 0:
              print("You win!")
              playerScore += 1
              break
         
         # Opponent's turn 
         opponentattackDamage = random.randint(5,15) * difficulty
         playerHealth -= opponentattackDamage

         if playerHealth <= 0:
              print("You lose!")
              opponentHealth += 1
              break
         
         print("Game over")
              

def specialAttack(playerName, opponentName, playerHealth):
    if playerHealth <= 30:
        specialAttack = True
        print(f"{playerName} unleashes a devasting special attack on {opponentName} and deals 50 damage!")
    elif playerHealth > 30:
        specialAttack = False
        print(f"{playerName} is unable to unleash a special attack on {opponentName}")
        return specialAttack 


specialAttack("Ryan", "Marcus", 30)

# Please Finish This Function.
def defend(player):
    playerDefense += 5
    print(f"{playerName} takes a defensive stance, increasing their defense by 5!")

# Please Finish This Function.
def attack(playerName, opponentHealth, damage):
        opponentHealth != 100
        print(f"{playerName} attacks {opponentHealth} and deals {damage}")

# PLEASE MAKE SURE TO CALL AND TEST THE FUNCTIONS. 















# Code Review by Trevis Brown