class Employee:
    __count = 0  # Private class variable to count the number of employees

    def __init__(self):
        Employee.__count += 1
        print("The number of employees:", Employee.__count)

emp = Employee()
emp2 = Employee()

try:
    print(emp._Employee__count)  # Accessing the private variable correctly( name-mangled )
except AttributeError:
    print("Cannot access __count directly!")
finally:
    pass
