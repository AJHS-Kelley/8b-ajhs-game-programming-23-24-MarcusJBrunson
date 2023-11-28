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

def functionOne(difficulty):
    difficulty = input("Type Easy, Medium, or Hard as your difficiulty \n")
    if difficulty == "Easy":
        print("You have selected Easy as your difficulty") 
        playerHealth = 100
        opponentHealth = 75
    elif difficulty == "Medium":
        print("You have selected Medium as your difficulty") 
        playerHealth
        opponentHealth
    elif difficulty == "Hard":
        print("You have selected Hard as your difficulty")
        playerHealth
        opponentHealth


def specialAttack(playerName, opponentName, playerHealth):
    if playerHealth <= 30:
        specialAttack = True
        print(f"{playerName} unleashes a devasting special attack on {opponentName} and deals 50 damage!")
    elif playerHealth > 30:
        specialAttack = False
        print(f"{playerName} is unable to unleash a special attack on {opponentName}")
    return specialAttack 

def defend(player = "Default Value"):
    print(player)

def attack(playerName, opponentHealth, damage):
        opponentHealth != 100
        print(f"{playerName} attacks {opponentHealth} and deals {damage}")

if playerHealth == 0:
     print("Yo, you lost")
     opponentScore += 1
else: 
    opponentHealth == 0
    print("Winner, Winner, chicken dinner!")
    playerScore += 1

def catchBall(throwQuality, passCatcherScore, weather):
    if throwQuality > 5.0 and passCatcherScore >= 99 and weather == 'Sunny':
            ballcaught = True
    elif throwQuality > 4.0 and passCatcherScore >= 75 and weather == 'Windy':
            ballcaught = False
    else:
            print('oh, no, interception!\n')
            ballIntercepted = True
    return ballcaught
    
    catchBall(4.25, 107, 'Rainy')