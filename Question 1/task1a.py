
class Vehicle: 
    def __init__(self, make):
        self.make = make
        
class Wheeled(Vehicle):
    def __init__(self, make, wheels):
        super().__init__(make)
        self.wheels = wheels
       
class Motorised(Vehicle):
    def __init__(self, make, typeOfEngine):
        super().__init__(make)
        self.typeOfEngine = typeOfEngine
        
class Aircraft(Vehicle):
    def __init__(self, make, wheels, typeOfEngine):
        super().__init__(make)
        self.typeOfEngine = typeOfEngine
        self.wheels = wheels
        
    def takeOff(self):
        print(f"Make: {self.make}, Wheels: {self.wheels}, Engine Type: {self.typeOfEngine}")     
