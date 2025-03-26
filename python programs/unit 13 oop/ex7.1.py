class Employee:
    # Parameterized Constructor

    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID:", self.id,"\nName:", self.name) #using this int on id string on name not number

# Creating instances and calling methods
emp1 = Employee("John", "abraham")
emp2 = Employee("David", 102.2)
emp1.display()
emp2.display()
