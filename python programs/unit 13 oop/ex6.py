class Employee:
 id = 10  #static
 name = "John" #static
 def display (self):
  print("ID:",self.id,"\nName:",self.name)


emp = Employee()
emp.display()