# 백준 9610 - 사분면
# 문제집 : Python 배우기 (1 ~ 50)

N = int(input())
A = {'Q1' : 0, 'Q2' : 0, 'Q3' : 0, 'Q4' : 0, 'AXIS' : 0}
for i in range(N) :
    x, y = map(int, input().split())
    if x == 0 or y == 0 :
        A['AXIS'] += 1
    elif x > 0 and y > 0 :
        A['Q1'] += 1
    elif x > 0 and y < 0 :
        A['Q4'] += 1
    elif x < 0 and y > 0 :
        A['Q2'] += 1
    elif x < 0 and y < 0 :
        A['Q3'] += 1

for key, value in A.items() :
    print(f"{key}: {value}")