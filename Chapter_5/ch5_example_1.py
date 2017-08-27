"""Chapter 5 samples boolean values and expressions"""

type(True)
#type(true) # NameError: name 'true' is not defined


5 == (3 + 2) # Is five equal 5 to the result of 3 + 2?
5 == 6
j = "hel"
j + "lo" == "hello"


#x == y # Produce True if ... x is equal to y
#x != y #... x is not equal to y
#x > y # ... x is greater than y
#x < y # ... x is less than y
#x >= y # ... x is greater than or equal to y
#x <= y # ... x is less than or equal to y


age = 18
old_enough_to_get_driving_licence = age >= 17
print(old_enough_to_get_driving_licence)
print(type(old_enough_to_get_driving_licence))

# Conditional execution
if x % 2 == 0:
    print(x, " is even.")
    print("Did you know that 2 is the only even prime number that is prime?")
else:
    print(x, " is odd.")
    print("Did you know that multiplying two odd numbers" + "always gives an odd result?")

# execution continues to the statement after the if.
if x < 0:
    print("The negative number ", x, " is not valid here.")
    x = 42
    print("I've decided to use the number 42 instead.")

print(" The squre root of ", x, "is ", math.sqrt(x))

# Chained Conditionals
if x < y:
    Statements_A
elif x > y:
    Statements_B
else:
    Statements_C

# Nested Conditionals
if x < y:
    Statements_A
else:
    if x > y:
        Statements_B
    else:
        Statements_C

# The return statement
"""
The return statement, with or without a value, depending on whether 
the function is fruitful or void, allows us to terminate the execution 
of a function before (or when) we reach the end. One reason to use an 
early return is if we detect an error condition:
"""
def print_square_root(x):
    if x <= 0:
        print("Positive numbers only, please.")
        return

    result = x**0.5
    print("The square root of", x, "is", result)

# Logical oposites

"""For example, if we wrote this Python:"""
if not (age > 17):
    print("Hey, you're too young to get a driving licence!")

"""it would probably be clearer to use the simplification laws, and to write instead:"""
if age < 17:
    print("Hey, you're too young to get a driving licence!")

# Morgan's Law
"""
For example, suppose we can slay the dragon only if our magic 
lightsabre sword is charged to 90% or higher, and we have 100 
or more energy units in our protective shield. We find this 
fragment of Python code in the game:
"""
if not ((sword_charge >= 0.90) and (shield_energy >= 100)):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")

"""
de Morgan’s laws together with the logical opposites would let
us rework the condition in a (perhaps) easier to understand way 
like this:
"""
if (sword_charge < 0.90) or (shield_energy < 100):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")

"""
We could also get rid of the not by swapping around the then and
else parts of the conditional. So here is a third version, also 
equivalent:
"""
if (sword_charge >= 0.90) and (shield_energy >= 100):
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
else:
    print("Your attack has no effect, the dragon fries you to a crisp!")

# Type Conversion

int("32")
int("Hello") # Will error due to charecters not having integer values
             # (ValueError: invalid literal for int() with base 10: ’Hello’)
int(-2.3) # 2
int(3.99999) # 3
int("42")
int(1.0)

float(32) # 32.0
float("3.14159")
float(1)

str(32)
str(3.14149)
str(True)
str(true) # Will throw an error (Traceback (most recent call last):
          # File "<interactive input>", line 1, in <module>
          # NameError: name ’true’ is not defined
