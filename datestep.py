import datetime
from datetime import timedelta
from datetime import date

start_entry = raw_input('Enter start date in YYYY-MM-DD HH:MM:SS format\n')
sparts = start_entry.split()
syear, smonth, sday = map(int, sparts[0].split('-'))
shour, sminute, ssecond = map(int,sparts[1].split(':'))
start_time = datetime.datetime(syear, smonth, sday, shour, sminute, ssecond)

end_entry = raw_input('Enter end date in YYYY-MM-DD HH:MM:SS format\n')
end_day, end_time = end_entry.split()
eyear, emonth, eday = map(int, end_day.split('-'))
ehour, eminute, esecond = map (int,end_time.split(':'))
end_time = datetime.datetime(eyear, emonth, eday, ehour, eminute, esecond)

counter=0
delta = 60
step = timedelta(seconds=delta)
step_date = start_time + step
print
print start_time

while step_date < end_time:
  print step_date.strftime("%Y-%m-%d %H:%M:%S")
  step_date += step
  counter += 1
