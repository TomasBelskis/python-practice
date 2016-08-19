#@author Tomas Belskis
#The formula for coputing the final
#  amount if one is earning compound
# interest is given on Wikipeadia as
# A = P (1+r/n)**nt
# Where:
# P = principal amount (initial investment)
# r = anual nominal interest rate (as a decimal)
# n = number of times the interest is compounded per year
# t = number of years

#Write a python program that assigns the principal amount of $10,000 to variable P,
# assign to n the value 12, and assign to r the interest rate of 8%.
#  Then have the program prompt the user for the number of years t
# that the money will be compounded for. Calculate and print the final amount after t years.



p = 10000
r = 0.08
n = 12
t = int(input("Enter the number of years for money to be compounded for: "))

print("Final ammount: ", p*(1+r/n)**n*t)

