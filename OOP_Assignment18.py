"""18. Property Decorators: @property, @setter, and @deleter
Assignment:
Create a class Product with a private attribute _price. Use @property to get the price,
@price.setter to update it, and @price.deleter to delete it."""

class Product :
    def __init__(self,_price):
        self._price = _price
    @property
    def price(self):
        print(self._price)    
        print("get")            
    @price.setter
    def price(self,value):
        self._price = value
        print("change")
    @price.deleter
    def price(self):
        del self._price      
        print("delete")  

p1 = Product(250)
print(p1.price)        
p1.price = 1000
print(p1._price)
del p1.price
