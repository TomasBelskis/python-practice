# Fruitful function (function that computes something an returns a value)
# Python generally always returns a value, if no value is set to return it
# returns none.
# Example of interest return function

def final_amt(p, r, n ,t):
    """
     Apply the compound interest formula to p to produce the final ammount.
    """
    a = p * ( 1 + r/n) ** (n*t)
    return a # this is new and what makes the function fruitful.

def final_amt_v2(principalAmount, nominalPercentageRate, numTimesPerYear, years):
    a = principalAmount * (1 + nominalPercentageRate / numTimesPerYear) ** (numTimesPerYear*years)
    return  a

def final_amt_v3(amt, rate, compounded, years):
    a = amt * (1 + rate / compounded) ** (compounded*years)
    return a

# Calling the above function
toIvest = float(input("How much do you want to invest ?"));
fnl = final_amt(toIvest, 0.08, 12, 5)
print("At the end of the period you'll have", fnl)

exit = input("Press enter to exit!")
