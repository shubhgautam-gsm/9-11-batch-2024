class Employee: #model
#  id = 10  #static
#  name = "John" #static
 
 def display (self,id,name):
  print("ID:",self.id,"\nName:",self.name)

emp = Employee()
# emp={}


emp.display(12,'john')
# emp={
    #   "id":12,
    #   "name":"john"
# }
# emp.display()