# 백준 1789 - 수들의 합
# 문제집 : Python 배우기

N = int(input())
num = 1
total = 0
while True :
    total += num
    if N < total :
        print(num - 1)
        break
    num += 1
        