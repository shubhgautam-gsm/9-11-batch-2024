# Encapsulation Example
class Vehicle:
    def __init__(self, price, model):
        self._price = price  # Encapsulated attribute
        self._model = model  # Encapsulated attribute

    def start(self):
        pass  # Implementation omitted for brevity

    def stop(self):
        pass  # Implementation omitted for brevity

    def get_price(self):  # Getter method
        return self._price

    def get_model(self):  # Getter method
        return self._model

# Usage of Encapsulation

vehicle = Vehicle("20000$", "i20")
print("Price:", vehicle.get_price())  # Output: Make: Toyota
print("Model:", vehicle.get_model())  # Output: Model: Camry
