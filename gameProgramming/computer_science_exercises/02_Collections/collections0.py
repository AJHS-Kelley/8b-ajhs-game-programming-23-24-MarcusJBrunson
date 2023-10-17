# playerInventory = [] 

# while len(playerInventory) < 10: 
#     item = input("What item do you want to add to the inventory?\n") 
#     playerInventory.append(item)

# playerInventory.sort()
# print(playerInventory) 

# while len(playerInventory) > 5: 
#     item = input("What item do you want to remove to the inventory?\n") 
#     playerInventory.remove(item) 

# playerInventory.sort()
# print(playerInventory) 

# doorKeys = [
# "red", 
# "green", 
# "yellow", 
# "purple", 
# "brown"
# ]

# key = input("Which color key do you need to unlock the door?\n") 

# if key in doorKeys: 
#     print("You have the correct key! The door unlocks.\n") 
# else: 
#     print("You do not have that key. The door remains locked.\n") 

weaponList = [
    True, # sword
    False, # laser blaster
    False, # flame thrower 
    False, # Ak-47 
    True, # grappling hook
    False, # missle launcher
    True, # lightsaber
] 

weaponNumber = 0 
while weaponNumber < len(weaponList): 
    if weaponNumber == 0 and weaponList[0] == True: 
        print("You are wielding a shiny sword.\n") 
    if weaponNumber == 1 and weaponList[1] == True 
        print("You have a laser blaster") 
    if weaponNumber == 2 and weaponList[2] == True 
        print("You are wielding a flame thrower.\n") 
    if weaponNumber == 3 and weaponList[3] == True: 
        print("You are wielding a Ak-47.\n") 
    if weaponNumber == 4 and weaponList[4] == True: 
        print("You are wielding a grappling hook.\n")
    if weaponNumber == 5 and weaponList[5] == True: 
        print("You are wielding a missle launcher.\n") 
    if weaponNumber == 6 and weaponList[6] == True: 
        print("You are wielding a lightsaber.\n") 
    weaponNumber += 1 