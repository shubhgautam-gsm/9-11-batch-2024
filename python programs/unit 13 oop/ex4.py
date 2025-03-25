class Person:
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

# Creating an instance of Person without __init__ method
person = Person()

# Setting attributes without using __init__
person.set_name("John")
# person={name:'john'} obj
person.set_age(30)
# person=
# {
    # name:'john',
    # age:30
# } obj

# Accessing attributes
print(person.name)  # Output: John
print(person.age)   # Output: 30
