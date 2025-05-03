# 백준 31738 - 매우 어려운 문제
# 분류 : 수학
N, M = map(int, input().split())

if N >= M :
    print(0)
else :
    d = 1
    for i in range(1, N + 1) :
        d *= i
        d %= M
        
    print(d)
