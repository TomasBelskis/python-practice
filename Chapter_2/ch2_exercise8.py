#@author Tomas Belskis
#Write a Python program to solve
# the genral version of the above problem (exercise 7).
# Ask the user for the time now (in hours), and ask for
# the number of hours to wait. Your program should output
# what time will be on the clock when the alarm goes off.

current = int(input("What is the time now?  "))
alarm = int(input("How many hours to wait? "))

alarm_time = alarm % 12

time_alarm_goes_off = current + alarm_time

print("The alarm will go off at " + str(time_alarm_goes_off) + " o'clock!")