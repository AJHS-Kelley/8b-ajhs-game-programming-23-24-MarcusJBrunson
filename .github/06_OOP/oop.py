# Object-Oriented prgramming, Marcus Brunson, v0.0 

class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name 
        self.age = age 
        self.weight = weight
        self.weakness = None
        self.nemsis = None

    # To string Function -- How the object appears as a string
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds.\n"

    def classfunction(self):
        print("This is an example class function")
        print("It only works when called on an object of that class.")

person1 = Person("Eren Yeager", 19, 140)
person2 = Person("Gojo", 22, 160)
# print(person1)
# print(person2)

# if person1.weight > person2.weight:
#     print("f{person1.name} weighs more than {person2.name}.")
# elif person1.weight == person2.weight:
#     print("Each person weighs the same.\n")
# else: 
#     print(f"{person2.name} weighs more than {person1.name}")

# if person1.age > person2.age:
#     print("f{person1.name} is older than {person2.name}.")
# elif person1.age == person2.age:
#     print("Each person is the same age.\n")
# else: 
#     print(f"{person2.name} is older than {person1.name}")

# person1.classfunction()

# Changing properties After Creation
print(person1.name)
person1.name = "Eren Yeager"
print(person1.name) 

# Deleting Properties -- Danger Will Robinson, Danger!
# THIS DOES BOT 'RESET' A PROPERTY, IT DELETS IT COMPLETELY
print(person1.name)
del person1.name
# print(person1)

# Deleting objects -- Delete them if your done with them.
del person1

# Adding Properties to Objects -- USE CAREFULLY
person2.weakness = "Kryptonite"
print(person2)
print(person2.weakness)