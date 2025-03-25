# Abstraction Example



class Vehicle(): #vehicles i.e plane ,car ,bike so we cant print 
# THAT CAR IS STARTED OR AIRPLANE IS STARTED..  

    def start(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Plane(Vehicle):
    def start(self):
        print("Plane is starting")




# Usage of Abstraction

car = Car() #class
car.start()  # Output: Car is starting

plane = Plane()
plane.start()  # Output: Plane is starting

