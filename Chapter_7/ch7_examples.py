"""
Chapter 7: Iteration
"""

# Assignment operations
airtime_remaining = 15
print(airtime_remaining)
airtime_remaining = 7
print(airtime_remaining)


# Further examples of assignment operation
a = 7
# Illegal assignment
# 7 = a

# In python two variables can  be equal but futher assigning them changes them
a = 5
b = a # After executing this line, b and a are equal
a = 3 # After executing this line, a and b are no longer equal

# Updating variables
n = 5
n = 3 * n + 1

# Getting values that do not exist throw an error
# w = x + 1

# Before updating variables a variable needs to be assigned.
runs_scored = 0
runs_scored = runs_scored + 1 # Incrementing a variable
