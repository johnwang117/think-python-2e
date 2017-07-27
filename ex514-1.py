import time

local_time = time.time()
print('The standard time is %d second.' % local_time)

seconds = local_time
minutes = seconds / 60
hours = minutes / 60
days = hours / 24

hours_last = hours - int(days) * 24
minutes_last = minutes - int(hours) * 60
seconds_last = seconds - int(minutes) * 60

print('It has been %d days %d hours %d minutes and %d seconds since the epoch.' % (days, hours_last, minutes_last, seconds_last))
