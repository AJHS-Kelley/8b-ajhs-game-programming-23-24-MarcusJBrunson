# Example Game Functions Project, Marcus Brunson, v0.0
import random
# DECLARATIOINS
playername = ""
playerHealth = 100
CPUHealth = 100
difficulty = ""
Damage = 

def functionOne(difficulty):
    if difficulty == "Easy":
        print("You have selected Easy as your difficulty")


def functionTwo(param1):
    pass

def functionThree(param1 = "Default Value"):
    print(param1)

    def functionFour(param1, param2, param3):
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

    
        
