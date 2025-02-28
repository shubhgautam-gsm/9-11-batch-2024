try:
    a =float(input("Enter a: "))
    b = (input("Enter b: "))
    c = a / b
    print("a / b = %f" % c)

except Exception as e:
    print(e)
else:
    print("Hi, I am the else block")
