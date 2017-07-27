"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 6
@description: Write a fruitful function sum_to(n) that returns the sum of
              all integer numbers up to and including n. So sum_to(10) would
               be 1+2+3...+10 which would return the value 55.
"""


def sum_to(n):
    total = 0
    for i in range(n+1):
        total += i

    return total


total = sum_to(10)

print("The total value of N is:", total)

exit=input("Press enter to exit!")