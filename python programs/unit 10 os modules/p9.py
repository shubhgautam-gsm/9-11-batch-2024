import os

try:
    fd = "python_xzx.txt"  # Original file name
    new_fd = 'python_121.txt'  # New file name

    # Attempt to rename the file
    os.rename(fd, new_fd)

except FileNotFoundError:
    print("The file you want to rename does not exist.")
except OSError:
    print("There was an issue with renaming the file. The target file might already exist.")
except IOError:
    print("An I/O error occurred. ")
    # ex 'r' file try to write
