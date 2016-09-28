# @author: Tomas Belskis
# EX 5: Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# (a) Write a loop that prints each of the numbers on a new line.
# (b) Write a loop that prints each number and its square on a new line.
# (c) Write a loop that adds all the numbers from the list into a variable
#     called total. You should set the total variable to have the value 0
#     before you start adding them up, and print the value in total after
#     the loop has completed.
# (d) Print the product of all the numbers in the list. (product means all
#     multiplied together)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# (a)
for i in xs:
    print("Number: ", i)

# (b)
for y in xs:
    print("Number: ", y , " Square: ", y**2)
# (c)
total = 0

for z in xs:
    total += z

print("Total: ", total)

# (d)
product = 1

for t in xs:
    product *= t

print("Product: ", product)

