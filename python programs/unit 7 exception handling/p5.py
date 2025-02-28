try:
#  a=10/0
#  a=int(input('Enter a number'))
 fileptr = open("file2.txt","r")
except( IOError):
 print("Arithmetic Exception")
else:
 print("Successfully Done")
