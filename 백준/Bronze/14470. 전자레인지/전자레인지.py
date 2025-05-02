# 백준 14470 - 전자레인지
# 분류 : 구현

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A < 0 and B < 0 :
    print((B - A) * C)
elif A < 0 and B > 0 :
    print(-A * C + D + B * E)
else :
    print((B - A) * E)