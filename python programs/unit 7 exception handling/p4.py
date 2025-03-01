try:
    a =int(input("Enter a: ")) #integer
    b = input("Enter b: ") #string
    c = a / b
    print("a / b = %d" % c)
except ValueError:
    print("Please enter valid integers for 'a' and 'b'.")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as errr:
    print("An unexpected error occurred:", errr)
else:
    print("Hi, I am the else block")
