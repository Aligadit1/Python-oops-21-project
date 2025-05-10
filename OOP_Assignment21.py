"""21. Make a Custom Class Iterable
Assignment:
Create a class Countdown that takes a start number.
Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0."""

class Countdown:
    def __init__(self,st_num):
        self.st_num = st_num

    def __iter__(self):
        return self    
    def __next__(self):
        if self.st_num < 0:
            raise StopIteration
        value = self.st_num
        self.st_num -= 1
        return value
    
for num in Countdown(10):
    print(num)
