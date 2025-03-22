import os

# Create a file
with open("python22.txt", "r") as file:
    file.read()
    
print(file)
# Change the permissions to deny read and write access for everyone
# os.chmod("Pytho1.txt", 0o000)

# Check if the file is readable
if os.access("python22.txt", os.R_OK):
    print("You have read permission for 'python22.txt'.")
else:
    print("You do not have read permission for 'python22.txt'.")

# Check if the file is writable
if os.access("python22.txt", os.W_OK):
    print("You have write permission for 'python22.txt'.")
else:
    print("You do not have write permission for 'python22.txt'.")
