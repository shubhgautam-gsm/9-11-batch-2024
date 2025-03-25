class MyClass:
    def __init__(self, a, b, c, d, e): # _init_ method calls automatically   (see ex1.3)
        
        self.c = a + b
        self.d = a * b
        self.e = a / b
        

# Creating an instance of MyClass
# obj={}
obj = MyClass(5,10,None,None,None)

# obj={ c:12.0 ,d:20.0,e:0.5 } first obj   key :value

print(obj.e)  # Output: Result of division
