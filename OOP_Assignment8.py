"""8. The super() Function
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it,"
add a subject field, and use super() to call the base class constructor."""

class Person:
    def __init__(self,name):
        self.name = name
class Teacher(Person):
    def __init__(self,name,subject):
        self.subject = subject
        super().__init__(name)
# changing str method to makea the print readable
    def __str__(self):
        return f"{self.name} teaches {self.subject}"    
teacher = Teacher("Arif","Python")         
print(teacher)       