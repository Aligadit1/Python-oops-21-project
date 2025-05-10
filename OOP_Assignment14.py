"""14. Aggregation
Assignment:
Create a class Department and a class Employee. 
Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
"""
class Employee:
    def __init__(self,name):
        self.name = name
    def info(self):
        print(f"Name of employee is {self.name}")    
class Department:
    def __init__(self,deparment,employee):
        self.department = deparment
        self.employee = employee
    def details(self):
        print(f"{self.employee.name} is working in {self.department} department") 

employee1 = Employee("Ali")
department1 = Department("K.Electric",employee1)
department1.details()