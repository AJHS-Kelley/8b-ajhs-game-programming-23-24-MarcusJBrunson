# collections Examples, Marcus Brunson, v0.2a

# LIST -- ORDERED, CHANGEABLE, ALLOWS DUPLICATE VALUES 
breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk"] 
# each item on the list is known as an ELEMENT 
# The position in the list for each ois the INDEX. 
# The element "BACON" is a index 0. 
# Python Only: index -1 is the last item on the list. 
testScores= [95, 100, 25, 15, 27, 35] 
classGPA= [3.14, 2.25, 1.74, 1.99, 0.99, 4,25] 


# Printing Contents of an List 
#print(breakfastFoods) 
#print(testScores)
#print(classGPA) 

# Accessing Specific List Elements -- REMEMBER FIRST ELEMENTS IS INDEX 0  
#print(breakfastFoods[0]) 
#print(testScores[0]) 
#print(classGPA[0]) 

# Accessing Last Element in Lists
#print(breakfastFoods[-1]) 
#print(testScores[-1]) 
#print(classGPA[-1]) 


#print(breakfastFoods[2])
#print(testScores[2]) 
#print(classGPA[2]) 

# Changing items in a List 
#breakfastFoods[0] = "Sausage" 
#testScores[0] = 97 
#classGPA[0] = 3.57 
#print(breakfastFoods[0]) 
#print(testScores[0])
#print(classGPA [0])
#print(breakfastFoods) 
#print(testScores)
#print(classGPA) 

#breakfastFoods[4] = "Eggs" 
#testScores[4] = 50 
#classGPA = 2.54
#print(breakfastFoods) 
#print(testScores)
#print(classGPA) 

# Adding and Inserting Items to a List 
# .append() adds an item to the END of a list. 
breakfastFoods.append("hash browns") 
print(breakfastFoods) 
testScores.append(99) 
print(testScores) 
classGPA.append(1.99) 
print(classGPA) 

# .inset() allows you to place an item at a specific index in the list.
breakfastFoods.insert(3, "Parfait") 
print(breakfastFoods) 
testScores.insert(3, 55) 
print(testScores) 
classGPA.insert(3, 0.0) 
print(classGPA) 


breakfastFoods.append("Toast") 
print(breakfastFoods) 
testScores.append(88) 
print(testScores) 
classGPA.append(2.99) 
print(classGPA) 

 
