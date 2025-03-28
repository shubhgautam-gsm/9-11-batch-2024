# main.py

import calc as mo
import importlib

# Perform addition
result_addition = mo.sum(5, 3)
print("Result of addition:", result_addition)

# Perform subtraction
result_subtraction = mo.sub(8, 4)
print("Result of subtraction:", result_subtraction)


# Perform addition again with the modified function
result_addition_modified = mo.sum(5, 3)
print("Modified result of addition:", result_addition_modified)

# Perform subtraction again with the modified function
result_subtraction_modified = mo.sub(8, 4)
print("Modified result of subtraction:", result_subtraction_modified)
