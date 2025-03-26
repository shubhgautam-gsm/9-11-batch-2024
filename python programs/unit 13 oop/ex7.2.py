class Employee:
    # Parameterized Constructor
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        # Check if the name is a number (string representation of a number)
        if self.name.isdigit():
            print('Name is not a string')
        else:
            # Using string formatting to display ID and Name
            print("ID: %d \nName: %s" % (self.id, self.name))
            

name=input('GIVE NAME:')
id=int(input('GIVE ID:'))

# Creating instances with correct parameter order (name first, then id)
emp1 = Employee(name, id)  # Name as string and ID as number

name=input('GIVE NAME:')
id=int(input('GIVE ID:'))

emp2 = Employee(name, id)  # Name as string (numeric characters) and ID as float

# Calling display methods
emp1.display()
emp2.display()
