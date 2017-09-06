# Fruitfull functions chapter 6
biggest = max(3, 7, 2, 5)
x = abs (3 - 11) + 10

print(biggest)
print(x)


# Area of a circle fruitful function
def area(radius):
    b = 3.14159 * radius ** 2
    return b

# The above can be written as follows
def area_2(radius):
    return 3.14159 * radius ** 2

# Writing own absolute value function
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

# Another way to write the above function is to leave out the else
def absolute_value_2(x):
    if x < 0:
        return -x
    return x

# Example of a bad function (dead code or unreacheable code)
def bad_absolute_value(x): # if x = 0 the function returns none
    if x < 0:
        return -x
    if x > 0:
        return x

print(bad_absolute_value(0))

# A function that goes through a string and returns first 2 letter word
# if there are none it returns empty string
def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    return ""

print(find_first_2_letter_word(["This", "is", "a", "dead", "parrot"]))
print(find_first_2_letter_word(["I","like","cheese"]))

# Incremental development
# Begining of writing a distance formaula
# Stage 1
def distance_1(x1, y1, x2, y2):
    return 0.0

# Testing function stage 1:
print("Testing stage 1: ", distance_1(1,2,4,6)) # When testing a function it's usefull to know the right answer

# Stage 2: determining difference between x2-x1, y2-y1
def distance_2(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    dsquared = dx*dx + dy*dy
    return dsquared
    # return 0.0

# testing the function stage 2:
print("Testing stage 2: ", distance_2(1,2,4,6)) # should return 25 : temporary test for dsquared value

# Stage 3: Finalising the function returning the square root
def distance_3(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    dsquared = dx * dx + dy * dy
    result = dsquared ** 0.5
    return result

# Testing the final function stage 3:
print("Testing stage 3: ", distance_3(1,2,4,6))

# A simple version with the use of math module can be implemented
# that looks more like the actual pythogorean formula
import math

def distance(x1, y1, x2, y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

print("Distance result using math module: ", distance(1,2,4,6))

# Notes debugging with print
"""
1. Use print functions in order to test outputs and your code 
2. Do not write chatterbox functions, a chatterbox is a fruitful function that, in addition
to it's primary task, also asks the user for input, or prints output, when it would be more 
useful if it simply shut up and did it's work quietly.
3. example: functions like range, max, and abs, wouldn't be useful building blocks for other programs 
if they prompted the user for input or printed results while performing tasks
4. Avoid calling print and input functions inside fruitful functions "unless the primary purpose
of your function is to perform input and output"
5. Use print functions for testing, remove them afterwards.
"""

# Notes : Composition
"""
 - Composition is when you call a function within a function.
 - Example: write a function that takes two points, the center of the circle
 and a point on the perimeter, and computes the area of the circle.
"""

# Example function: Calculating the area of a circle
"""
1. Assume center point is stored in the variables xc and yc, and the permiter point is in
xp and yp.
2. First step is to find the radius of the circle, which is the distance between the
two points. 
3. Formula previously written within a  function distance does that 
radius = distance(xc, yc, xp, yp)
4. Second step is to find the area of a circle with that radius and return it. Again 
use the previously written function area
result = area(radius)
return result
5. Wrap it all in a single function.
"""

def area2(xc, yc, xp, yp): # Final function
    radius = distance(xc,yc,xp,yp)
    result = area_2(radius)
    return  result

# Once the function has been tested and working it can be rewritten to a more concise function
def area2_v2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

# Boolean Functions
"""
 - Functions can return Boolean value, which is often convenient for hiding complicated test inside functions. 
 Example:
"""
def is_divisible(x, y):
    """ Test if x is exactly divisble by y """
    if x % y == 0:
        return True
    else:
        return False

# Can make the above function more concise by doing the following
def is_divisible_2(x ,y):
    return x % y == 0

