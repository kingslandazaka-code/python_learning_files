
# 14. Basic OOP
# Define a class named Person
# A class is a blueprint (template) for creating objects
# Think of it like a form — every Person object will follow this structure
class Person:

    # __init__ is a special method called a CONSTRUCTOR
    # It runs AUTOMATICALLY every time a new object is created from the class
    # self refers to the CURRENT object being created
    # name and age are parameters that will be passed when creating the object
    def __init__(self, name, age):

        # self.name creates an attribute called 'name' for this object
        # The value of 'name' comes from the argument passed during object creation
        # Each object will have its OWN copy of self.name
        self.name = name

        # self.age creates another attribute called 'age' for this object
        # This stores the age of the person inside the object
        self.age = age


    # Define a method called greet
    # A method is just a function that BELONGS to a class
    # self allows the method to access the object's data (attributes)
    def greet(self):

        # This prints a greeting message
        # f-string allows us to insert the value of self.name into the string
        # self.name refers to the name stored inside THIS specific object
        print(f"Hi, I'm {self.name}")


# Create an object (instance) of the Person class
# Person("Kingsland", 21) calls the __init__ method automatically
# "Kingsland" is assigned to self.name
# 21 is assigned to self.age
p = Person("Kingsland", 21)

# Call the greet method on the object p
# Python automatically passes 'p' as the self argument
# This prints the greeting using the object's name
p.greet()

