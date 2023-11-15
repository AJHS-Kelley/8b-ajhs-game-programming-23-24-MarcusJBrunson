# Example Game Functions Project, Marcus Brunson, v0.0
import random
# DECLARATIOINS
playername = ""
playerHealth = 200
cpuHealth = 100
difficulty = ""
playerScore = 0
cpuScore = 0

def functionOne(difficulty):
    difficulty = input("Type Easy, medium, or Hard as your difficiulty \n")
    if difficulty == "Easy":
        print("You have selected Easy as your difficulty") 
       
    elif difficulty == "Medium":
        print("You have selected Medium as your difficulty") 
    
    
    elif difficulty == "Hard":
        print("You have selected Hard as your difficulty")
         
        

         


def functionTwo(comboHit):
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

    
        
