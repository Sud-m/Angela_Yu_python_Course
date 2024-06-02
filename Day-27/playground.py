def add(*args):
    return sum([arg for arg in args])

print(add(1, 2, 3, 4, 5, 6))


def calculate(n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2, add = 3, multiply = 5))

class Car:
    
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")
        
        
car = Car(make = "Nissan", model = "GTR", color = "Black", seats = 2)
print(car.make, car.model, car.color, car.seats)