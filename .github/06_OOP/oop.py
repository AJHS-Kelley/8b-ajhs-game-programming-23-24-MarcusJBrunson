# Object-Oriented prgramming, Marcus Brunson, v0.0 

class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name 
        self.age = age 
        self.weight = weight

    # To string Function -- How the object appears as a string
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds.\n"



person1 = Person("Eren Yeager", 19, 140)
print(person1)