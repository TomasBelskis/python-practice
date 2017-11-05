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

    def tearDown(self):
        pass

