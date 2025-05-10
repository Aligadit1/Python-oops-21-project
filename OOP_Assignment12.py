"""12. Static Methods
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

"""

class TemperatureConverter:
    def celcsius_to_fahrenhit(self,celsius):
        f = (celsius * 9/5) + 32
        return f 
temperature_converter = TemperatureConverter()    
print(temperature_converter.celcsius_to_fahrenhit(10))