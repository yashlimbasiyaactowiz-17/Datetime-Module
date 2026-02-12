# 22. Days in Month

from calendar import monthrange
year = int(input("Enter the year formate %yyyy: "))
month = int(input("Enter the month formate %mm: "))

print(f"In the month of {month} month - {year} year = {monthrange(year,month)[1]} days")