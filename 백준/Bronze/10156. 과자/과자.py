# 백준 10156 - 과자
# 문제집 : Python 배우기

K, N, M = map(int, input().split())
money = K * N - M
if money < 0 :
    print(0)
else :
    print(money)