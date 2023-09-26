# cONTOL FLOW mRCUS bRUNSON, VO.O 
# dECLARATIONS 

fav color = "blue" 
luckynumber = 55 
myGPA = 3.5 
myage = 16 
pineappleOnPizza = False 

# If Statments - Check for a condition to be True/False
if favColor == "Green": 
    print("I like your style.") 

if favgame == mortalKombat


# if else statment -- Check condition, do something fro True and False 
if myGPA >= 3.0: 
    print("Congratulations on making the honor roll!") 
else: 
    print("Better luck next year.") 

if myage >= 18: 
    print("Your not a child.") 
else: 
    print("Your still a child.") 

# if - elif - else statments
if myage > 65: 
    print("Congratulations on retiring!") 
    elif myage > 50: 
    print("Congratulations you have earned a bonus of $1000"!) 
    else: 
        print("You are not old enough for a bouns.") 
# 1 if, 1 else, any number of elif allowed. 

# Nested if - elif - else Statements 
if myage > 15: 
    print("You are eligible for a license!") 
    if myGPA >= 3.5: 
        print("You quality for a new car!") 
    elif myGPA > 2.0: 
        print("You quality for $500 off a car!") 
    else: 
        print("You get nothing!") 
    else: 
        print("You are not yet old enough to drive.") 

# When doing if - elif - else statments, check for the highest value first!!!! 
if myGPA > 1.5: 
    print("You are in danger of failing for the year.") 
    elif myGPA > 2.0: 
        print("You are on tract to graduate.") 
    elif myGPA > 3.0: 
        print("You qualify for some scholarship money!") 
    elif myGPA > 3.99: 
        print("You quality for Bright Futures 100 percent scholarship!") 
    else: 
        print("GPA was not calculated. Please try again.") 

# While loop -- Think "Muscial CHAIRS" -- 
# Iteration == one complete trip through a loop 
x = 0
while x < 100: 
    print(f"X is currently equal to {x}") 
    x += 1


    # () Parentheses 
    # [] Square Brackets 
    # <> Angle Brackets 
    # {} Braces 

x = 0
while x < 100: 
    print(f"X is currently equal to {x}") 
    x += 11 

While x > 0:
    print(f"X is currently equal to {x}") 
    x-=1 

# for loop -- Think 'Go Fish' , used when you number of iterations needed. 
print("For LOOP STARTS HERE")
for i in range(10): # i == iterable variable 
    print(i) 

print("EVEN OR ODD LOOP")
for i range(101): 
    print(i) 
    if i % 2 == 0: 
    print("That number is even")
    else:
    print("That number is odd!") 