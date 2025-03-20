# main.py

import calc as mo
import importlib

# Perform addition
result_addition = mo.sum(5, 3)
print("Result of addition:", result_addition)

# Perform subtraction
result_subtraction = mo.sub(8, 4)
print("Result of subtraction:", result_subtraction)

# Now, let's modify the math_operations.py module
with open("math_operations.py", "w") as f:
    f.write("""
def sum(a, b):
    return a + b + 1

def sub(a, b):
    return a - b - 1
""")

# Reload the module
mo = importlib.reload(math_operations)

# Perform addition again with the modified function
result_addition_modified = mo.sum(5, 3)
print("Modified result of addition:", result_addition_modified)

# Perform subtraction again with the modified function
result_subtraction_modified = mo.sub(8, 4)
print("Modified result of subtraction:", result_subtraction_modified)
