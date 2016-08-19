#@author Tomas Belskis
#You look at the clock and it is exactly 2pm.
# You set an alarm to go off in 51 hours. At what time does the alarm go off?

current_time = 2
alarm_time = 51 % 12 #every 12 hours the clock is at 2,
                   # need the remainder from it to add it to
                   # current time to find out the time of alarm going off

time_alarm_go_off = current_time +alarm_time
print("Time alarm goes off: " + str(time_alarm_go_off))

