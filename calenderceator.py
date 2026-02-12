import calendar
year = int(input('enter the year: '))
month= int(input('enter the month: '))
date = calendar.month(year,month)
print(date)