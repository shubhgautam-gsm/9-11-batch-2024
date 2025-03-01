try:
#  a=10/0
#  a=int(input('Enter a number'))
#  fileptr = open("file2.txt","r")
 fileptr = open("file3.txt","r")
except Exception as e:
 print('FOR FILE ',e)
else:
 print("Successfully Done")
