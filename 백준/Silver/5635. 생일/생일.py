# 백준 5635 - 생일
# 분류 : 구현

from datetime import date

N = int(input())
# 1990-01-01 기준
people = []
for _ in range(N) :
    data = input().split()
    name = data[0]
    day = int(data[1])
    month = int(data[2])
    year = int(data[3])

    calc_day = date(year, month, day)

    people.append((name, calc_day))

max_person = max(people, key = lambda x : x[1])
min_person = min(people, key = lambda x : x[1])
print(max_person[0])
print(min_person[0])