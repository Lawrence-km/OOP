class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
        
    def __str__(self):
        return self.name

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying! 🕊️"
        
class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming! 🐟"
        
class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering! 🐍"
        
class Kangaroo(Animal):
    def move(self):
        return f"{self.name} is hopping! 🦘"

# Vehicle polymorphism example
class Vehicle:
    def __init__(self, model):
        self.model = model
        
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
        
    def __str__(self):
        return self.model

class Car(Vehicle):
    def move(self):
        return f"{self.model} is driving on the road! 🚗"
        
class Boat(Vehicle):
    def move(self):
        return f"{self.model} is sailing on water! ⛵"
        
class Airplane(Vehicle):
    def move(self):
        return f"{self.model} is flying through the air! ✈️"
        
class Helicopter(Vehicle):
    def move(self):
        return f"{self.model} is hovering in the sky! 🚁"

if __name__ == "__main__":
    print("\n=== Animal Polymorphism Example ===")
    animals = [
        Bird("Pigeon"),
        Fish("Salmon"),
        Snake("Python"),
        Kangaroo("Joey")
    ]
    
    for animal in animals:
        print(animal.move())
    
    print("\n=== Vehicle Polymorphism Example ===")
    vehicles = [
        Car("Toyota Camry"),
        Boat("Speedboat"),
        Airplane("Boeing 747"),
        Helicopter("Apache")
    ]
    
    for vehicle in vehicles:
        print(vehicle.move())
