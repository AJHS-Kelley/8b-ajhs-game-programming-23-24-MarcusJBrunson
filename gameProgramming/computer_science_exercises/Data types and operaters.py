#Data Types and Operaters, Marcus Brunson, v0.5
# Variables Rules 
#CANNOT START WITH A NUMBER !!!!!!!!! 
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES. 
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORTED. 
# Snake_case variables use _ to separate words, all lower case. 
# camelCase variables do not use spaces, 1st word lower, rest upp 
# String Literal Examples 
playername = "Black Prince" 
emptyString = "" 
spacestring = " " 
monsterName = "Purple People Eater"

#Interger Data Types 
health = 100 
extraLives = 5 
temperature = -17 
people = 3

#floating points data types
pi = 3.1415678 
lapTime =3.5 
velocity = -2.0

# Boolean Data Types 
isFireType = False
weaponEquipped = True 
pvpEnabled = False
isWaterType = True 

# Arithmetic Operaters 
# PEMDAS APPLIES JUST LIKE IN MATH CLASS 
print(7 + -3) #addition 
print(65 - 25) #Subtraction
print(5 * -5) #Multiplication
print(100 / -10) #Division 
print(3 ** 3) #Exponents
print(10 % 5) #Modulus -- Divides, then returns remainder, mostly commoly used to determine even/odd 

# Comparison operators 
#Evaluate the expression then return True or False 
print (5 > 3) #Greater Than 
print (7 >= -1) #Greater Than or Equal to 
print # Less Than 
print (0<= 0) 
print (5 == 3) # Is Equal To 
print (-99 != 99) # Not equal To 

# Assignment Operators 
myVariable = "my value" # Assign varaiable on left the value on the right, throw out any current value 
myOthervariable = (10 + 5) 

myVariableAgain= 1 
myVariableAgain= 5 
print(myVariableAgain) 

# Addition Assignment -- Add the value on the right, keeping any current value
myWallet = 0 
myWallet += 1 
myWallet += 5 
print(myWallet) 

# Same Effect 
x += 1 
x += 1 
x = x + 1 

# Logical Operaters 
print(3 > 5) and (4 < 3) # AND requires ALL expresions to be True. 
print(3 > 2 and 4 < 3) 
print(3 > 2 and 4!= 3) 
print(3 > 2 and 4!= 3 and favcolor == "Blue" and temperature == -5) 
# When writing and ecpressions, put the value most likely to be false first! 

# Logical OR -- Requires ONE to be True.
print(5 > 2 or 2 < -2) 
print(3 != 3 or 5 == 5) 

# AND OR Combined 
print("Line 81" )
print(3 > 2 and 4 < 3 or 5 != 7) 
# print(True and False or True) 


print(not  3 > 2) 
print(not (not (not (5 != 3 )))) 

