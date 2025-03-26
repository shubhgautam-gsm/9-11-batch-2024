class Employee: #model
#  id = 10  #static
#  name = "John" #static

 def __init__(self,id,name):
  self.id = id
  self.name = name
  
 def display (self):
  print("ID:",self.id,"\nName:",self.name)  



id=int(input('GIVE ID:'))
name=input('GIVE NAME:')
emp = Employee(id,name)

emp.display()
