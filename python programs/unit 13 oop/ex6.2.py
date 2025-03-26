class Employee: #model
#  id = 10  #static
#  name = "John" #static
 def display (self,id,name):
  self.id = id
  self.name = name
  print("ID:",self.id,"\nName:",self.name)  

emp = Employee()
# emp={}

id=int(input('GIVE ID:'))
name=input('GIVE NAME:')
emp.display(id,name)
# emp={
    #   "id":12,
    #   "name":"john"
# }
# emp.display()