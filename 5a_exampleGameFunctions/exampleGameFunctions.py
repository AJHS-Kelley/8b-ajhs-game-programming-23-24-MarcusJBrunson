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
    difficulty = input("Type Easy, medium, or Hard as your difficiulty \n")
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
        

         


def specialAttack(player, opponent):
    if playerHealth <= 50:
        specialAttack = True
        print("player unleashes a devasting special attack on the opponent and deales 50 damage!")


def defend(player = "Default Value"):
    print(player)

    def attack(player, opponent, damage):
        pass

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

    
        
