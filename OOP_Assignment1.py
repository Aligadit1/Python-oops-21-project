""""1. Using self
Assignment:
Create a class Student with attributes name and marks. 
Use the self keyword to initialize these values via a constructor.
 Add a method display() that prints student details."""

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def detail(self):
        print(f"{self.name} has obtained {self.marks} marks")

std1 = Student("Ali",100)            
std1.detail()