# Parent class
class Animal:
    def speak(self):
        print("Animal Sounds")

# Child class inheriting from Animal
class Dog(Animal):
    
    # def speak(self):
    #     print("Animal Speaking")

    def bark(self):
        print("Dog Barking")

dog = Dog()
dog.bark()  # Output: Dog Barking
dog.speak() # Output: Animal Speaking
