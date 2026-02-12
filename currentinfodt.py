# 40. Current DateTime Info

import time
from datetime import datetime

# formating for decimal if we not use than gives string error
print(datetime.now())
print(datetime.now().strftime("%y-%m-%d-%H-%M"))#  use for frmating and str
print(datetime.today())
print(datetime.today().strftime(f"today year is %Y or %y"))
print(datetime.today().strftime(f"today month is %m and its represent month or %M its represent minites"))
print(datetime.today().strftime(f"its give the full name of that month %B"))
print(datetime.today().strftime(f"day %W"))
print(datetime.today().strftime(f"day %w"))#Print the weekday of the week (0 for Sunday, 6 for Saturday)
print(datetime.now().strftime(f'hours of curent time %H'))
print(datetime.now().strftime(f'month of current time %M'))
