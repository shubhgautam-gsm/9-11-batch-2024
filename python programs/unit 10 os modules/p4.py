import os

# Print the current working directory before changing
print("Current Working Directory before change:", os.getcwd())

# Change the current working directory to "d:\\"
os.chdir("g:\\")

# Print the current working directory after changing
print("Current Working Directory after change:", os.getcwd())
