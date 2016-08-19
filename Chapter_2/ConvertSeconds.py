#Chapter 2
#Gets users input for seconds and convers it to hours, minutes and seconds

total_secs = int(input("How many seconds, in total?"))
hours = total_secs//3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, " mins=", minutes, "secs=", secs_finally_remaining)
