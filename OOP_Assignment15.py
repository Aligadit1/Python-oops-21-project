"""15. Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO."""

class A:
    def show(self):
        print("I am method A")
        
class B(A):
    def show(self):
        print("I am method B")
class C(A):
    def show(self):
        print("I am method C")
# this is called diamond inheritence 
class D(B,C):
    pass

d = D()
# the method b will be called because MRO is designed by an algorithm which will first check the method in d 
# if not found it will move to the first parameter of D means b if it found in b it will called otherwise it will again move 
 
d.show()
# the mro method only operates with class name 
print(D.__mro__)