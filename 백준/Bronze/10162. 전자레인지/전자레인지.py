# 백준 10162 - 전자레인지
# 문제집 : Python 배우기 (1 ~ 50)

T = int(input())
A, B, C = 0, 0, 0

if T % 10 != 0 :
    print(-1)
else :
    A = T // 300
    T %= 300
    B = T // 60
    T %= 60
    C = T // 10
    print(A, B, C)