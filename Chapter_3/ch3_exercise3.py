# @author: Tomas Belskis
# EX 3: Write a program that uses a loop to print the following
#   'One of the following months of the year is January'
#   'One of the following months of the year is February'
#   .....

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
for m in months:
    print("One of the following months of the year is " + m)

