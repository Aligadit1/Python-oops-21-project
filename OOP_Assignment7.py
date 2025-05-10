"""7. Access Modifiers: Public, Private, and Protected
Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens."""

class Employee:
    def __init__(self):
        self.name = "Ali"
        self._salary = "150k"
        self.__ssn = 1234
employee = Employee()
print(f"Public name : {employee.name}") 
print(f"Protected salary {employee._salary}") 
try:
    print(f"Private ssn :{employee.__ssn}") 
except AttributeError as e:
    print("Private __ssn : Access denied - ",e)    

"""the error will show that attribute not found becuase python changes the name of private attributes called name-mangling
we can access it like this"""

print("Accessing private attribute through name mangling",f"Private __ssn : {employee._Employee__ssn}")