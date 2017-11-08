"""
Chapter 7: Iteration
"""
import unittest

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

# The for loop (revision)
for f in ["Zoe", "Joe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    invitation = "Hi " + f + ".  Please come to my party this Saturday!"
    print(invitation)

# Iterating through a list generating a sum total
def mysum(xs):
    """ Sum all the numbers in the list xs, and return total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

# The while statement
def sum_to(n):
    """ Return the sum of 1+2+3 ... n"""
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss

# The Collatz 3n + 1 sequence
def seq3np1(n):
    """ Print the 3n + 1 sequence from n,
        terminating when it reaches 1.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:  # n is even
            n = n // 2
        else:           # n is odd
            n = n + 3 + 1
    print(n, end=".\n" )
# Notes
"""
    Definite iteration: Know ahead of time how many iterations are required,
    some definite bounds for what is needed.
    Indefinite iteration: We don't know how many iterations we need,
    we cannot even establish an upper bound
"""


# 7.6 - Tracing program:
"""
    Ability to go through programs iteration and follow what is being executed,
    and the order of execution.
"""

# 7.7 - Counting digits:
def num_digits(n):
    """ Counts the number of decimal digits in a positive integer. """
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count

def num_zero_and_five_digits(n):
    """ Count digits that are either 0 or 5"""
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count

# 7.8 - Abbreviated assignment
"""
    count += 1 is the same as count = count + 1
"""

# 7.9 - Help and meta-notation
"""
    Meta notation:
    Bold means token, keyword or symbol
    Italic means something of this type
"""

# 7.10 - Tables
def raised_to_power_of_two(n):
    for x in range(n): # Generate numbers
        print(x, "\t", 2**x)
# 7.11 - Two dimensional tables
def two_dimensional_table():
    for i in range(1, 7):
        print(2 * i, end="  ")
    print()
# 7.12 - Encapsulation and generalisation
    """ 
        Encapsulation is the process of wrapping a piece of code in a function.
        Generalisation means taking something specific such as printing the
        multiples of 2 and making it more generic, such as printing multiples
        of any integer.
    """
def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()

# 7.13 - More encapsulation
    """
        Demonstration of more encapsulation, wrapping the code in previous 
        section in a new function.
    """
def print_mult_table():
    for i in range(1, 7):
        print_mult_table(i)

    """
        Notes:
        This process is common development plan. Develop code by writing l
        ines of code outside any function, or typing them in to the interpreter.
        When we get the code working, we extract it and wrap it in a function.
    """
# 7.14 - Local variables
    """
        Variables are local to the functions they are used in, therefore same 
        variable names can be used as long as they are in separate functions.
    """
# 7.15 - The break statement
    """
        Break keyword is used to break out of a loop immediately and continue 
        the program outside of that statement.
    """
def example_break():
    for i in [12, 16, 17, 24, 29]:
        if i % 2 == 1: # If the number is odd
            break      # ... immediately exit the loop
        print(i)
    print("done")

# 7.16 - Other flavours of loops
    """
        Middle test loop with the exit test in the middle of the body, rather
        that at the beginning or at the end. Python uses a combination of 
        while and if condition: break to get the job done.
    """
def example_do_while():
    total = 0
    while True:
        response = input(" Enter the next number. (Leave blank to end)")
        if response == "":
            break
        total += int(response)
    print("The total of the numbers you entered is ", total)

def play_the_game_once():
    print("Playing Game")

def play_one_game():
    while True:
        play_the_game_once()
        response = input("Play again (yes or no)")
        if response != "yes":
            break
    print("Goodbye")



# Test cases:
class TestingExamples(unittest.TestCase):
    def setUp(self):
        pass

    def test_mysum_1(self):
        self.assertEquals(mysum([1, 2, 3, 4, 5]), 10)

    def test_mysum_2(self):
        self.assertEquals(mysum([1.25, 2.5, 1.75]), 5.5)

    def test_mysum_3(self):
        self.assertEquals(mysum([1, -2, 3]), 2)

    def test_mysum_4(self):
        self.assertEquals(mysum([ ]), 0)

    def test_mysum_5(self):
        self.assertEquals(mysum(range(11)), 55) # 11 is not included in the list

    def test_sum_to_1(self):
        self.assertEquals(sum_to(4), 10)

    def test_sum_to_2(self):
        self.assertEquals(sum_to(1000), 500500)

    def test_num_zero_and_five_digits_1(self):
        self.assertEquals(num_zero_and_five_digits(1055030250), 7)

    def tearDown(self):
        pass

