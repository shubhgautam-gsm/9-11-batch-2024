fileptr = open("file1.txt","r")

try:
    # Read and print data from the file while it's open
    data = list(fileptr)
    print("Data from file:", data)
finally:
    # The file is not being closed here, so data is still accessible
    print("Data from file again in finally block:", data)
print("Data from file again in finally block:", data)
