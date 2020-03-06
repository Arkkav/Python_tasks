import datetime

yyyy, mm, dd = input().split()
delta = int(input())
d = datetime.date(int(yyyy), int(mm), int(dd)) + datetime.timedelta(days = delta)
print(d.year, d.month, d.day)