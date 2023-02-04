days = int(input("Enter days:"))
year = days // 365
week = (days - year * 365 ) // 7
days = days - year * 365 - week * 7
print(year,week,days)