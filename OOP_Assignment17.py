"""17. Class Decorators
Assignment:
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!".
Apply it to a class Person."""

def add_greeting(class_person):
    def greet(s):
        return "Hello from decorator"
    class_person.greet = greet
    return class_person

@add_greeting
class Person:
    def __init__(self):
        print("i am person")

person1 = Person()
print(person1.greet())