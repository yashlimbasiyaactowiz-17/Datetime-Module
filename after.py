#28. 30 Days Before/After
from datetime import date,timedelta,datetime

currenttime = datetime.now()

befor = date.today()+timedelta(days=30)
after = date.today()-timedelta(days=30)
print(f"This is current date: {date.today()}")
print(f"This is 30 date before date : {befor}")
print(f"This is 30 date after date : {after}")
