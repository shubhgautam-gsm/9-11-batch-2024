class Calculation1:
    def Summation(self, a, b):
        return a + b

class Calculation2:
    def Multiplication(self, a, b):
        return a * b

class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b

# Create an instance of Derived class
d = Derived()

# Check if d is an instance of Derived class
print(isinstance(d, Calculation1))  # Output: True


# tata=5
# reliance=5
# abani is tata x