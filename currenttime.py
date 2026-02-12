from datetime import datetime

#16. Add Years to Date
def dateyear(d,n):
    return d.replace(d.year + n)

n = int(input("enter the year "))
d = datetime.today()
print(d)
print(dateyear(d.date(),n))


