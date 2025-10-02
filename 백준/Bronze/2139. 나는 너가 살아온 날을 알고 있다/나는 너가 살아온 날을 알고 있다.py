import sys

date_range = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    date, month, year = map(int, sys.stdin.readline().split())

    if month == date == year == 0:
        break
    
    count = 0

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        count = sum(date_range[:month]) + date

        if 2 < month:
            count += 1
    else:
        count = sum(date_range[:month]) + date
    
    print(count)